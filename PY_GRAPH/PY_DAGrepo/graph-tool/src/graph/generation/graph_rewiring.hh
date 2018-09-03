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

#ifndef GRAPH_REWIRING_HH
#define GRAPH_REWIRING_HH

#include <tuple>
#include <iostream>
#include <boost/functional/hash.hpp>

#include "graph.hh"
#include "graph_filtering.hh"
#include "graph_util.hh"
#include "sampler.hh"

#include "random.hh"

#include "hash_map_wrap.hh"

namespace graph_tool
{
using namespace std;
using namespace boost;

template <class Graph>
typename graph_traits<Graph>::vertex_descriptor
source(const pair<size_t, bool>& e,
       const vector<typename graph_traits<Graph>::edge_descriptor>& edges,
       const Graph& g)
{
    if (e.second)
        return target(edges[e.first], g);
    else
        return source(edges[e.first], g);
}

template <class Graph>
typename graph_traits<Graph>::vertex_descriptor
target(const pair<size_t, bool>& e,
       const vector<typename graph_traits<Graph>::edge_descriptor>& edges,
       const Graph& g)
{
    if (e.second)
        return source(edges[e.first], g);
    else
        return target(edges[e.first], g);
}


template <class Nmap, class Graph>
void add_count(size_t s, size_t t, Nmap& nvmap, Graph&)
{
    if (!is_directed::apply<Graph>::type::value && s > t)
        std::swap(s, t);
    auto& nmap = nvmap[s];
    nmap[t]++;
}

template <class Nmap, class Graph>
void remove_count(size_t s, size_t t, Nmap& nvmap, Graph&)
{
    if (!is_directed::apply<Graph>::type::value && s > t)
        std::swap(s, t);
    auto& nmap = nvmap[s];
    auto iter = nmap.find(t);
    iter->second--;
    if (iter->second == 0)
        nmap.erase(iter);
}

template <class Nmap, class Graph>
size_t get_count(size_t s, size_t t, Nmap& nvmap, Graph&)
{
    if (!is_directed::apply<Graph>::type::value && s > t)
        std::swap(s, t);
    auto& nmap = nvmap[s];
    auto iter = nmap.find(t);
    if (iter == nmap.end())
        return 0;
    return iter->second;
    // if (s != t)
    //     return iter->second;
    // else
    //     return iter->second / 2;
}

// this functor will swap the source of the edge e with the source of edge se
// and the target of edge e with the target of te
struct swap_edge
{
    template <class Nmap, class Graph>
    static bool
    parallel_check_target (const pair<size_t, bool>& e,
                           const pair<size_t, bool>& te,
                           vector<typename graph_traits<Graph>::edge_descriptor>& edges,
                           Nmap& nmap,
                           const Graph &g)
    {
        // We want to check that if we swap the target of 'e' with the target of
        // 'te', as such
        //
        //  (s)    -e--> (t)          (s)    -e--> (nt)
        //  (te_s) -te-> (nt)   =>    (te_s) -te-> (t)
        //
        // no parallel edges are introduced.

        typename graph_traits<Graph>::vertex_descriptor
            s = source(e, edges, g),          // current source
            t = target(e, edges, g),          // current target
            nt = target(te, edges, g),        // new target
            te_s = source(te, edges, g);      // target edge source

        if (get_count(s,  nt, nmap, g) > 0)
            return true; // e would clash with an existing edge
        if (get_count(te_s, t, nmap, g) > 0)
            return true; // te would clash with an existing edge
        return false; // no parallel edges
    }

