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

#ifndef GRAPH_BLOCKMODEL_OVERLAP_UTIL_HH
#define GRAPH_BLOCKMODEL_OVERLAP_UTIL_HH

#include "config.h"
#include <tuple>

#include "../blockmodel/graph_blockmodel.hh"
#include "../blockmodel/graph_blockmodel_util.hh"

namespace graph_tool
{

using namespace boost;

//===============
// Overlap stats
//===============

class overlap_stats_t
{
public:
    typedef pair<size_t, size_t> deg_t;

    typedef vprop_map_t<int32_t>::type ::unchecked_t
        vmap_t;
    typedef vprop_map_t<int64_t>::type ::unchecked_t
        vimap_t;
    typedef vprop_map_t<vector<int64_t>>::type ::unchecked_t
        vvmap_t;

    template <class Graph>
    overlap_stats_t(Graph& g, vmap_t b, vvmap_t half_edges, vimap_t node_index,
                    size_t B)
        : _half_edges(half_edges), _node_index(node_index),
          _out_neighbors(num_vertices(g), _null),
          _in_neighbors(num_vertices(g), _null)
    {
        _block_nodes.resize(B);

        _N = 0;
        for (auto v : vertices_range(g))
        {
            size_t vi = node_index[v];
            _N = std::max(_N, vi + 1);
            size_t kin = in_degreeS()(v, g);
            size_t kout = out_degreeS()(v, g);

            size_t r = b[v];
            auto& bnodes = _block_nodes[r];
            auto& k = bnodes[vi];
            k.first += kin;
            k.second += kout;

            for (auto e : out_edges_range(v, g))
                _out_neighbors[v] = target(e, g);
            for (auto e : in_edges_range(v, g))
                _in_neighbors[v] = source(e, g);
        }

        // parallel edges
        _mi.resize(num_vertices(g), -1);

        for (size_t i = 0; i < _N; ++i)
        {
            auto& he = half_edges[i];

            gt_hash_map<size_t, vector<size_t>> out_us;
            for (auto u : he)
            {
                auto w = _out_neighbors[u];
                if (w == _null)
                    continue;
                if (!is_directed::apply<Graph>::type::value && size_t(node_index[w]) < i)
                    continue;
                out_us[node_index[w]].push_back(u);
            }

            for (auto& uc : out_us)
            {
                if (uc.second.size() > 1)
                {
                    _parallel_bundles.resize(_parallel_bundles.size() + 1);
                    auto& h = _parallel_bundles.back();
                    for (auto u : uc.second)
                    {
                        auto w = _out_neighbors[u];
                        assert(w != _null);
                        _mi[u] = _mi[w] = _parallel_bundles.size() - 1;
                        size_t r = b[u];
                        size_t s = b[w];
                        if (!is_directed::apply<Graph>::type::value && r > s)
                            std::swap(r, s);
                        h[std::make_tuple(r, s, !is_directed::apply<Graph>::type::value && u == w)]++;
                    }
                }
            }
        }
    }

    template <class Graph, class VProp>
    void add_half_edge(size_t v, size_t v_r, VProp& b, Graph&)
    {
        size_t u = _node_index[v];
        size_t kin = (_in_neighbors[v] != _null);
        size_t kout = (_out_neighbors[v] != _null);
        assert(kin + kout == 1);
        auto& k = _block_nodes[v_r][u];
        k.first += kin;
        k.second += kout;

        int m = _mi[v];
        if (m != -1)
        {
            size_t r, s;
            auto u = _out_neighbors[v];
            if (u == _null)
            {
                u = _in_neighbors[v];
                r = b[u];
                s = v_r;
            }
            else
            {
                r = v_r;
                s = b[u];
            }
            auto& h = _parallel_bundles[m];
            if (!is_directed::apply<Graph>::type::value && r > s)
                std::swap(r, s);
            h[std::make_tuple(r, s, !is_directed::apply<Graph>::type::value && u == v)]++;
        }
    }

    template <class Graph, class VProp>
    void remove_half_edge(size_t v, size_t v_r, VProp& b, Graph&)
    {
        size_t u = _node_index[v];
        size_t kin = (_in_neighbors[v] != _null);
        size_t kout = (_out_neighbors[v] != _null);
        assert(kin + kout == 1);
        auto& k = _block_nodes[v_r][u];
        k.first -= kin;
        k.second -= kout;

        if (k.first + k.second == 0)
            _block_nodes[v_r].erase(u);

        int m = _mi[v];
        if (m != -1)
        {
            size_t r, s;
            auto u = _out_neighbors[v];
            if (u == _null)
            {
                u = _in_neighbors[v];
                r = b[u];
                s = v_r;
            }
            else
            {
                r = v_r;
                s = b[u];
            }
            auto& h = _parallel_bundles[m];
            if (!is_directed::apply<Graph>::type::value && r > s)
                std::swap(r, s);
            auto iter = h.find(std::make_tuple(r, s, !is_directed::apply<Graph>::type::value && u == v));
            assert(iter->second > 0);
            iter->second--;
            if (iter->second == 0)
                h.erase(iter);
        }
    }

