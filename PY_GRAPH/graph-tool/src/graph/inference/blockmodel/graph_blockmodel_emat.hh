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

#ifndef GRAPH_BLOCKMODEL_EMAT_HH
#define GRAPH_BLOCKMODEL_EMAT_HH

#include <boost/multi_array.hpp>
#include "hash_map_wrap.hh"

namespace graph_tool
{

// this structure speeds up the access to the edges between given blocks, by
// using a simple adjacency matrix

template <class BGraph>
class EMat
{
public:
    template <class RNG>
    EMat(BGraph& bg, RNG&)
    {
        sync(bg);
    }

    void sync(BGraph& bg)
    {
        size_t B = num_vertices(bg);
        _mat.resize(boost::extents[B][B]);
        std::fill(_mat.data(), _mat.data() + _mat.num_elements(), _null_edge);

        for (auto e : edges_range(bg))
        {
            assert(get_me(source(e, bg),target(e, bg)) == _null_edge);
            _mat[source(e, bg)][target(e, bg)] = e;
            if (!is_directed::apply<BGraph>::type::value)
                _mat[target(e, bg)][source(e, bg)] = e;
        }
    }

    typedef typename graph_traits<BGraph>::vertex_descriptor vertex_t;
    typedef typename graph_traits<BGraph>::edge_descriptor edge_t;

    const auto& get_me(vertex_t r, vertex_t s) const
    {
        return _mat[r][s];
    }

    void put_me(vertex_t r, vertex_t s, const edge_t& e)
    {
        _mat[r][s] = e;
        if (!is_directed::apply<BGraph>::type::value && r != s)
            _mat[s][r] = e;
    }

    void remove_me(const edge_t& me, BGraph& bg)
    {
        auto r = source(me, bg);
        auto s = target(me, bg);
        _mat[r][s] = _null_edge;
        if (!is_directed::apply<BGraph>::type::value)
            _mat[s][r] = _null_edge;
        remove_edge(me, bg);
    }

    const auto& get_null_edge() const { return _null_edge; }

private:
    multi_array<edge_t, 2> _mat;
    static const edge_t _null_edge;
};

template <class BGraph>
const typename EMat<BGraph>::edge_t EMat<BGraph>::_null_edge;


template <class Key>
class perfect_hash_t
{
public:
    template <class RNG>
    perfect_hash_t(size_t N, std::vector<size_t>& index, RNG& rng)
        : _index(&index)
    {
        index.reserve(N);
        for (size_t i = 0; i < N; ++i)
            index.push_back(i);
        std::shuffle(index.begin(), index.end(), rng);
    }
    perfect_hash_t(std::vector<size_t>& index)
        : _index(&index) {}
    perfect_hash_t() {}
    size_t operator()(const Key& k) const { return (*_index)[k]; }
    void resize(size_t N)
    {
        auto& index = *_index;
        for (size_t i = index.size(); i < N; ++i)
            index.push_back(i);
    }
private:
    std::vector<size_t>* _index;
};

// this structure speeds up the access to the edges between given blocks, since
// we're using an adjacency list to store the block structure (this is like
// EMat above, but takes less space and is slower)

template <class BGraph>
class EHash
{
public:

    template <class RNG>
    EHash(BGraph& bg, RNG& rng)
        : _hash_function(num_vertices(bg), _index, rng),
          _hash(num_vertices(bg), ehash_t(0, _hash_function))
    {
        sync(bg);
    }

    EHash(const EHash& other)
        : _index(other._index),
          _hash_function(_index),
          _hash(other._hash.size(), ehash_t(0, _hash_function))
    {
        for (size_t r = 0; r < other._hash.size(); ++r)
        {
            auto& h = _hash[r];
            for (const auto& x : other._hash[r])
                h[x.first] = x.second;
        }
    }

    void sync(BGraph& bg)
    {
        _hash_function.resize(num_vertices(bg));
        _hash.clear();
        _hash.resize(num_vertices(bg), ehash_t(0, _hash_function));
        for (auto& h : _hash)
            h.max_load_factor(.3);

        for (auto e : edges_range(bg))
        {
            assert(get_me(source(e, bg), target(e, bg)) == _null_edge);
            put_me(source(e, bg), target(e, bg), e);
        }
    }

    typedef typename graph_traits<BGraph>::vertex_descriptor vertex_t;
    typedef typename graph_traits<BGraph>::edge_descriptor edge_t;

    __attribute__((flatten)) __attribute__((hot))
    const auto& get_me(vertex_t r, vertex_t s) const
    {
        if (!is_directed::apply<BGraph>::type::value && r > s)
            std::swap(r, s);
        auto& map = _hash[r];
        const auto& iter = map.find(s);
        if (iter == map.end())
            return _null_edge;
        return iter->second;
    }

    void put_me(vertex_t r, vertex_t s, const edge_t& e)
    {
        if (!is_directed::apply<BGraph>::type::value && r > s)
            std::swap(r, s);
        assert(r < _hash.size());
        _hash[r][s] = e;
    }

    void remove_me(const edge_t& me, BGraph& bg)
    {
        auto r = source(me, bg);
        auto s = target(me, bg);
        if (!is_directed::apply<BGraph>::type::value && r > s)
            std::swap(r, s);
        assert(r < _hash.size());
        _hash[r].erase(s);
        remove_edge(me, bg);
    }

    const auto& get_null_edge() const { return _null_edge; }

private:
    std::vector<size_t> _index;
    perfect_hash_t<vertex_t> _hash_function;
    typedef gt_hash_map<vertex_t, edge_t, perfect_hash_t<vertex_t>> ehash_t;
    std::vector<ehash_t> _hash;
    static const edge_t _null_edge;
};

template <class BGraph>
const typename EHash<BGraph>::edge_t EHash<BGraph>::_null_edge;

template <class Vertex, class Eprop, class Emat, class BEdge>
inline auto get_beprop(Vertex r, Vertex s, const Eprop& eprop, const Emat& emat,
                       BEdge& me)
{
    typedef typename property_traits<Eprop>::value_type val_t;
    me = emat.get_me(r, s);
    if (me != emat.get_null_edge())
        return eprop[me];
    return val_t();
}

template <class Vertex, class Eprop, class Emat>
inline auto get_beprop(Vertex r, Vertex s, const Eprop& eprop, const Emat& emat)
{
    typedef typename property_traits<Eprop>::key_type bedge_t;
    bedge_t me;
    return get_beprop(r, s, eprop, emat, me);
}

} // namespace graph_tool

#endif // GRAPH_BLOCKMODEL_EMAT_HH