    template <class Graph>
    static void swap_target
        (const pair<size_t, bool>& e,
         const pair<size_t, bool>& te,
         vector<typename graph_traits<Graph>::edge_descriptor>& edges,
         Graph& g)
    {
        // swap the target of the edge 'e' with the target of edge 'te', as
        // such:
        //
        //  (s)    -e--> (t)          (s)    -e--> (nt)
        //  (te_s) -te-> (nt)   =>    (te_s) -te-> (t)

        if (e.first == te.first)
            return;

        // new edges which will replace the old ones
        typename graph_traits<Graph>::edge_descriptor ne, nte;
        typename graph_traits<Graph>::vertex_descriptor
            s_e = source(e, edges, g),
            t_e = target(e, edges, g),
            s_te = source(te, edges, g),
            t_te = target(te, edges, g);
        remove_edge(edges[e.first], g);
        remove_edge(edges[te.first], g);

        if (is_directed::apply<Graph>::type::value || !e.second)
            ne = add_edge(s_e, t_te, g).first;
        else // keep invertedness (only for undirected graphs)
            ne = add_edge(t_te, s_e, g).first;
        edges[e.first] = ne;
        if (is_directed::apply<Graph>::type::value || !te.second)
            nte = add_edge(s_te, t_e, g).first;
        else // keep invertedness (only for undirected graphs)
            nte = add_edge(t_e, s_te,  g).first;
        edges[te.first] = nte;
    }

};

// used for verbose display
void print_progress(size_t i, size_t n_iter, size_t current, size_t total,
                    stringstream& str)
{
    size_t atom = (total > 200) ? total / 100 : 1;
    if ( ( (current+1) % atom == 0) || (current + 1) == total)
    {
        size_t size = str.str().length();
        for (size_t j = 0; j < str.str().length(); ++j)
            cout << "\b";
        str.str("");
        str << "(" << i + 1 << " / " << n_iter << ") "
            << current + 1 << " of " << total << " ("
            << (current + 1) * 100 / total << "%)";
        for (int j = 0; j < int(size - str.str().length()); ++j)
            str << " ";
        cout << str.str() << flush;
    }
}

//select blocks based on in/out degrees
class DegreeBlock
{
public:
    typedef pair<size_t, size_t> block_t;

    template <class Graph>
    block_t get_block(typename graph_traits<Graph>::vertex_descriptor v,
                      const Graph& g) const
    {
        return make_pair(in_degreeS()(v, g), out_degree(v, g));
    }
};

//select blocks based on property map
template <class PropertyMap>
class PropertyBlock
{
public:
    typedef typename property_traits<PropertyMap>::value_type block_t;

    PropertyBlock(PropertyMap p): _p(p) {}

    template <class Graph>
    block_t get_block(typename graph_traits<Graph>::vertex_descriptor v,
                      const Graph&) const
    {
        return get(_p, v);
    }

private:
    PropertyMap _p;
};

// select an appropriate "null" key for densehash
template <class Type>
struct get_null_key
{
    Type operator()() const
    {
        return numeric_limits<Type>::max();
    }
};

template <>
struct get_null_key<string>
{
    string operator()() const
    {
        return lexical_cast<string>(get_null_key<size_t>()());
    }
};

template <>
struct get_null_key<boost::python::object>
{
    boost::python::object operator()() const
    {
        return boost::python::object();
    }
};

template <class Type>
struct get_null_key<vector<Type>>
{
    vector<Type> operator()() const
    {
        vector<Type> v(1);
        v[0] = get_null_key<Type>()();
        return v;
    }
};

template <class Type1, class Type2>
struct get_null_key<pair<Type1, Type2>>
{
    pair<Type1, Type2> operator()() const
    {
        return make_pair(get_null_key<Type1>()(),
                         get_null_key<Type2>()());
    }
};


// main rewire loop
template <template <class Graph, class EdgeIndexMap, class CorrProb,
                    class BlockDeg>
          class RewireStrategy>
struct graph_rewire
{

