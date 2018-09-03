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

#ifndef GRAPH_BLOCKMODEL_LAYERS_HH
#define GRAPH_BLOCKMODEL_LAYERS_HH

#include "config.h"

#include <vector>

#include "../support/graph_state.hh"
#include "../blockmodel/graph_blockmodel_util.hh"
#include "graph_blockmodel_layers_util.hh"

namespace graph_tool
{
using namespace boost;
using namespace std;

typedef eprop_map_t<int32_t>::type emap_t;
typedef vprop_map_t<std::vector<int32_t>>::type vcvmap_t;

typedef gt_hash_map<size_t, size_t> bmap_t;
typedef std::vector<bmap_t> vbmap_t;

#define LAYERED_BLOCK_STATE_params                                             \
    ((__class__,&, mpl::vector<python::object>, 1))                            \
    ((layer_states,, python::object, 0))                                       \
    ((ec,, emap_t, 0))                                                         \
    ((vc,, vcvmap_t, 0))                                                       \
    ((vmap,, vcvmap_t, 0))                                                     \
    ((block_map, &, vbmap_t&, 0))                                              \
    ((master,, bool, 0))


class LayeredBlockStateVirtualBase
    : public BlockStateVirtualBase
{
public:
    virtual BlockStateVirtualBase& get_layer(size_t l) = 0;
    virtual size_t get_block(size_t l, size_t v) = 0;
    virtual void set_block(size_t l, size_t v, size_t r) = 0;
    virtual size_t get_vweight(size_t l, size_t v) = 0;
    virtual void add_layer_node(size_t l, size_t v, size_t u) = 0;
    virtual void remove_layer_node(size_t l, size_t v, size_t u) = 0;
    virtual size_t get_layer_node(size_t l, size_t v) = 0;
    virtual size_t get_block_map(size_t l, size_t r, bool put_new=true) = 0;
    virtual bool check_layers() = 0;
};

template <class BaseState>
struct Layers
{
    GEN_STATE_BASE(LayeredBlockStateBase, LAYERED_BLOCK_STATE_params)

