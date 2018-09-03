// graph-tool -- a general graph modification and manipulation thingy
//
// Copyright (C) 2006-2017 Tiago de Paula Peixoto <tiago@skewed.de>
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 3
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

#ifndef GRAPH_BLOCKMODEL_ELIST_HH
#define GRAPH_BLOCKMODEL_ELIST_HH

#include "../generation/sampler.hh"
#include "../generation/dynamic_sampler.hh"

namespace graph_tool
{

// ====================================
// Construct and manage half-edge lists
// ====================================

//the following guarantees a stable (source, target) ordering even for
//undirected graphs
template <class Edge, class Graph>
inline typename graph_traits<Graph>::vertex_descriptor
get_source(const Edge& e, const Graph &g)
{
    if (is_directed::apply<Graph>::type::value)
        return source(e, g);
    return std::min(source(e, g), target(e, g));
}

template <class Edge, class Graph>
inline typename graph_traits<Graph>::vertex_descriptor
get_target(const Edge& e, const Graph &g)
{
    if (is_directed::apply<Graph>::type::value)
        return target(e, g);
    return std::max(source(e, g), target(e, g));
}


template <class Graph, class Weighted>
class EGroups
{
public:
    template <class Vprop, class Eprop, class BGraph>
    void init(Vprop b, Eprop eweight, Graph& g, BGraph& bg)
    {
        _egroups.clear();
        _egroups.resize(num_vertices(bg));

        for (auto e : edges_range(g))
        {
            _epos[e] = make_pair(numeric_limits<size_t>::max(),
                                 numeric_limits<size_t>::max());
            insert_edge(e, eweight[e], b, g);
        }
    }

    void clear()
    {
        _egroups.clear();
    }

    bool empty()
    {
        return _egroups.empty();
    }

    template <class Vprop>
    bool check(Vprop b, Graph& g)
    {
        for (size_t r = 0; r < _egroups.size(); ++r)
        {
            auto& edges = _egroups[r];
            for (size_t i = 0; i < edges.size(); ++i)
            {
                const auto& e = edges[i];
                if (!is_valid(i, edges))
                    continue;
                if (size_t(b[source(get<0>(e), g)]) != r &&
                    size_t(b[target(get<0>(e), g)]) != r)
                {
                    assert(false);
                    return false;
                }
            }
        }
        return true;
    }

    template <class Edge>
    bool is_valid(size_t i, DynamicSampler<Edge>& elist)
    {
        return elist.is_valid(i);
    }

    template <class Edge>
    bool is_valid(size_t, vector<Edge>&)
    {
        return true;
    }

    template <class Edge, class Vprop>
    void insert_edge(const Edge& e, size_t weight, Vprop& b, Graph& g)
    {
        size_t r = b[get_source(e, g)];
        auto& r_elist = _egroups[r];
        insert_edge(std::make_tuple(e, true), r_elist, weight,
                    _epos[e].first);

        size_t s = b[get_target(e, g)];
        auto& s_elist = _egroups[s];
        insert_edge(std::make_tuple(e, false), s_elist, weight,
                    _epos[e].second);
    }

    template <class Edge, class EV>
    void insert_edge(const Edge& e, EV& elist, size_t, size_t& pos)
    {
        if (pos < elist.size() && elist[pos] == e)
            return;
        assert(pos >= elist.size() || elist[pos] != e);
        elist.push_back(e);
        pos = elist.size() - 1;
    }

    template <class Edge>
    void insert_edge(const Edge& e, DynamicSampler<Edge>& elist,
                     size_t weight, size_t& pos)
    {
        if ((pos < elist.size() && elist.is_valid(pos) && elist[pos] == e) ||
            weight == 0)
            return;
        assert(pos >= elist.size() || !elist.is_valid(pos) || elist[pos] != e);
        pos = elist.insert(e, weight);
    }

    template <class Edge, class Vprop>
    void remove_edge(const Edge& e, Vprop& b, Graph& g)
    {
        auto& pos = _epos[e];

        size_t r = b[get_source(e, g)];
        remove_edge(make_tuple(e, true), pos.first, _egroups[r]);

        size_t s = b[get_target(e, g)];
        remove_edge(make_tuple(e, false), pos.second, _egroups[s]);
    }

    template <class Edge>
    void remove_edge(const Edge& e, size_t pos, vector<Edge>& elist)
    {
        if (pos >= elist.size() || elist[pos] != e)
            return;
        if (get<1>(elist.back()))
            _epos[get<0>(elist.back())].first = pos;
        else
            _epos[get<0>(elist.back())].second = pos;
        if (get<1>(elist[pos]))
            _epos[get<0>(elist[pos])].first = numeric_limits<size_t>::max();
        else
            _epos[get<0>(elist[pos])].second = numeric_limits<size_t>::max();
        elist[pos] = elist.back();
        elist.pop_back();
    }

    template <class Edge>
    void remove_edge(const Edge& e, size_t pos, DynamicSampler<Edge>& elist)
    {
        if (pos >= elist.size() || elist[pos] != e)
            return;
        if (get<1>(elist[pos]))
            _epos[get<0>(elist[pos])].first = numeric_limits<size_t>::max();
        else
            _epos[get<0>(elist[pos])].second = numeric_limits<size_t>::max();
        elist.remove(pos);
    }

    template <class Vertex, class VProp>
    void remove_vertex(Vertex v, VProp& b, Graph& g)
    {
        if (_egroups.empty())
            return;
        // update the half-edge lists
        for (auto e : out_edges_range(v, g))
            remove_edge(e, b, g);
        for (auto e : in_edges_range(v, g))
            remove_edge(e, b, g);
    }

    template <class Vertex, class Vprop, class Eprop>
    void add_vertex(Vertex v, Vprop& b, Eprop& eweight, Graph& g)
    {
        if (_egroups.empty())
            return;
        //update the half-edge lists
        for (auto e : out_edges_range(v, g))
            insert_edge(e, eweight[e], b, g);
        for (auto e : in_edges_range(v, g))
            insert_edge(e, eweight[e], b, g);
    }

    template <class Edge, class RNG>
    const auto& sample_edge(const DynamicSampler<Edge>& elist, RNG& rng)
    {
        return get<0>(elist.sample(rng));
    }

    template <class Edge, class RNG>
    const auto& sample_edge(const vector<Edge>& elist, RNG& rng)
    {
        return get<0>(uniform_sample(elist, rng));
    }

    template <class Vertex, class RNG>
    const auto& sample_edge(Vertex r, RNG& rng)
    {
        return sample_edge(_egroups[r], rng);
    }

private:
    typedef typename std::conditional<Weighted::value,
                                      DynamicSampler<std::tuple<typename graph_traits<Graph>::edge_descriptor, bool>>,
                                      vector<std::tuple<typename graph_traits<Graph>::edge_descriptor, bool>>>::type
        sampler_t;
    vector<sampler_t> _egroups;

    typedef typename eprop_map_t<pair<size_t, size_t>>::type epos_t;
    epos_t _epos;
};

} // namespace graph_tool

#endif //GRAPH_BLOCKMODEL_ELIST_HH