    template <class Graph, class EdgeIndexMap, class CorrProb,
              class BlockDeg, class PinMap>
    void operator()(Graph& g, EdgeIndexMap edge_index, CorrProb corr_prob,
                    PinMap pin, bool self_loops, bool parallel_edges,
                    bool configuration, pair<size_t, bool> iter_sweep,
                    std::tuple<bool, bool, bool> cache_verbose, size_t& pcount,
                    rng_t& rng, BlockDeg bd) const
    {
        typedef typename graph_traits<Graph>::edge_descriptor edge_t;
        bool persist = std::get<0>(cache_verbose);
        bool cache = std::get<1>(cache_verbose);
        bool verbose = std::get<2>(cache_verbose);

        vector<edge_t> edges;
        vector<size_t> edge_pos;
        typename graph_traits<Graph>::edge_iterator e, e_end;
        for (tie(e, e_end) = boost::edges(g); e != e_end; ++e)
        {
            if (pin[*e])
                continue;
            edges.push_back(*e);
            edge_pos.push_back(edge_pos.size());
        }

        typedef random_permutation_iterator<typename vector<size_t>::iterator,
                                            rng_t>
            random_edge_iter;

        RewireStrategy<Graph, EdgeIndexMap, CorrProb, BlockDeg>
            rewire(g, edge_index, edges, corr_prob, bd, cache, rng,
                   parallel_edges, configuration);

        size_t niter;
        bool no_sweep;
        tie(niter, no_sweep) = iter_sweep;
        pcount = 0;
        if (verbose)
            cout << "rewiring edges: ";
        stringstream str;
        for (size_t i = 0; i < niter; ++i)
        {
            random_edge_iter
                ei_begin(edge_pos.begin(), edge_pos.end(), rng),
                ei_end(edge_pos.end(), edge_pos.end(), rng);

            for (random_edge_iter ei = ei_begin; ei != ei_end; ++ei)
            {
                size_t e_pos = ei - ei_begin;
                if (verbose)
                    print_progress(i, niter, e_pos, no_sweep ? 1 : edges.size(),
                                   str);

                size_t e = *ei;

                bool success = false;
                do
                {
                    success = rewire(e, self_loops, parallel_edges);
                }
                while(persist && !success);

                if (!success)
                    ++pcount;

                if (no_sweep)
                    break;
            }
        }
        if (verbose)
            cout << endl;
    }

    template <class Graph, class EdgeIndexMap, class CorrProb, class PinMap>
    void operator()(Graph& g, EdgeIndexMap edge_index, CorrProb corr_prob,
                    PinMap pin, bool self_loops, bool parallel_edges,
                    bool configuration, pair<size_t, bool> iter_sweep,
                    std::tuple<bool, bool, bool> cache_verbose, size_t& pcount,
                    rng_t& rng) const
    {
        operator()(g, edge_index, corr_prob, pin, self_loops, parallel_edges,
                   configuration, iter_sweep, cache_verbose, pcount, rng,
                   DegreeBlock());
    }
};


// this will rewire the edges so that the resulting graph will be entirely
// random (i.e. Erdos-Renyi)
template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg>
class ErdosRewireStrategy
{
public:
    typedef typename graph_traits<Graph>::edge_descriptor edge_t;
    typedef typename EdgeIndexMap::value_type index_t;

    ErdosRewireStrategy(Graph& g, EdgeIndexMap edge_index,
                        vector<edge_t>& edges, CorrProb, BlockDeg,
                        bool, rng_t& rng, bool, bool configuration)
        : _g(g), _edge_index(edge_index), _edges(edges),
          _vertices(HardNumVertices()(g)), _rng(rng),
          _configuration(configuration),
          _nmap(get(vertex_index, g), num_vertices(g))
    {
        decltype(_vertices.begin()) viter = _vertices.begin();
        typename graph_traits<Graph>::vertex_iterator v, v_end;
        for (tie(v, v_end) = vertices(_g); v != v_end; ++v)
            *(viter++) = *v;

        if (!configuration)
        {
            for (size_t i = 0; i < edges.size(); ++i)
                add_count(source(edges[i], g), target(edges[i], g), _nmap, g);
        }
    }