    template <class... Ts>
    class LayeredBlockState
        : public LayeredBlockStateBase<Ts...>,
          public BaseState,
          public LayeredBlockStateVirtualBase
    {
    public:
        GET_PARAMS_USING(LayeredBlockStateBase<Ts...>,
                         LAYERED_BLOCK_STATE_params)
        GET_PARAMS_TYPEDEF(Ts, LAYERED_BLOCK_STATE_params)

        GET_PARAMS_USING(BaseState, BASE_STATE_params)
        using BaseState::_bg;
        using BaseState::_m_entries;
        using BaseState::_emat;
        using BaseState::_partition_stats;
        using BaseState::is_partition_stats_enabled;
        using BaseState::get_move_entries;

        typedef vprop_map_t<int32_t>::type block_rmap_t;

        class LayerState
            : public BaseState
        {
        public:
            LayerState(const BaseState& base_state, LayeredBlockState& lstate,
                       bmap_t& block_map, block_rmap_t block_rmap,
                       vector<size_t>& free_blocks, size_t l)
                : BaseState(base_state),
                  _lstate(&lstate),
                  _block_map(block_map),
                  _block_rmap(block_rmap),
                  _free_blocks(free_blocks),
                  _l(l), _E(0)
            {
                for (auto e : edges_range(BaseState::_g))
                    _E += BaseState::_eweight[e];
            }

            LayeredBlockState* _lstate;
            bmap_t& _block_map;
            block_rmap_t _block_rmap;
            vector<size_t>& _free_blocks;
            size_t _l;
            size_t _E;

            using BaseState::_bg;
            using BaseState::_wr;
            using BaseState::_bclabel;
            using BaseState::add_block;

            size_t get_block_map(size_t r, bool put_new=true)
            {
                size_t r_u;
                auto iter = _block_map.find(r);
                if (iter == _block_map.end())
                {
                    if (_free_blocks.empty())
                        _free_blocks.push_back(_block_map.size());
                    r_u = _free_blocks.back();
                    while (r_u >= num_vertices(_bg))
                        add_block();
                    assert(r_u < num_vertices(_bg));

                    if (put_new)
                    {
                        _block_map[r] = r_u;
                        _block_rmap[r_u] = r;
                        if (_lstate->_lcoupled_state != nullptr)
                        {
                            _lstate->_lcoupled_state->add_layer_node(_l, r, r_u);
                            _bclabel[r_u] =
                                _lstate->_lcoupled_state->get_block_map(_l, _lstate->_bclabel[r]);
                            assert(_lstate->_lcoupled_state->get_vweight(_l, r_u) == (_wr[r_u] > 0));
                            if (_wr[r_u] == 0)
                                _lstate->_lcoupled_state->set_block(_l, r_u, _bclabel[r_u]);
                            assert(_lstate->_lcoupled_state->get_block(_l, r_u) == size_t(_bclabel[r_u]));
                        }
                        _free_blocks.pop_back();
                        assert(_lstate->_lcoupled_state == nullptr ||
                               r_u == _lstate->_lcoupled_state->get_layer_node(_l, r));
                        assert(_lstate->_lcoupled_state == nullptr ||
                               size_t(_bclabel[r_u]) ==
                               _lstate->_lcoupled_state->
                               get_block_map(_l, _lstate->_bclabel[r], false));
                    }
                }
                else
                {
                    r_u = iter->second;
                    assert(size_t(_block_rmap[r_u]) == r);
                    assert(_lstate->_lcoupled_state == nullptr ||
                           r_u == _lstate->_lcoupled_state->get_layer_node(_l, r));
                }
                assert(r_u < num_vertices(_bg));
                return r_u;
            }

            bool has_block_map(size_t r)
            {
                return _block_map.find(r) != _block_map.end();
            }

        };

        template <class... ATs,
                  typename std::enable_if_t<sizeof...(ATs) == sizeof...(Ts)>* = nullptr>
        LayeredBlockState(const BaseState& base_state, ATs&&... args)
            : LayeredBlockStateBase<Ts...>(std::forward<ATs>(args)...),
              BaseState(base_state), _vc_c(_vc.get_checked()),
              _vmap_c(_vmap.get_checked())
        {
            for (int l = 0; l < python::len(_layer_states); ++l)
            {
                auto ostate = _layer_states[l];
                BaseState& state = python::extract<BaseState&>(ostate.attr("_state"));
                boost::python::object temp = ostate.attr("block_rmap").attr("_get_any")();
                boost::any& a = python::extract<boost::any&>(temp);
                block_rmap_t block_rmap = boost::any_cast<block_rmap_t>(a);
                std::vector<size_t>& free_blocks =
                    python::extract<std::vector<size_t>&>(ostate.attr("free_blocks"));
                bmap_t& block_map = _block_map[l];
                _layers.emplace_back(state, *this, block_map, block_rmap, free_blocks, l);
            }
            for (auto r : vertices_range(BaseState::_bg))
            {
                if (BaseState::_wr[r] > 0)
                    _actual_B++;
            }
            _N = BaseState::get_N();
            // assert(check_layers());
            // assert(check_edge_counts());
        }

        LayeredBlockState(const LayeredBlockState& other)
            : LayeredBlockStateBase<Ts...>(static_cast<const LayeredBlockStateBase<Ts...>&>(other)),
              BaseState(other),
              _layers(other._layers),
              _actual_B(other._actual_B),
              _N(other._N),
              _is_partition_stats_enabled(other._is_partition_stats_enabled),
              _lcoupled_state(other._lcoupled_state),
              _vc_c(_vc.get_checked()),
            _vmap_c(_vmap.get_checked())
        {
            for (auto& state : _layers)
                state._lstate = this;
        }

        std::vector<LayerState> _layers;
        size_t _actual_B = 0;
        size_t _N = 0;
        bool _is_partition_stats_enabled = false;
        LayeredBlockStateVirtualBase* _lcoupled_state = nullptr;
        typename vc_t::checked_t _vc_c;
        typename vmap_t::checked_t _vmap_c;
        openmp_mutex _llock;

        void move_vertex(size_t v, size_t s)
        {
            // assert(check_layers());

            if (BaseState::_vweight[v] == 0)
            {
                _b[v] = s;
                return;
            }

            size_t r = _b[v];

            if (r == s)
                return;

            if (_wr[s] == 0)
                _bclabel[s] = _bclabel[r];

            auto& ls = _vc[v];
            auto& vs = _vmap[v];
            for (size_t j = 0; j < ls.size(); ++j)
            {
                int l = ls[j];
                size_t u = vs[j];

                auto& state = _layers[l];

                if (state._vweight[u] == 0)
                    continue;

                assert(state.has_block_map(r));
                assert(size_t(state._b[u]) == state.get_block_map(r, false));
                assert(_lcoupled_state == nullptr ||
                       _lcoupled_state->get_vweight(l, state._b[u]) > 0);
                assert(state._wr[state._b[u]] > 0);
                size_t s_u = state.get_block_map(s);

                assert(size_t(state._b[u]) != s_u);

                state.move_vertex(u, s_u);

                assert(state._wr[s_u] > 0);
                assert(s_u == state.get_block_map(s, false));
            }

            // bottom update needs to be last, due to _coupled_state, and the
            // fact that the upper levels are affected by get_block_map()

            if (_wr[s] == 0)
                _actual_B++;

            BaseState::move_vertex(v, s);

            if (_wr[r] == 0)
                _actual_B--;

            if (_lcoupled_state != nullptr)
            {
                for (size_t j = 0; j < ls.size(); ++j)
                {
                    int l = ls[j];
                    size_t u = vs[j];
                    auto& state = _layers[l];

                    if (state._vweight[u] == 0)
                        continue;

                    size_t r_u = state._b[u];
                    assert(r_u == state.get_block_map(s));
                    assert(state._wr[r_u] > 0);

                    _lcoupled_state->get_layer(l).set_vertex_weight(r_u, 1);

                    r_u = state.get_block_map(r);
                    if (state._wr[r_u] == 0)
                        _lcoupled_state->get_layer(l).set_vertex_weight(r_u, 0);
                    assert(state._wr[r_u] == 0 || BaseState::_wr[r] != 0);
                }
            }

            // assert(check_layers());
        }

        template <class Vec>
        void move_vertices(Vec& v, Vec& nr)
        {
            for (size_t i = 0; i < std::min(v.size(), nr.size()); ++i)
                move_vertex(v[i], nr[i]);
        }

        void move_vertices(python::object ovs, python::object ors)
        {
            multi_array_ref<uint64_t, 1> vs = get_array<uint64_t, 1>(ovs);
            multi_array_ref<uint64_t, 1> rs = get_array<uint64_t, 1>(ors);
            if (vs.size() != rs.size())
                throw ValueException("vertex and group lists do not have the same size");
            move_vertices(vs, rs);
        }

        void remove_vertex(size_t v)
        {
            size_t r = _b[v];
            auto& ls = _vc[v];
            auto& vs = _vmap[v];
            for (size_t j = 0; j < ls.size(); ++j)
            {
                int l = ls[j];
                size_t u = vs[j];
                auto& state = _layers[l];
                state.remove_vertex(u);
            }
            BaseState::remove_vertex(v);
            if (_wr[r] == 0)
                _actual_B--;
        }

        template <class Vec>
        void remove_vertices(Vec& vs)
        {
            gt_hash_map<size_t, vector<size_t>> lvs;
            gt_hash_set<size_t> rs;
            for (auto v : vs)
            {
                for (auto l : _vc[v])
                    lvs[l].push_back(v);
                rs.insert(_b[v]);
            }
            for (auto& lv : lvs)
            {
                auto l = lv.first;
                auto& state = _layers[l];
                vector<size_t> us;
                gt_hash_map<size_t, size_t> rus;
                for (auto v : lv.second)
                {
                    auto u = _vmap[v][l];
                    us.push_back(u);
                    size_t r = _b[v];
                    size_t r_u = state._b[u];
                    rus[r] = r_u;
                }
                state.remove_vertices(us);

                // for (auto rr_u : rus)
                // {
                //     if (state._wr[rr_u.second] == 0)
                //         state.remove_block_map(rr_u.first);
                // }
            }
            BaseState::remove_vertices(vs);
            for (auto r : rs)
            {
                if (_wr[r] == 0)
                    _actual_B--;
            }
        }

        void remove_vertices(python::object ovs)
        {
            multi_array_ref<uint64_t, 1> vs = get_array<uint64_t, 1>(ovs);
            remove_vertices(vs);
        }

        void add_vertex(size_t v, size_t r)
        {
            auto& ls = _vc[v];
            auto& vs = _vmap[v];
            for (size_t j = 0; j < ls.size(); ++j)
            {
                int l = ls[j];
                size_t u = vs[j];
                auto& state = _layers[l];
                size_t r_u = state.get_block_map(r);
                state.add_vertex(u, r_u);
            }
            if (_wr[r] == 0)
                _actual_B++;
            BaseState::add_vertex(v, r);
        }

        template <class Vs, class Rs>
        void add_vertices(Vs& vs, Rs& rs)
        {
            if (vs.size() != rs.size())
                throw ValueException("vertex and group lists do not have the same size");

            gt_hash_map<size_t, vector<size_t>> lvs;
            gt_hash_map<size_t, size_t> vrs;
            for (size_t i = 0; i < vs.size(); ++i)
            {
                auto v = vs[i];
                vrs[v] = rs[i];
                for (auto l : _vc[v])
                    lvs[l].push_back(v);
            }

            for (auto& lv : lvs)
            {
                auto l = lv.first;
                auto& state = _layers[l];
                vector<size_t> us;
                vector<size_t> rus;
                for (auto v : lv.second)
                {
                    us.emplace_back(_vmap[v][l]);
                    rus.emplace_back(state.get_block_map(vrs[v]));
                }
                state.add_vertices(us, rus);
            }
            for (auto r : rs)
            {
                if (_wr[r] == 0)
                    _actual_B++;
            }
            BaseState::add_vertices(vs, rs);
        }

        void add_vertices(python::object ovs, python::object ors)
        {
            multi_array_ref<uint64_t, 1> vs = get_array<uint64_t, 1>(ovs);
            multi_array_ref<uint64_t, 1> rs = get_array<uint64_t, 1>(ors);
            add_vertices(vs, rs);
        }

        template <class VMap>
        void set_partition(VMap&& b)
        {
            for (auto v : vertices_range(_g))
                LayeredBlockState::move_vertex(v, b[v]);
        }

        void set_partition(boost::any& ab)
        {
            typename BaseState::b_t::checked_t& b
                = boost::any_cast<typename BaseState::b_t::checked_t&>(ab);
            set_partition(b.get_unchecked());
        }

        template <class MEntries>
        double virtual_move(size_t v, size_t r, size_t s, entropy_args_t ea,
                            MEntries& m_entries)
        {
            if (s == r)
                return 0;
            // assert(check_layers());

            double dS = 0;

            entropy_args_t mea(ea);
            mea.edges_dl = false;
            mea.recs = false;

            if (!_master)
            {
                mea.adjacency = false;
                mea.degree_dl = false;
            }

            dS += BaseState::virtual_move(v, r, s, mea, m_entries);

            if (_master)
            {
                dS -= virtual_move_covariate(v, r, s, *this, m_entries, false);

                if (ea.edges_dl)
                    dS += get_delta_edges_dl(v, r, s);
            }

            // assert(check_layers());

            if (ea.adjacency || ea.recs || ea.edges_dl)
            {
                scoped_lock lck(_llock);

                entropy_args_t lea(ea);
                lea.partition_dl = false;

                if (_master)
                {
                    lea.adjacency = false;
                    lea.degree_dl = false;
                    lea.edges_dl = false;
                }

                auto& ls = _vc[v];
                auto& vs = _vmap[v];
                for (size_t j = 0; j < ls.size(); ++j)
                {
                    size_t l = ls[j];
                    size_t u = vs[j];

                    auto& state = _layers[l];

                    if (state._vweight[u] == 0)
                        continue;

                    size_t s_u = (s != null_group) ?
                        state.get_block_map(s, false) : null_group;
                    size_t r_u = (r != null_group) ?
                        state._b[u] : null_group;

                    assert(r == null_group || state.has_block_map(r));
                    assert(r == null_group || r_u == state.get_block_map(r, false));

                    if (_master && ea.adjacency)
                        dS += virtual_move_covariate(u, r_u, s_u, state,
                                                     m_entries, true);
                    dS += state.virtual_move(u, r_u, s_u, lea, m_entries);
                }
            }

            if (BaseState::_coupled_state != nullptr)
            {
                bool r_vacate = (r != null_group) && (BaseState::virtual_remove_size(v) == 0);
                bool nr_occupy = (s != null_group) && (_wr[s] == 0);

                int L = _layers.size();
                dS -= _actual_B * (L * std::log(2) + std::log1p(-std::pow(2., -L)));
                size_t B = _actual_B;
                if (r_vacate)
                    B--;
                if (nr_occupy)
                    B++;
                dS += B * (L * std::log(2) + std::log1p(-std::pow(2., -L)));
            }
            // assert(check_layers());

            return dS;
        }

        double virtual_move(size_t v, size_t r, size_t s, entropy_args_t ea)
        {
            return virtual_move(v, r, s, ea, _m_entries);
        }

        template <class MEntries>
        double get_move_prob(size_t v, size_t r, size_t s, double c, double d,
                             bool reverse, MEntries& m_entries)
        {
            // m_entries may include entries from different levels
            if (!reverse)
                BaseState::get_move_entries(v, r, s, m_entries);
            return BaseState::get_move_prob(v, r, s, c, d, reverse, m_entries);
        }

        double get_move_prob(size_t v, size_t r, size_t s, double c, double d,
                             bool reverse)
        {
            return BaseState::get_move_prob(v, r, s, c, d, reverse);
        }

        void merge_vertices(size_t u, size_t v)
        {
            if (u == v)
                return;

            assert(BaseState::_vweight[v] > 0);
            assert(BaseState::_vweight[u] > 0);

            std::set<size_t> ls;
            gt_hash_map<size_t, size_t> ls_u, ls_v;
            for (size_t i = 0; i < _vc[u].size(); ++i)
            {
                size_t l = _vc[u][i];
                ls_u[l] = _vmap[u][i];
                ls.insert(l);
            }

            for (size_t i = 0; i < _vc[v].size(); ++i)
            {
                size_t l = _vc[v][i];
                ls_v[l] = _vmap[v][i];
                ls.insert(l);
            }

            _vc[u].clear();
            _vmap[u].clear();
            _vc[v].clear();
            _vmap[v].clear();

            for (auto l : ls)
            {
                auto iter_u = ls_u.find(l);
                auto iter_v = ls_v.find(l);

                size_t uu = (iter_u != ls_u.end()) ? iter_u->second : iter_v->second;
                size_t vv = (iter_v != ls_v.end()) ? iter_v->second : iter_u->second;

                auto& state = _layers[l];
                assert(state._vweight[vv] > 0);
                assert(state._vweight[uu] > 0);

                state.merge_vertices(uu, vv);

                assert(state._b[uu] == state._b[vv]);
                assert(size_t(state._b[vv]) == state.get_block_map(_b[v], false));

                assert(state._vweight[uu] > 0 || total_degreeS()(uu, state._g, state._eweight) == 0);
                assert(state._vweight[vv] > 0 || total_degreeS()(vv, state._g, state._eweight) == 0);

                _vc[v].push_back(l);
                _vmap[v].push_back(vv);
            }

            BaseState::merge_vertices(u, v, _ec.get_checked());

            // assert(check_layers());
            // assert(check_edge_counts());
        }

        double entropy(bool dense, bool multigraph, bool deg_entropy,
                       bool exact, bool recs, bool recs_dl, bool adjacency)
        {
            double S = 0;
            if (_master)
            {
                S += BaseState::entropy(dense, multigraph, deg_entropy, exact,
                                        false, false, adjacency);
                if (adjacency)
                {
                    S -= covariate_entropy(_bg, _mrs);
                    if (multigraph)
                        S -= BaseState::get_parallel_entropy();
                    for (auto& state : _layers)
                    {
                        S += covariate_entropy(state._bg, state._mrs);
                        if (multigraph)
                            S += state.get_parallel_entropy();
                    }
                }

                if (recs)
                {
                    for (auto& state : _layers)
                        S += state.entropy(false, false, false, false,
                                           true, recs_dl, false);
                }
            }
            else
            {
                for (auto& state : _layers)
                    S += state.entropy(dense, multigraph, deg_entropy, exact,
                                       recs, recs_dl, adjacency);
                int L = _layers.size();
                S += _N * (L * std::log(2) + std::log1p(-std::pow(2., -L)));
            }
            return S;
        }

        double get_delta_edges_dl(size_t v, size_t r, size_t s)
        {
            if (r == s || BaseState::_allow_empty)
                return 0;
            if (BaseState::_vweight[v] == 0)
                return 0;
            int dB = 0;
            if (r != null_group && BaseState::virtual_remove_size(v) == 0)
                --dB;
            if (s != null_group && _wr[s] == 0)
                ++dB;
            double S_a = 0, S_b = 0;
            if (dB != 0)
            {
                auto get_x = [](size_t B)
                    {
                        if (is_directed::apply<typename BaseState::g_t>::type::value)
                            return B * B;
                        else
                            return (B * (B + 1)) / 2;
                    };

                for (auto& state : _layers)
                {
                    S_b += lbinom(get_x(_actual_B) + state._E - 1, state._E);
                    S_a += lbinom(get_x(_actual_B + dB) + state._E - 1, state._E);
                }
            }
            return S_a - S_b;
        }

        double get_deg_dl(int kind)
        {
            if (_master)
            {
                return BaseState::get_deg_dl(kind);
            }
            else
            {
                double S = 0;
                for (auto& state : _layers)
                    S += state.get_deg_dl(kind);
                return S;
            }
        }

        void enable_partition_stats()
        {
            if (!_is_partition_stats_enabled)
            {
                BaseState::enable_partition_stats();
                for (auto& state : _layers)
                    state.enable_partition_stats();
                _is_partition_stats_enabled = true;
            }
        }

        void disable_partition_stats()
        {
            BaseState::disable_partition_stats();
            for (auto& state : _layers)
                state.disable_partition_stats();
            _is_partition_stats_enabled = false;
        }

        void init_mcmc(double c, double dl)
        {
            BaseState::init_mcmc(c, dl);
            for (auto& state : _layers)
                state.init_mcmc(numeric_limits<double>::infinity(), dl);
        }

        LayerState& get_layer(size_t l)
        {
            assert(l < _layers.size());
            return _layers[l];
        }

        size_t get_block(size_t l, size_t v)
        {
            return _layers[l]._b[v];
        }

        void set_block(size_t l, size_t v, size_t r)
        {
            _layers[l]._b[v] = r;
        }

        size_t get_vweight(size_t l, size_t v)
        {
            return _layers[l]._vweight[v];
        }

        void couple_state(LayeredBlockStateVirtualBase& s,
                          entropy_args_t ea)
        {
            _lcoupled_state = &s;

            entropy_args_t lea(ea);
            lea.edges_dl = false;
            lea.partition_dl = false;
            for (size_t l = 0; l < _layers.size(); ++l)
                _layers[l].couple_state(s.get_layer(l), lea);

            lea.partition_dl = true;
            lea.adjacency = false;
            lea.recs = false;
            lea.degree_dl = false;

            BaseState::couple_state(s, lea);

            // assert(check_layers());
        }

        void decouple_state()
        {
            BaseState::decouple_state();
            _lcoupled_state = nullptr;
            for (auto& state : _layers)
                state.decouple_state();
        }

        void couple_state(BlockStateVirtualBase& s,
                          entropy_args_t ea)
        {
            BaseState::couple_state(s, ea);
        }

        void add_partition_node(size_t v, size_t r)
        {
            if (_wr[r] == 0)
                _actual_B++;
            BaseState::add_partition_node(v, r);
        }

        void remove_partition_node(size_t v, size_t r)
        {
            BaseState::remove_partition_node(v, r);
            if (_wr[r] == 0)
                _actual_B--;
        }

        size_t get_layer_node(size_t l, size_t v)
        {
            auto& ls = _vc[v];
            auto& vs = _vmap[v];

            auto pos = std::lower_bound(ls.begin(), ls.end(), l);

            if (pos == ls.end() || size_t(*pos) != l)
                return null_group;

            return *(vs.begin() + (pos - ls.begin()));
        }

        void add_layer_node(size_t l, size_t v, size_t u)
        {
            auto& ls = _vc_c[v];
            auto& vs = _vmap_c[v];

            auto pos = std::lower_bound(ls.begin(), ls.end(), l);
            assert(pos == ls.end() || size_t(*pos) != l);

            vs.insert(vs.begin() + (pos - ls.begin()), u);
            ls.insert(pos, l);

            auto& state = _layers[l];
            state.set_vertex_weight(u, 0);
        }

        void remove_layer_node(size_t l, size_t v, size_t)
        {
            auto& ls = _vc[v];
            auto& vs = _vmap[v];

            auto pos = std::lower_bound(ls.begin(), ls.end(), l);

            assert(pos != ls.end());
            assert(size_t(*pos) == l);
            //assert(u == size_t(*(vs.begin() + (pos - ls.begin()))));

            vs.erase(vs.begin() + (pos - ls.begin()));
            ls.erase(pos);
        }

        size_t get_block_map(size_t l, size_t r, bool put_new=true)
        {
            return _layers[l].get_block_map(r, put_new);
        }

        void set_vertex_weight(size_t v, int w)
        {
            if (w == 0 && BaseState::_vweight[v] > 0)
                _N--;
            if (w == 1 && BaseState::_vweight[v] == 0)
                _N++;
            BaseState::set_vertex_weight(v, w);
        }

        size_t add_block()
        {
            auto r = BaseState::add_block();
            for (size_t l = 0; l < _layers.size(); ++l)
            {
                auto& state = _layers[l];
                size_t r_u = state.add_block();
                if (_lcoupled_state != nullptr)
                    _lcoupled_state->get_layer(l).coupled_resize_vertex(r_u);
            }
            return r;
        }

        void coupled_resize_vertex(size_t v)
        {
            BaseState::coupled_resize_vertex(v);
            auto& ls = _vc_c[v];
            auto& vs = _vmap_c[v];
            for (size_t j = 0; j < ls.size(); ++j)
            {
                int l = ls[j];
                size_t u = vs[j];
                auto& state = _layers[l];
                state.coupled_resize_vertex(u);
            }
        }

        void add_edge(const GraphInterface::edge_t& e)
        {
            BaseState::add_edge(e);
        }

        void remove_edge(const GraphInterface::edge_t& e)
        {
            BaseState::remove_edge(e);
        }

        void update_edge(const GraphInterface::edge_t& e,
                         const std::vector<double>& delta)
        {
            BaseState::update_edge(e, delta);
        }

        double recs_dS(size_t, size_t,
                       const std::vector<std::tuple<size_t, size_t,
                                                    GraphInterface::edge_t, int,
                                                    std::vector<double>>>&,
                       std::vector<double>&, int)
        {
            return 0;
        }

        void clear_egroups()
        {
            BaseState::clear_egroups();
        }

        void rebuild_neighbor_sampler()
        {
            BaseState::rebuild_neighbor_sampler();
        }

        void sync_emat()
        {
            BaseState::sync_emat();
            for (auto& state : _layers)
                state.sync_emat();
        }

        void sync_bclabel()
        {
            if (_lcoupled_state == nullptr)
                return;
            for (size_t l = 0; l < _layers.size(); ++ l)
            {
                auto& state = _layers[l];
                for (auto r_u : vertices_range(state._bg))
                {
                    if (state._wr[r_u] == 0)
                        continue;
                    state._bclabel[r_u] = _lcoupled_state->get_block(l, r_u);
                    assert(size_t(state._bclabel[r_u]) ==
                           _lcoupled_state->
                           get_block_map(l, _bclabel[state._block_rmap[r_u]], false));
                    assert(r_u == _lcoupled_state->get_layer_node(l, state._block_rmap[r_u]));
                }
            }
        }

        bool check_edge_counts(bool emat = true)
        {
            if (!BaseState::check_edge_counts(emat))
                return false;
            for (auto& state : _layers)
                if (!state.check_edge_counts(emat))
                    return false;
            return true;
        }

        bool check_layers()
        {
            scoped_lock lck(_llock);
            for (auto v : vertices_range(_g))
            {
                auto r = _b[v];
                auto& ls = _vc[v];
                auto& vs = _vmap[v];

                for (size_t j = 0; j < ls.size(); ++j)
                {
                    size_t l = ls[j];
                    size_t u = vs[j];

                    auto& state = _layers[l];

                    assert(state._vweight[u] > 0 || total_degreeS()(u, state._g, state._eweight) == 0);

                    if (state._vweight[u] == 0)
                        continue;

                    assert(BaseState::_vweight[v] > 0);

                    size_t r_u = state._b[u];
                    assert(r == state._block_rmap[r_u]);
                    if (r != state._block_rmap[r_u])
                        return false;

                    // bool found = false;
                    // for (auto e : out_edges_range(v, _g))
                    // {
                    //     if (_ec[e] == l && BaseState::_eweight[e] > 0)
                    //         found = true;
                    // }
                    // assert(found);
                }

                // for (auto e: out_edges_range(v, _g))
                // {
                //     if (BaseState::_eweight[e] == 0)
                //         continue;
                //     auto l = _ec[e];
                //     auto iter = std::find(ls.begin(), ls.end(), l);
                //     assert(iter != ls.end());
                // }
            }

            if (_lcoupled_state == nullptr)
                return true;
            for (auto v : vertices_range(_g))
            {
                if (BaseState::_vweight[v] == 0)
                    continue;
                auto r = _b[v];
                auto& ls = _vc[v];
                auto& vs = _vmap[v];
                for (size_t j = 0; j < ls.size(); ++j)
                {
                    size_t l = ls[j];
                    size_t u = vs[j];

                    auto& state = _layers[l];

                    if (state._vweight[u] == 0)
                        continue;
                    size_t r_u = state._b[u];
                    assert(r == state._block_rmap[r_u]);
                    if (r != state._block_rmap[r_u])
                        return false;
                    assert(r_u == state.get_block_map(r, false));
                    if (r_u != state.get_block_map(r, false))
                        return false;
                    assert(r_u == _lcoupled_state->get_layer_node(l, r));
                    if (r_u != _lcoupled_state->get_layer_node(l, r))
                        return false;
                    assert(_lcoupled_state->get_vweight(l, r_u) == (state._wr[r_u] > 0));
                    if (_lcoupled_state->get_vweight(l, r_u) != (state._wr[r_u] > 0))
                        return false;
                }
            }

            for (size_t l = 0; l < _layers.size(); ++l)
            {
                auto& state = _layers[l];
                for (auto r_u : vertices_range(state._bg))
                {
                    assert(_lcoupled_state->get_vweight(l, r_u) == (state._wr[r_u] > 0));
                    if (state._wr[r_u] == 0)
                        continue;
                    auto r = state._block_rmap[r_u];
                    assert(r_u == state.get_block_map(r, false));
                    if (r_u != state.get_block_map(r, false))
                        return false;
                    assert(r_u == _lcoupled_state->get_layer_node(l, r));
                    if (r_u != _lcoupled_state->get_layer_node(l, r))
                        return false;
                }
            }
            return _lcoupled_state->check_layers();
        }
    };
};

} // graph_tool namespace

#endif //GRAPH_BLOCKMODEL_LAYERS_HH