    size_t get_block_size(size_t r) const
    {
        return _block_nodes[r].size();
    }

    size_t virtual_remove_size(size_t v, size_t r, size_t in_deg = 0,
                               size_t out_deg = 0) const
    {
        size_t nr = _block_nodes[r].size();
        size_t u = _node_index[v];
        size_t kin = (in_deg + out_deg) > 0 ?
            in_deg : (_in_neighbors[v] != _null);
        size_t kout = (in_deg + out_deg) > 0 ?
            out_deg : (_out_neighbors[v] != _null);
        const auto iter = _block_nodes[r].find(u);
        const auto& deg = iter->second;
        if (deg.first == kin && deg.second == kout)
            nr--;
        return nr;
    }

    size_t virtual_add_size(size_t v, size_t r) const
    {
        size_t nr = _block_nodes[r].size();
        size_t u = _node_index[v];
        const auto& bnodes = _block_nodes[r];
        if (bnodes.find(u) == bnodes.end())
            nr++;
        return nr;
    }

    template <class Graph>
    double virtual_move_dS(size_t v, size_t r, size_t nr, Graph& g,
                           size_t in_deg = 0, size_t out_deg = 0) const
    {
        double dS = 0;

        size_t u = _node_index[v];
        size_t u_kin = ((in_deg + out_deg) > 0) ? in_deg : in_degreeS()(v, g);
        size_t u_kout = ((in_deg + out_deg) > 0) ? out_deg : out_degreeS()(v, g);

        auto deg =  _block_nodes[r].find(u)->second;
        auto ndeg = deg;
        ndeg.first -= u_kin;
        ndeg.second -= u_kout;

        dS -= lgamma_fast(ndeg.first + 1) + lgamma_fast(ndeg.second + 1);
        dS += lgamma_fast(deg.first + 1) + lgamma_fast(deg.second + 1);

        const auto iter = _block_nodes[nr].find(u);
        if (iter != _block_nodes[nr].end())
            deg = iter->second;
        else
            deg = make_pair(0, 0);
        ndeg = deg;
        ndeg.first += u_kin;
        ndeg.second += u_kout;

        dS -= lgamma_fast(ndeg.first + 1) + lgamma_fast(ndeg.second + 1);
        dS += lgamma_fast(deg.first + 1) + lgamma_fast(deg.second + 1);

        return dS;
    }

    template <class Graph, class VProp>
    double virtual_move_parallel_dS(size_t v, size_t v_r, size_t v_nr, VProp& b,
                                    Graph&, bool bundled=false) const
    {
        int m = _mi[v];
        if (m == -1)
            return 0;

        size_t r, s, nr, ns;
        size_t u = _out_neighbors[v];
        if (u == _null)
        {
            u = _in_neighbors[v];
            r = b[u];
            s = v_r;
            nr = r;
            ns = v_nr;
        }
        else
        {
            r = v_r;
            s = b[u];
            nr = v_nr;
            ns = s;
        }

        if (!is_directed::apply<Graph>::type::value && r > s)
            std::swap(r, s);
        if (!is_directed::apply<Graph>::type::value && nr > ns)
            std::swap(nr, ns);

        auto& h = _parallel_bundles[m];

        auto get_h = [&](const std::tuple<size_t, size_t, bool>& k) -> int
            {
                const auto iter = h.find(k);
                if (iter == h.end())
                    return 0;
                return iter->second;
            };

        bool is_loop = !is_directed::apply<Graph>::type::value && u == v;
        int c  = get_h(std::make_tuple(r,  s, is_loop));
        int nc = get_h(std::make_tuple(nr, ns, is_loop));

        assert(c > 0);
        assert(nc >= 0);
        assert(v_r != v_nr);
        assert(make_pair(r, s) != make_pair(nr, ns));

        double S = 0;
        S -= lgamma_fast(c + 1) + lgamma_fast(nc + 1);
        if (!bundled)
            S += lgamma_fast(c) + lgamma_fast(nc + 2);
        else
            S += lgamma_fast(c + nc + 1);

        return S;
    }

    // sample another half-edge adjacent to the node w
    template <class RNG>
    size_t sample_half_edge(size_t w, RNG& rng) const
    {
        auto& half_edges = _half_edges[w];
        return uniform_sample(half_edges, rng);
    }

    size_t get_node(size_t v) const { return _node_index[v]; }
    const vector<int64_t>& get_half_edges(size_t v) const { return _half_edges[v]; }

    auto get_out_neighbor(size_t v) const { return _out_neighbors[v]; }
    auto get_in_neighbor(size_t v) const { return _in_neighbors[v]; }


    typedef gt_hash_map<std::tuple<size_t, size_t, bool>, int> phist_t;