    bool operator()(size_t ei, bool self_loops, bool parallel_edges)
    {
        size_t e_s = source(_edges[ei], _g);
        size_t e_t = target(_edges[ei], _g);

        if (!is_directed::apply<Graph>::type::value && e_s > e_t)
            std::swap(e_s, e_t);

        //try randomly drawn pairs of vertices
        std::uniform_int_distribution<size_t> sample(0, _vertices.size() - 1);
        typename graph_traits<Graph>::vertex_descriptor s, t;
        while (true)
        {
            s = sample(_rng);
            t = sample(_rng);
            if (s == t)
            {
                if (!self_loops) // reject self-loops if not allowed
                    continue;

            }
            else if (!is_directed::apply<Graph>::type::value && self_loops)
            {
                // sample self-loops w/ correct probability for undirected
                // graphs
                std::bernoulli_distribution reject(.5);
                if (reject(_rng))
                    continue;
            }
            break;
        }

        if (!is_directed::apply<Graph>::type::value && s > t)
            std::swap(s, t);

        if (s == e_s && t == e_t)
            return false;

        // reject parallel edges if not allowed
        if (!parallel_edges && is_adjacent(s, t, _g))
            return false;

        if (!_configuration)
        {
            size_t m = get_count(s, t, _nmap, _g);
            size_t m_e = get_count(e_s, e_t, _nmap, _g);

            double a = (m + 1) / double(m_e);

            std::bernoulli_distribution accept(std::min(a, 1.));
            if (!accept(_rng))
                return false;
        }

        remove_edge(_edges[ei], _g);
        edge_t ne = add_edge(s, t, _g).first;
        _edges[ei] = ne;

        if (!_configuration)
        {
            remove_count(e_s, e_t, _nmap, _g);
            add_count(s, t, _nmap, _g);
        }

        return true;
    }

private:
    Graph& _g;
    EdgeIndexMap _edge_index;
    vector<edge_t>& _edges;
    vector<typename graph_traits<Graph>::vertex_descriptor> _vertices;
    rng_t& _rng;
    bool _configuration;
    typedef gt_hash_map<size_t, size_t> nmapv_t;
    typedef typename property_map_type::apply<nmapv_t,
                                              typename property_map<Graph, vertex_index_t>::type>
        ::type::unchecked_t nmap_t;
    nmap_t _nmap;
};



// this is the mother class for edge-based rewire strategies
// it contains the common loop for finding edges to swap, so different
// strategies need only to specify where to sample the edges from.
template <class Graph, class EdgeIndexMap, class RewireStrategy>
class RewireStrategyBase
{
public:
    typedef typename graph_traits<Graph>::edge_descriptor edge_t;
    typedef typename graph_traits<Graph>::vertex_descriptor vertex_t;

    typedef typename EdgeIndexMap::value_type index_t;

    RewireStrategyBase(Graph& g, EdgeIndexMap edge_index, vector<edge_t>& edges,
                       rng_t& rng, bool parallel_edges, bool configuration)
        : _g(g), _edge_index(edge_index), _edges(edges), _rng(rng),
          _nmap(get(vertex_index, g), num_vertices(g)),
          _configuration(configuration)
    {
        if (!parallel_edges || !configuration)
        {
            for (size_t i = 0; i < edges.size(); ++i)
                add_count(source(edges[i], g), target(edges[i], g), _nmap, g);
        }
    }

    bool operator()(size_t ei, bool self_loops, bool parallel_edges)
    {
        RewireStrategy& self = *static_cast<RewireStrategy*>(this);

        // try randomly drawn pairs of edges and check if they satisfy all the
        // consistency checks

        pair<size_t, bool> e = make_pair(ei, false);

        // rewire target
        pair<size_t, bool> et = self.get_target_edge(e, parallel_edges);

        if (et.first == ei)
            return false;

        auto s = source(e,  _edges, _g);
        auto t = target(e,  _edges, _g);
        auto ts = source(et,  _edges, _g);
        auto tt = target(et,  _edges, _g);

        if (!self_loops) // reject self-loops if not allowed
        {
            if(s == tt || ts == t)
                return false;
        }

        // reject parallel edges if not allowed
        if (!parallel_edges && (et.first != e.first))
        {
            if (swap_edge::parallel_check_target(e, et, _edges, _nmap, _g))
                return false;
        }

        double a = 0;

        if (!is_directed::apply<Graph>::type::value)
        {
            a -= log(2 + (s == t) + (ts == tt));
            a += log(2 + (s == tt) + (ts == t));
        }

        if (!_configuration)
        {
            map<std::pair<size_t, size_t>, int> delta;

            delta[std::make_pair(s, t)] -= 1;
            delta[std::make_pair(ts, tt)] -= 1;
            delta[std::make_pair(s, tt)] += 1;
            delta[std::make_pair(ts, t)] += 1;

            for (auto& e_d : delta)
            {
                auto u = e_d.first.first;
                auto v = e_d.first.second;
                int d = e_d.second;
                size_t m = get_count(u,  v,  _nmap, _g);
                a -= lgamma(m + 1) - lgamma((m + 1) + d);
                if (!is_directed::apply<Graph>::type::value && u == v)
                    a += d * log(2);
            }

        }

        std::bernoulli_distribution accept(std::min(exp(a), 1.));
        if (!accept(_rng))
            return false;

        self.update_edge(e.first, false);
        self.update_edge(et.first, false);

        if (!parallel_edges || !_configuration)
        {
            remove_count(source(e, _edges, _g), target(e, _edges, _g), _nmap, _g);
            remove_count(source(et, _edges, _g), target(et, _edges, _g), _nmap, _g);
        }

        swap_edge::swap_target(e, et, _edges, _g);

        self.update_edge(e.first, true);
        self.update_edge(et.first, true);

        if (!parallel_edges || !_configuration)
        {
            add_count(source(e, _edges, _g), target(e, _edges, _g), _nmap, _g);
            add_count(source(et, _edges, _g), target(et, _edges, _g), _nmap, _g);
        }

        return true;
    }

protected:
    Graph& _g;
    EdgeIndexMap _edge_index;
    vector<edge_t>& _edges;
    rng_t& _rng;

    typedef gt_hash_map<size_t, size_t> nmapv_t;
    typedef typename property_map_type::apply<nmapv_t,
                                              typename property_map<Graph, vertex_index_t>::type>
        ::type::unchecked_t nmap_t;
    nmap_t _nmap;
    bool _configuration;
};

// this will rewire the edges so that the combined (in, out) degree distribution
// will be the same, but all the rest is random
template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg>
class RandomRewireStrategy:
    public RewireStrategyBase<Graph, EdgeIndexMap,
                              RandomRewireStrategy<Graph, EdgeIndexMap,
                                                   CorrProb, BlockDeg> >
{
public:
    typedef RewireStrategyBase<Graph, EdgeIndexMap,
                               RandomRewireStrategy<Graph, EdgeIndexMap,
                                                    CorrProb, BlockDeg> >
        base_t;

    typedef Graph graph_t;
    typedef EdgeIndexMap edge_index_t;

    typedef typename graph_traits<Graph>::vertex_descriptor vertex_t;
    typedef typename graph_traits<Graph>::edge_descriptor edge_t;
    typedef typename EdgeIndexMap::value_type index_t;

    struct hash_index {};
    struct random_index {};

    RandomRewireStrategy(Graph& g, EdgeIndexMap edge_index,
                         vector<edge_t>& edges, CorrProb, BlockDeg,
                         bool, rng_t& rng, bool parallel_edges,
                         bool configuration)
        : base_t(g, edge_index, edges, rng, parallel_edges, configuration),
          _g(g) {}

    pair<size_t,bool> get_target_edge(pair<size_t,bool>& e, bool)
    {
        std::uniform_int_distribution<> sample(0, base_t::_edges.size() - 1);
        pair<size_t, bool> et = make_pair(sample(base_t::_rng), false);
        if (!is_directed::apply<Graph>::type::value)
        {
            std::bernoulli_distribution coin(0.5);
            et.second = coin(base_t::_rng);
            e.second = coin(base_t::_rng);
        }
        return et;
    }

    void update_edge(size_t, bool) {}

private:
    Graph& _g;
    EdgeIndexMap _edge_index;
};


// this will rewire the edges so that the (in,out) degree distributions and the
// (in,out)->(in,out) correlations will be the same, but all the rest is random
template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg>
class CorrelatedRewireStrategy:
    public RewireStrategyBase<Graph, EdgeIndexMap,
                              CorrelatedRewireStrategy<Graph, EdgeIndexMap,
                                                       CorrProb, BlockDeg> >
{
public:
    typedef RewireStrategyBase<Graph, EdgeIndexMap,
                               CorrelatedRewireStrategy<Graph, EdgeIndexMap,
                                                        CorrProb, BlockDeg> >
        base_t;

    typedef Graph graph_t;

    typedef typename graph_traits<Graph>::vertex_descriptor vertex_t;
    typedef typename graph_traits<Graph>::edge_descriptor edge_t;

    typedef typename BlockDeg::block_t deg_t;

    CorrelatedRewireStrategy(Graph& g, EdgeIndexMap edge_index,
                             vector<edge_t>& edges, CorrProb, BlockDeg blockdeg,
                             bool, rng_t& rng, bool parallel_edges,
                             bool configuration)
        : base_t(g, edge_index, edges, rng, parallel_edges, configuration),
          _blockdeg(blockdeg), _g(g)
    {
        for (size_t ei = 0; ei < base_t::_edges.size(); ++ei)
        {
            // For undirected graphs, there is no difference between source and
            // target, and each edge will appear _twice_ in the list below,
            // once for each different ordering of source and target.
            edge_t& e = base_t::_edges[ei];

            vertex_t t = target(e, _g);
            deg_t tdeg = get_deg(t, _g);;
            _edges_by_target[tdeg].push_back(make_pair(ei, false));

            if (!is_directed::apply<Graph>::type::value)
            {
                t = source(e, _g);
                deg_t tdeg = get_deg(t, _g);
                _edges_by_target[tdeg].push_back(make_pair(ei, true));
            }
        }
    }

    pair<size_t,bool> get_target_edge(pair<size_t, bool>& e, bool)
    {
        if (!is_directed::apply<Graph>::type::value)
        {
            std::bernoulli_distribution coin(0.5);
            e.second = coin(base_t::_rng);
        }

        vertex_t t = target(e, base_t::_edges, _g);
        deg_t tdeg = get_deg(t, _g);
        auto& elist = _edges_by_target[tdeg];
        std::uniform_int_distribution<> sample(0, elist.size() - 1);
        auto ep = elist[sample(base_t::_rng)];
        if (get_deg(target(ep, base_t::_edges, _g), _g) != tdeg)
            ep.second = not ep.second;
        return ep;
    }

    void update_edge(size_t, bool) {}

    deg_t get_deg(vertex_t v, const Graph& g)
    {
        return _blockdeg.get_block(v, g);
    }

private:
    BlockDeg _blockdeg;

    typedef std::unordered_map<deg_t,
                          vector<pair<size_t, bool>>>
        edges_by_end_deg_t;

    edges_by_end_deg_t _edges_by_target;

protected:
    const Graph& _g;
};


// general stochastic blockmodel
// this version is based on rejection sampling
template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg>
class ProbabilisticRewireStrategy:
    public RewireStrategyBase<Graph, EdgeIndexMap,
                              ProbabilisticRewireStrategy<Graph, EdgeIndexMap,
                                                          CorrProb, BlockDeg> >
{
public:
    typedef RewireStrategyBase<Graph, EdgeIndexMap,
                               ProbabilisticRewireStrategy<Graph, EdgeIndexMap,
                                                           CorrProb, BlockDeg> >
        base_t;

    typedef Graph graph_t;
    typedef EdgeIndexMap edge_index_t;

    typedef typename BlockDeg::block_t deg_t;

    typedef typename graph_traits<Graph>::vertex_descriptor vertex_t;
    typedef typename graph_traits<Graph>::edge_descriptor edge_t;
    typedef typename EdgeIndexMap::value_type index_t;

    ProbabilisticRewireStrategy(Graph& g, EdgeIndexMap edge_index,
                                vector<edge_t>& edges, CorrProb corr_prob,
                                BlockDeg blockdeg, bool cache, rng_t& rng,
                                bool parallel_edges, bool configuration)
        : base_t(g, edge_index, edges, rng, parallel_edges, configuration),
          _g(g), _corr_prob(corr_prob), _blockdeg(blockdeg)
    {
        if (cache)
        {
            // cache probabilities
            _corr_prob.get_probs(_probs);

            if (_probs.empty())
            {
                std::unordered_set<deg_t> deg_set;
                for (size_t ei = 0; ei < base_t::_edges.size(); ++ei)
                {
                    edge_t& e = base_t::_edges[ei];
                    deg_set.insert(get_deg(source(e, g), g));
                    deg_set.insert(get_deg(target(e, g), g));
                }

                for (auto s_iter = deg_set.begin(); s_iter != deg_set.end(); ++s_iter)
                    for (auto t_iter = deg_set.begin(); t_iter != deg_set.end(); ++t_iter)
                    {
                        double p = _corr_prob(*s_iter, *t_iter);
                        _probs[make_pair(*s_iter, *t_iter)] = p;
                    }
            }

            for (auto iter = _probs.begin(); iter != _probs.end(); ++iter)
            {
                double& p = iter->second;
                // avoid zero probability to not get stuck in rejection step
                if (std::isnan(p) || std::isinf(p) || p <= 0)
                    p = numeric_limits<double>::min();
                p = log(p);
            }
        }
    }

    double get_prob(const deg_t& s_deg, const deg_t& t_deg)
    {
        if (_probs.empty())
        {
            double p = _corr_prob(s_deg, t_deg);
            // avoid zero probability to not get stuck in rejection step
            if (std::isnan(p) || std::isinf(p) || p <= 0)
                p = numeric_limits<double>::min();
            return log(p);
        }
        auto k = make_pair(s_deg, t_deg);
        auto iter = _probs.find(k);
        if (iter == _probs.end())
            return log(numeric_limits<double>::min());
        return iter->second;
    }

    deg_t get_deg(vertex_t v, Graph& g)
    {
        return _blockdeg.get_block(v, g);
    }

    pair<size_t, bool> get_target_edge(pair<size_t, bool>& e, bool)
    {
        if (!is_directed::apply<Graph>::type::value)
        {
            std::bernoulli_distribution coin(0.5);
            e.second = coin(base_t::_rng);
        }

        deg_t s_deg = get_deg(source(e, base_t::_edges, _g), _g);
        deg_t t_deg = get_deg(target(e, base_t::_edges, _g), _g);

        std::uniform_int_distribution<> sample(0, base_t::_edges.size() - 1);
        size_t epi = sample(base_t::_rng);
        pair<size_t, bool> ep = make_pair(epi, false);
        if (!is_directed::apply<Graph>::type::value)
        {
            // for undirected graphs we must select a random direction
            std::bernoulli_distribution coin(0.5);
            ep.second = coin(base_t::_rng);
        }

        if (source(e, base_t::_edges, _g) == source(ep, base_t::_edges, _g) ||
            target(e, base_t::_edges, _g) == target(ep, base_t::_edges, _g))
            return ep; // rewiring is a no-op

        deg_t ep_s_deg = get_deg(source(ep, base_t::_edges, _g), _g);
        deg_t ep_t_deg = get_deg(target(ep, base_t::_edges, _g), _g);

        double pi = get_prob(s_deg, t_deg) + get_prob(ep_s_deg, ep_t_deg);
        double pf = get_prob(s_deg, ep_t_deg) + get_prob(ep_s_deg, t_deg);

        if (pf >= pi)
            return ep;

        double a = exp(pf - pi);

        std::uniform_real_distribution<> rsample(0.0, 1.0);
        double r = rsample(base_t::_rng);
        if (r > a)
            return e; // reject
        else
            return ep;
    }

    void update_edge(size_t, bool) {}

private:
    Graph& _g;
    EdgeIndexMap _edge_index;
    CorrProb _corr_prob;
    BlockDeg _blockdeg;

    typedef std::unordered_map<pair<deg_t, deg_t>, double> prob_map_t;
    prob_map_t _probs;
};


// general "traditional" stochastic blockmodel
// this version is based on the alias method, and does not keep the degrees fixed
template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg,
          bool micro>
class TradBlockRewireStrategy
{
public:
    typedef typename graph_traits<Graph>::vertex_descriptor vertex_t;
    typedef typename graph_traits<Graph>::edge_descriptor edge_t;
    typedef typename EdgeIndexMap::value_type index_t;
    typedef typename BlockDeg::block_t deg_t;