    const vector<phist_t>& get_parallel_bundles() const { return _parallel_bundles; }
    const vector<int>& get_mi() const { return _mi; }

    size_t get_N() const { return _N; }

    void add_block()
    {
        _block_nodes.emplace_back();
    }

    static constexpr size_t _null = numeric_limits<size_t>::max();

private:

    vvmap_t _half_edges;     // half-edges to each node
    vimap_t _node_index;     // node to each half edges
    size_t _N;

    typedef gt_hash_map<size_t, deg_t> node_map_t;

    vector<node_map_t> _block_nodes; // nodes (and degrees) in each block

    vector<size_t> _out_neighbors;
    vector<size_t> _in_neighbors;


    vector<int> _mi;
    vector<phist_t> _parallel_bundles; // parallel edge bundles
};


template <class Graph, class BGraph, class... EVals>
class SingleEntrySet
{
public:
    typedef typename graph_traits<BGraph>::edge_descriptor bedge_t;

    SingleEntrySet() : _pos(0), _mes_pos(0) {}
    SingleEntrySet(size_t) : SingleEntrySet() {}

    void set_move(size_t, size_t, size_t) { clear(); }

    template <bool Add, class... DVals>
    void insert_delta(size_t t, size_t s, DVals... delta)
    {
        if (!is_directed::apply<Graph>::type::value && (t > s))
            std::swap(t, s);
        _entries[_pos] = make_pair(t, s);
        if (Add)
            tuple_op(_delta[_pos], [&](auto& r, auto& v){ r += v; },
                     delta...);
        else
            tuple_op(_delta[_pos], [&](auto& r, auto& v){ r -= v; },
                     delta...);
        ++_pos;
    }

    const auto& get_delta(size_t t, size_t s)
    {
        if (!is_directed::apply<Graph>::type::value && (t > s))
            std::swap(t, s);
        for (size_t i = 0; i < 2; ++i)
        {
            auto& entry = _entries[i];
            if (entry.first == t && entry.second == s)
                return _delta[i];
        }
        return _null_delta;
    }

    void clear()
    {
        for (auto& d : _delta)
            d = std::tuple<EVals...>();
        _pos = 0;
        _mes_pos = 0;
    }

    const std::array<pair<size_t, size_t>,2>& get_entries() const { return _entries; }
    const std::array<std::tuple<EVals...>, 2>& get_delta() const { return _delta; }
    const bedge_t& get_null_edge() const { return _null_edge; }

    template <class Emat>
    std::array<bedge_t, 2>& get_mes(Emat& emat)
    {
        for (; _mes_pos < 2; ++_mes_pos)
        {
            auto& entry = _entries[_mes_pos];
            _mes[_mes_pos] = emat.get_me(entry.first, entry.second);
        }
        return _mes;
    }

    template <class Emat>
    const bedge_t& get_me(size_t t, size_t s, Emat& emat)
    {
        if (!is_directed::apply<Graph>::type::value && (t > s))
            std::swap(t, s);
        for (size_t i = 0; i < 2; ++i)
        {
            auto& entry = _entries[i];
            if (entry.first == t && entry.second == s)
            {
                if (i >= _mes_pos)
                {
                    _mes[i] = emat.get_me(t, s);
                    _mes_pos++;
                }
                return _mes[i];
            }
        }
        return emat.get_me(t, s);
    }

    std::tuple<EVals...> _self_weight;

    std::vector<std::tuple<size_t, size_t,
                           GraphInterface::edge_t, int, std::vector<double>>>
        _recs_entries;

private:
    size_t _pos;
    std::array<pair<size_t, size_t>, 2> _entries;
    std::array<std::tuple<EVals...>, 2> _delta;
    std::array<bedge_t, 2> _mes;
    size_t _mes_pos;

    static const std::tuple<EVals...> _null_delta;
    static const bedge_t _null_edge;
};

template <class Graph, class BGraph, class... EVals>
const std::tuple<EVals...> SingleEntrySet<Graph, BGraph, EVals...>::_null_delta;

template <class Graph, class BGraph, class... EVals>
const typename SingleEntrySet<Graph, BGraph, EVals...>::bedge_t
SingleEntrySet<Graph, BGraph, EVals...>::_null_edge;

struct is_loop_overlap
{
    is_loop_overlap(const overlap_stats_t& os)
        : _overlap_stats(os) {}
    const overlap_stats_t& _overlap_stats;

    bool operator()(size_t v) const
    {
        auto u = _overlap_stats.get_out_neighbor(v);
        if (u == _overlap_stats._null)
             u = _overlap_stats.get_in_neighbor(v);
        return _overlap_stats.get_node(v) == _overlap_stats.get_node(u);
    }
};

} // namespace graph_tool

#include "graph_blockmodel_overlap_partition.hh"

#endif // GRAPH_BLOCKMODEL_OVERLAP_UTIL_HH