    TradBlockRewireStrategy(Graph& g, EdgeIndexMap edge_index,
                            vector<edge_t>& edges, CorrProb corr_prob,
                            BlockDeg blockdeg, bool, rng_t& rng,
                            bool parallel_edges, bool configuration)

        : _g(g), _edge_index(edge_index), _edges(edges), _corr_prob(corr_prob),
          _blockdeg(blockdeg), _rng(rng), _sampler(nullptr),
          _configuration(configuration),
          _nmap(get(vertex_index, g), num_vertices(g))
    {
        for (auto v : vertices_range(_g))
        {
            deg_t d = _blockdeg.get_block(v, g);
            _vertices[d].push_back(v);
        }

        if (!micro)
        {
            std::unordered_map<pair<deg_t, deg_t>, double> probs;
            _corr_prob.get_probs(probs);

            vector<double> dprobs;
            if (probs.empty())
            {
                for (auto& s : _vertices)
                {
                    for (auto& t : _vertices)
                    {
                        double p = _corr_prob(s.first, t.first);
                        if (std::isnan(p) || std::isinf(p) || p <= 0)
                            continue;

                        _items.push_back(make_pair(s.first, t.first));
                        dprobs.push_back(p * s.second.size() * t.second.size());
                    }
                }
            }
            else
            {
                for (auto& stp : probs)
                {
                    deg_t s = stp.first.first;
                    deg_t t = stp.first.second;
                    double p = stp.second;
                    // avoid zero probability to not get stuck in rejection step
                    if (std::isnan(p) || std::isinf(p) || p <= 0)
                        continue;
                    _items.push_back(make_pair(s, t));
                    dprobs.push_back(p * _vertices[s].size() * _vertices[t].size());
                }
            }

            if (_items.empty())
                throw GraphException("No connection probabilities larger than zero!");

            _sampler = new Sampler<pair<deg_t, deg_t> >(_items, dprobs);
        }

        if (!configuration || !parallel_edges)
        {
            for (size_t i = 0; i < edges.size(); ++i)
                add_count(source(edges[i], g), target(edges[i], g), _nmap, g);
        }
    }

    ~TradBlockRewireStrategy()
    {
        if (_sampler != nullptr)
            delete _sampler;
    }

    bool operator()(size_t ei, bool self_loops, bool parallel_edges)
    {
        size_t e_s = source(_edges[ei], _g);
        size_t e_t = target(_edges[ei], _g);

        typename graph_traits<Graph>::vertex_descriptor s, t;

        pair<deg_t, deg_t> deg;
        if (micro)
            deg = {_blockdeg.get_block(e_s, _g),
                   _blockdeg.get_block(e_t, _g)};

        while (true)
        {
            if (!micro)
                deg = _sampler->sample(_rng);

            vector<vertex_t>& svs = _vertices[deg.first];
            vector<vertex_t>& tvs = _vertices[deg.second];

            if (svs.empty() || tvs.empty())
                continue;

            s = uniform_sample(svs, _rng);
            t = uniform_sample(tvs, _rng);

            if (!is_directed::apply<Graph>::type::value &&
                deg.first == deg.second && s != t && self_loops)
            {
                // sample self-loops w/ correct probability for undirected
                // graphs
                std::bernoulli_distribution reject(.5);
                if (reject(_rng))
                    continue;
            }

            break;
        }

        // reject self-loops if not allowed
        if (!self_loops && s == t)
            return false;

        // reject parallel edges if not allowed
        if (!parallel_edges && get_count(s, t, _nmap, _g))
            return false;

        if (!_configuration)
        {
            size_t m = get_count(s, t, _nmap, _g);
            size_t m_e = get_count(e_s, e_t, _nmap, _g);

            double a = (m + 1) / double(m_e);

            std::bernoulli_distribution accept(std::min(a, 1.));
            if (!accept(_rng))
                return false;
        }

        remove_edge(_edges[ei], _g);
        edge_t ne = add_edge(s, t, _g).first;
        _edges[ei] = ne;

        if (!_configuration || !parallel_edges)
        {
            remove_count(e_s, e_t, _nmap, _g);
            add_count(s, t, _nmap, _g);
        }

        return true;
    }

private:
    Graph& _g;
    EdgeIndexMap _edge_index;
    vector<edge_t>& _edges;
    CorrProb _corr_prob;
    BlockDeg _blockdeg;
    rng_t& _rng;

    std::unordered_map<deg_t, vector<vertex_t>> _vertices;

    vector<pair<deg_t, deg_t> > _items;
    Sampler<pair<deg_t, deg_t> >* _sampler;

    bool _configuration;

    typedef gt_hash_map<size_t, size_t> nmapv_t;
    typedef typename property_map_type::apply<nmapv_t,
                                              typename property_map<Graph, vertex_index_t>::type>
        ::type::unchecked_t nmap_t;
    nmap_t _nmap;
};

template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg>
using CanTradBlockRewireStrategy =
    TradBlockRewireStrategy<Graph, EdgeIndexMap, CorrProb, BlockDeg, false>;

template <class Graph, class EdgeIndexMap, class CorrProb, class BlockDeg>
using MicroTradBlockRewireStrategy =
    TradBlockRewireStrategy<Graph, EdgeIndexMap, CorrProb, BlockDeg, true>;

} // graph_tool namespace

#endif // GRAPH_REWIRING_HH
