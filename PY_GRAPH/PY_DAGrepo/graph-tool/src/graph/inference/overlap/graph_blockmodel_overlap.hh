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

#ifndef GRAPH_BLOCKMODEL_OVERLAP_HH
#define GRAPH_BLOCKMODEL_OVERLAP_HH

#include "config.h"
#include <tuple>

#include "../support/graph_state.hh"
#include "../blockmodel/graph_blockmodel_util.hh"
#include "graph_blockmodel_overlap_util.hh"

namespace graph_tool
{

using namespace boost;
using namespace std;

typedef vprop_map_t<int32_t>::type vmap_t;
typedef eprop_map_t<int32_t>::type emap_t;

typedef vprop_map_t<int64_t>::type vimap_t;
typedef vprop_map_t<vector<int64_t>>::type vvmap_t;

typedef mpl::vector2<std::true_type, std::false_type> use_hash_tr;

#define OVERLAP_BLOCK_STATE_params                                             \
    ((g, &, never_filtered_never_reversed, 1))                                 \
    ((use_hash,, use_hash_tr, 1))                                              \
    ((_abg, &, boost::any&, 0))                                                \
    ((node_index,, vimap_t, 0))                                                \
    ((half_edges,, vvmap_t, 0))                                                \
    ((mrs,, emap_t, 0))                                                        \
    ((mrp,, vmap_t, 0))                                                        \
    ((mrm,, vmap_t, 0))                                                        \
    ((wr,, vmap_t, 0))                                                         \
    ((b,, vmap_t, 0))                                                          \
    ((candidate_blocks, &, std::vector<size_t>&, 0))                           \
    ((bclabel,, vmap_t, 0))                                                    \
    ((pclabel,, vmap_t, 0))                                                    \
    ((deg_corr,, bool, 0))                                                     \
    ((rec_types,, std::vector<int>, 0))                                        \
    ((rec,, std::vector<eprop_map_t<double>::type>, 0))                        \
    ((drec,, std::vector<eprop_map_t<double>::type>, 0))                       \
    ((brec,, std::vector<eprop_map_t<double>::type>, 0))                       \
    ((bdrec,, std::vector<eprop_map_t<double>::type>, 0))                      \
    ((brecsum,, vprop_map_t<double>::type, 0))                                 \
    ((wparams,, std::vector<std::vector<double>>, 0))                          \
    ((recdx, &, std::vector<double>&, 0))                                      \
    ((Lrecdx, &, std::vector<double>&, 0))                                     \
    ((epsilon, &, std::vector<double>&, 0))                                    \
    ((allow_empty,, bool, 0))

GEN_STATE_BASE(OverlapBlockStateVirtualBase, OVERLAP_BLOCK_STATE_params)

template <class... Ts>
class OverlapBlockState
    : public OverlapBlockStateVirtualBase<Ts...>,
      public BlockStateVirtualBase
{
public:
    GET_PARAMS_USING(OverlapBlockStateVirtualBase<Ts...>, OVERLAP_BLOCK_STATE_params)
    GET_PARAMS_TYPEDEF(Ts, OVERLAP_BLOCK_STATE_params)

    template <class RNG, class... ATs,
              typename std::enable_if_t<sizeof...(ATs) == sizeof...(Ts)>* = nullptr>
    OverlapBlockState(RNG& rng, ATs&&... args)
        : OverlapBlockStateVirtualBase<Ts...>(std::forward<ATs>(args)...),
          _bg(boost::any_cast<std::reference_wrapper<bg_t>>(__abg)),
          _c_mrs(_mrs.get_checked()),
          _emat(_bg, rng),
          _egroups_enabled(true),
          _overlap_stats(_g, _b, _half_edges, _node_index, num_vertices(_bg)),
          _coupled_state(nullptr)
    {
        for (auto r : vertices_range(_bg))
            _wr[r] = _overlap_stats.get_block_size(r);
        for (auto& p : _brec)
        {
            _c_brec.push_back(p.get_checked());
            double x = 0;
            for (auto me : edges_range(_bg))
                x += p[me];
            _recsum.push_back(x);
        }
        for (auto& p : _bdrec)
            _c_bdrec.push_back(p.get_checked());
        if (!_rec_types.empty())
        {
            _recx2.resize(this->_rec_types.size());
            _recdx.resize(this->_rec_types.size());
            for (auto me : edges_range(_bg))
            {
                if (_brec[0][me] > 0)
                {
                    _B_E++;
                    for (size_t i = 0; i < _rec_types.size(); ++i)
                    {
                        if (this->_rec_types[i] == weight_type::REAL_NORMAL)
                        {
                            _recx2[i] += std::pow(_brec[i][me], 2);
                            if (_brec[0][me] > 1)
                                _recdx[i] += \
                                    (_bdrec[i][me] -
                                     std::pow(_brec[i][me], 2) / _brec[0][me]);
                        }
                    }
                }
                if (_brec[0][me] > 1)
                    _B_E_D++;
            }
        }

        _rt = weight_type::NONE;
        for (auto rt : _rec_types)
        {
            _rt = rt;
            if (rt == weight_type::REAL_NORMAL)
                break;
        }
        _dBdx.resize(_rec_types.size());
    }

    OverlapBlockState(const OverlapBlockState& other)
        : OverlapBlockStateVirtualBase<Ts...>
             (static_cast<const OverlapBlockStateVirtualBase<Ts...>&>(other)),
          _bg(other._bg),
          _c_mrs(other._c_mrs),
          _c_brec(other._c_brec),
          _c_bdrec(other._c_bdrec),
          _recsum(other._recsum),
          _recx2(other._recx2),
          _dBdx(other._dBdx),
          _B_E(other._B_E),
          _B_E_D(other._B_E_D),
          _rt(other._rt),
          _emat(other._emat),
          _egroups_enabled(other._egroups_enabled),
          _overlap_stats(other._overlap_stats),
          _coupled_state(nullptr)
    {
        if (other.is_partition_stats_enabled())
            enable_partition_stats();
    }

    template <bool Add, class MOP, class EOP>
    void modify_vertex(size_t v, size_t r, MOP&& mop, EOP&& eop)
    {
        auto u = _overlap_stats.get_out_neighbor(v);
        if (u != _overlap_stats._null)
        {
            size_t s = (Add) ? r : _b[u];

            if (Add && u != v)
                s = _b[u];

            auto me = _emat.get_me(r, s);

            if (Add && me == _emat.get_null_edge())
            {
                me = boost::add_edge(r, s, _bg).first;
                _emat.put_me(r, s, me);
                _c_mrs[me] = 0;
                for (size_t i = 0; i < _rec_types.size(); ++i)
                {
                    _c_brec[i][me] = 0;
                    _c_bdrec[i][me] = 0;
                }
            }

            auto e = *out_edges(v, _g).first;
            mop(e, me);

            if (Add)
            {
                _mrs[me] += 1;
                _mrp[r] += 1;
                _mrm[s] += 1;
            }
            else
            {
                _mrs[me] -= 1;
                _mrp[r] -= 1;
                _mrm[s] -= 1;
            }

            eop(e, me);

            assert(_mrs[me] >= 0);
            // if (_mrs[me] == 0)
            //     _emat.remove_me(me, _bg);
        }

        u = _overlap_stats.get_in_neighbor(v);
        if (u != _overlap_stats._null)
        {
            size_t s = (Add) ? r : _b[u];

            if (Add && u != v)
                s = _b[u];

            auto me = _emat.get_me(s, r);

            if (Add && me == _emat.get_null_edge())
            {
                me = boost::add_edge(s, r, _bg).first;
                _emat.put_me(s, r, me);
                _c_mrs[me] = 0;
                for (size_t i = 0; i < _rec_types.size(); ++i)
                {
                    _c_brec[i][me] = 0;
                    _c_bdrec[i][me] = 0;
                }
            }

            auto e = *in_edge_iteratorS<g_t>().get_edges(v, _g).first;
            mop(e, me);

            if (Add)
            {
                _mrs[me] += 1;
                _mrp[s] += 1;
                _mrm[r] += 1;
            }
            else
            {
                _mrs[me] -= 1;
                _mrp[s] -= 1;
                _mrm[r] -= 1;
            }

            eop(e, me);

            // if (_mrs[me] == 0)
            //     _emat.remove_me(me, _bg);
        }

        if (Add)
        {
            _overlap_stats.add_half_edge(v, r, _b, _g);
            _b[v] = r;
            if (!_egroups.empty() && _egroups_enabled)
                _egroups.add_vertex(v, _b, _eweight, _g);
        }
        else
        {
            _overlap_stats.remove_half_edge(v, r, _b, _g);
            if (!_egroups.empty() && _egroups_enabled)
                _egroups.remove_vertex(v, _b, _g);
        }
        _wr[r] = _overlap_stats.get_block_size(r);
     }

    template <bool Add>
    void modify_vertex(size_t v, size_t r)
    {
        if (_rec_types.empty())
        {
            modify_vertex<Add>(v, r,
                               [&](auto&, auto&){},
                               [&](auto&, auto&){});
        }
        else
        {
            int one = (Add) ? 1 : -1;
            auto end_op = [&](auto& e, auto& me)
                {
                    for (size_t i = 0; i < this->_rec_types.size(); ++i)
                       {
                           switch (this->_rec_types[i])
                           {
                           case weight_type::REAL_NORMAL: // signed weights
                               this->_bdrec[i][me] += one * this->_drec[i][e];
                               [[gnu::fallthrough]];
                           default:
                               this->_brec[i][me] += one * this->_rec[i][e];
                           }
                       }
                };

            auto mid_op_BE =
                [&](auto& e, auto& me)
                {
                    auto& mrs = this->_brec[0][me];
                    if (Add && mrs == 0 && mrs + one * this->_rec[0][e] > 0)
                    {
                        _B_E++;
                        if (_coupled_state != nullptr)
                            _coupled_state->add_edge(me);
                    }

                    if (!Add && mrs > 0 && mrs + one * this->_rec[0][e] == 0)
                    {
                        _B_E--;
                        if (_coupled_state != nullptr)
                            _coupled_state->remove_edge(me);
                    }
                };

            if (_rt != weight_type::REAL_NORMAL)
            {
                modify_vertex<Add>(v, r, mid_op_BE, end_op);
            }
            else
            {
                for (size_t i = 0; i < this->_rec_types.size(); ++i)
                    _dBdx[i] = 0;

                auto mid_op =
                    [&](auto& e, auto& me)
                    {
                        auto& mrs = this->_brec[0][me];
                        mid_op_BE(e, me);

                        if (mrs + one * this->_rec[0][e] > 1)
                        {
                            for (size_t i = 0; i < this->_rec_types.size(); ++i)
                            {
                                if (this->_rec_types[i] == weight_type::REAL_NORMAL)
                                {
                                    auto dx = \
                                        (this->_bdrec[i][me] + one * this->_drec[i][e]
                                         - (std::pow((this->_brec[i][me] +
                                                      one * this->_rec[i][e]), 2) /
                                            (mrs + one * this->_rec[0][e])));
                                    _recdx[i] += dx;
                                    _dBdx[i] += dx;
                                }
                            }

                            if (Add && (mrs < 2))
                            {
                                if (_B_E_D == 0 && this->_Lrecdx[0] >= 0)
                                    this->_Lrecdx[0] += 1;
                                _B_E_D++;
                            }
                        }

                        if (mrs > 1)
                        {
                            for (size_t i = 0; i < this->_rec_types.size(); ++i)
                            {
                                if (this->_rec_types[i] == weight_type::REAL_NORMAL)
                                {
                                    auto dx = \
                                       (this->_bdrec[i][me] -
                                        std::pow(this->_brec[i][me], 2) / mrs);
                                    _recdx[i] -= dx;
                                }
                            }

                            if (!Add && ((mrs + one * this->_rec[0][e]) < 2))
                            {
                                _B_E_D--;
                                if (_B_E_D == 0 && this->_Lrecdx[0] >= 0)
                                    this->_Lrecdx[0] -= 1;
                            }
                        }

                        for (size_t i = 0; i < this->_rec_types.size(); ++i)
                        {
                            if (this->_rec_types[i] == weight_type::REAL_NORMAL)
                            {
                                _recx2[i] -= std::pow(this->_brec[i][me], 2);
                                _recx2[i] += std::pow(this->_brec[i][me] +
                                                      one * this->_rec[i][e], 2);
                            }
                        }

                    };

                auto coupled_end_op = [&](auto& e, auto& me)
                    {
                        end_op(e, me);
                        if (_coupled_state != nullptr)
                        {
                            _rdelta.clear();
                            for (size_t i = 0; i < this->_rec_types.size(); ++i)
                                _rdelta.push_back(one * this->_rec[i][e]);
                            _coupled_state->update_edge(me, _rdelta);
                        }
                    };

                if (_Lrecdx[0] >= 0)
                {
                    for (size_t i = 0; i < _rec_types.size(); ++i)
                        _Lrecdx[i+1] -= _recdx[i] * _B_E_D;
                }

                modify_vertex<Add>(v, r, mid_op, coupled_end_op);

                if (_Lrecdx[0] >= 0)
                {
                    for (size_t i = 0; i < _rec_types.size(); ++i)
                        _Lrecdx[i+1] += _recdx[i] * _B_E_D;
                }
            }
        }
    }

    size_t get_B_E()
    {
        return _B_E;
    }

    size_t get_B_E_D()
    {
        return _B_E_D;
    }

    void remove_vertex(size_t v)
    {
        modify_vertex<false>(v, _b[v]);
    }

    void add_vertex(size_t v, size_t r)
    {
        modify_vertex<true>(v, r);
    }

    bool allow_move(size_t r, size_t nr)
    {
        return (_bclabel[r] == _bclabel[nr]);
    }

    // move a vertex from its current block to block nr
    void move_vertex(size_t v, size_t nr)
    {
        size_t r = _b[v];

        if (r == nr)
            return;

        if (!allow_move(r, nr))
            throw ValueException("cannot move vertex across clabel barriers");

        if (_coupled_state != nullptr)
        {
            if (_overlap_stats.virtual_remove_size(v, r) == 0)
            {
                _coupled_state->remove_partition_node(r, _bclabel[r]);
                _coupled_state->set_vertex_weight(r, 0);
            }

            if (_wr[nr] == 0)
            {
                _coupled_state->set_vertex_weight(nr, 1);
                _coupled_state->add_partition_node(nr, _bclabel[r]);
                _bclabel[nr] = _bclabel[r];
            }
        }

        if (is_partition_stats_enabled())
            get_partition_stats(v).move_vertex(v, r, nr, _deg_corr, _g);

        remove_vertex(v);
        add_vertex(v, nr);
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

    template <class VMap>
    void set_partition(VMap&& b)
    {
        for (auto v : vertices_range(_g))
            move_vertex(v, b[v]);
    }

    void set_partition(boost::any& ab)
    {
        vmap_t& b = boost::any_cast<vmap_t&>(ab);
        set_partition<typename vmap_t::unchecked_t>(b.get_unchecked());
    }

    size_t virtual_remove_size(size_t v)
    {
        return _overlap_stats.virtual_remove_size(v, _b[v]);
    }

    template <class MEntries>
    void get_move_entries(size_t v, size_t r, size_t nr, MEntries& m_entries)
    {
        auto mv_entries = [&](auto&&... args)
            {
                move_entries(v, r, nr, _b, _g, _eweight,
                             num_vertices(_bg), m_entries,
                             [](auto) {return false;},
                             is_loop_overlap(_overlap_stats), args...);
            };

        if (_rt == weight_type::NONE)
        {
            mv_entries();
        }
        else
        {
            if (_rt == weight_type::REAL_NORMAL)
                mv_entries(_rec, _drec);
            else
                mv_entries(_rec);
        }
    }

    // compute the entropy difference of a virtual move of vertex from block r to nr
    template <bool exact, class MEntries>
    double virtual_move_sparse(size_t v, size_t nr, bool multigraph,
                               MEntries& m_entries) const
    {
        size_t r = _b[v];

        if (r == nr)
            return 0.;

        size_t kout = out_degreeS()(v, _g);
        size_t kin = 0;
        if (is_directed::apply<g_t>::type::value)
            kin = in_degreeS()(v, _g);

        double dS = entries_dS<exact>(m_entries, _mrs, _emat, _bg);

        int dwr = _wr[r] - _overlap_stats.virtual_remove_size(v, r, kin, kout);
        int dwnr = _overlap_stats.virtual_add_size(v, nr) - _wr[nr];

        if (_deg_corr)
            dS += _overlap_stats.virtual_move_dS(v, r, nr, _g, kin, kout);

        if (multigraph)
            dS += _overlap_stats.virtual_move_parallel_dS(v, r, nr, _b, _g);

        if (!is_directed::apply<g_t>::type::value)
            kin = kout;

        auto vt = [&](auto mrp, auto mrm, auto nr)
            {
                if (exact)
                    return vterm_exact(mrp, mrm, nr, _deg_corr, _bg);
                else
                    return vterm(mrp, mrm, nr, _deg_corr, _bg);
            };

        dS += vt(_mrp[r]  - kout, _mrm[r]  - kin, _wr[r]  - dwr );
        dS += vt(_mrp[nr] + kout, _mrm[nr] + kin, _wr[nr] + dwnr);
        dS -= vt(_mrp[r]        , _mrm[r]       , _wr[r]        );
        dS -= vt(_mrp[nr]       , _mrm[nr]      , _wr[nr]       );

        return dS;
    }

    template <bool exact>
    double virtual_move_sparse(size_t v, size_t nr, bool multigraph)
    {
        return virtual_move_sparse<exact>(v, nr, multigraph, _m_entries);
    }

    template <class MEntries>
    double virtual_move_dense(size_t, size_t, bool, MEntries&) const
    {
        throw GraphException("Dense entropy for overlapping model not implemented!");
    }

    double virtual_move_dense(size_t v, size_t nr, bool multigraph)
    {
        return virtual_move_dense(v, nr, multigraph, _m_entries);
    }

    template <class MEntries>
    double virtual_move(size_t v, size_t r, size_t nr, entropy_args_t ea,
                        MEntries& m_entries)
    {
        if (r == nr)
            return 0;

        if (!allow_move(r, nr))
            return std::numeric_limits<double>::infinity();

        get_move_entries(v, r, nr, m_entries);

        double dS = 0;
        if (ea.adjacency)
        {
            if (ea.exact)
                dS = virtual_move_sparse<true>(v, nr, ea.multigraph, m_entries);
            else
                dS = virtual_move_sparse<false>(v, nr, ea.multigraph, m_entries);
        }

        if (ea.partition_dl || ea.degree_dl || ea.edges_dl)
        {
            enable_partition_stats();
            auto& ps = get_partition_stats(v);
            if (ea.partition_dl)
                dS += ps.get_delta_partition_dl(v, r, nr, _g);
            if (_deg_corr && ea.degree_dl)
                dS += ps.get_delta_deg_dl(v, r, nr, _eweight, _g);
            if (ea.edges_dl)
            {
                size_t actual_B = 0;
                for (auto& ps : _partition_stats)
                    actual_B += ps.get_actual_B();
                dS += ps.get_delta_edges_dl(v, r, nr, actual_B, _g);
            }
        }

        int dL = 0;
        if (ea.recs)
        {
            auto positive_entries_op = [&](size_t i, auto&& w_log_P,
                                           auto&& w_log_prior)
                {
                    int dB_E = 0;
                    entries_op(m_entries, this->_emat,
                               [&](auto, auto, auto& me, auto& delta)
                               {
                                   double ers = 0;
                                   double xrs = 0;
                                   if (me != _emat.get_null_edge())
                                   {
                                       ers = this->_brec[0][me];
                                       xrs = this->_brec[i][me];
                                   }
                                   auto d = get<1>(delta)[0];
                                   auto dx = get<1>(delta)[i];
                                   dS -= -w_log_P(ers, xrs);
                                   dS += -w_log_P(ers + d, xrs + dx);

                                   if (ea.recs_dl)
                                   {
                                       size_t ers = 0;
                                       if (me != _emat.get_null_edge())
                                           ers = this->_mrs[me];
                                       if (ers == 0 && get<0>(delta) > 0)
                                           dB_E++;
                                       if (ers > 0 && ers + get<0>(delta) == 0)
                                           dB_E--;
                                   }
                               });
                    if (dB_E != 0 && ea.recs_dl && std::isnan(_wparams[i][0])
                        && std::isnan(_wparams[i][1]))
                    {
                        dS -= -w_log_prior(_B_E);
                        dS += -w_log_prior(_B_E + dB_E);
                    }
                };

            for (size_t i = 0; i < _rec_types.size(); ++i)
            {
                auto& wp = _wparams[i];
                switch (_rec_types[i])
                {
                case weight_type::COUNT:
                    break;
                case weight_type::REAL_EXPONENTIAL:
                    positive_entries_op(i,
                                        [&](auto N, auto x)
                                        { return positive_w_log_P(N, x, wp[0],
                                                                  wp[1],
                                                                  this->_epsilon[i]);
                                        },
                                        [&](size_t B_E)
                                        { return positive_w_log_P(B_E,
                                                                  _recsum[i],
                                                                  wp[0], wp[1],
                                                                  this->_epsilon[i]);
                                        });
                    break;
                case weight_type::DISCRETE_GEOMETRIC:
                    positive_entries_op(i,
                                        [&](auto N, auto x)
                                        { return geometric_w_log_P(N, x, wp[0],
                                                                   wp[1]);
                                        },
                                        [&](size_t B_E)
                                        { return geometric_w_log_P(B_E,
                                                                   _recsum[i],
                                                                   wp[0],
                                                                   wp[1]);
                                        });
                    break;
                case weight_type::DISCRETE_POISSON:
                    positive_entries_op(i,
                                        [&](auto N, auto x)
                                        { return poisson_w_log_P(N, x, wp[0],
                                                                 wp[1]);
                                        },
                                        [&](size_t B_E)
                                        { return geometric_w_log_P(B_E,
                                                                   _recsum[i],
                                                                   wp[0],
                                                                   wp[1]);
                                        });
                    break;
                case weight_type::DISCRETE_BINOMIAL:
                    positive_entries_op(i,
                                        [&](auto N, auto x)
                                        { return binomial_w_log_P(N, x, wp[0],
                                                                  wp[1], wp[2]);
                                        },
                                        [&](size_t B_E)
                                        { return geometric_w_log_P(B_E,
                                                                   _recsum[i],
                                                                   wp[1],
                                                                   wp[2]);
                                        });
                    break;
                case weight_type::REAL_NORMAL:
                    {
                        int dB_E = 0;
                        int dB_E_D = 0;
                        double dBx2 = 0;
                        _dBdx[i] = 0;
                        entries_op(m_entries, _emat,
                                   [&](auto, auto, auto& me, auto& delta)
                                   {
                                       double ers = 0;
                                       double xrs = 0, x2rs = 0;
                                       if (me != _emat.get_null_edge())
                                       {
                                           ers = this->_brec[0][me];
                                           xrs = this->_brec[i][me];
                                           x2rs = this->_bdrec[i][me];
                                       }
                                       auto d = get<1>(delta)[0];
                                       auto dx = get<1>(delta)[i];
                                       auto dx2 = get<2>(delta)[i];
                                       dS -= -signed_w_log_P(ers, xrs, x2rs,
                                                             wp[0], wp[1],
                                                             wp[2], wp[3],
                                                             this->_epsilon[i]);
                                       dS += -signed_w_log_P(ers + d,
                                                             xrs + dx,
                                                             x2rs + dx2,
                                                             wp[0], wp[1],
                                                             wp[2], wp[3],
                                                             this->_epsilon[i]);
                                       if (std::isnan(wp[0]) &&
                                           std::isnan(wp[1]))
                                       {
                                           auto n_ers = ers + get<1>(delta)[0];
                                           if (ers == 0 && n_ers > 0)
                                               dB_E++;
                                           if (ers > 0 && n_ers == 0)
                                               dB_E--;
                                           if (n_ers > 1)
                                           {
                                               if (ers < 2)
                                                   dB_E_D++;
                                               _dBdx[i] += \
                                                   (x2rs + dx2 -
                                                    std::pow(xrs + dx, 2) / n_ers);

                                           }
                                           if (ers > 1)
                                           {
                                               if (n_ers < 2)
                                                   dB_E_D--;
                                               _dBdx[i] -= \
                                                   (x2rs -
                                                    std::pow(xrs, 2) / ers);
                                           }
                                           dBx2 += (std::pow(xrs + dx, 2) -
                                                    std::pow(xrs, 2));

                                       }
                                   });

                        if (std::isnan(wp[0]) && std::isnan(wp[1]))
                        {
                            if (ea.recs_dl && (dB_E != 0 || dBx2 != 0))
                            {
                                dS -= -signed_w_log_P(_B_E, _recsum[i],
                                                      _recx2[i], wp[0], wp[1],
                                                      wp[2], wp[3], _epsilon[i]);
                                dS += -signed_w_log_P(_B_E + dB_E, _recsum[i],
                                                      _recx2[i] + dBx2, wp[0],
                                                      wp[1], wp[2], wp[3],
                                                      _epsilon[i]);
                            }

                            if (dB_E_D != 0 || _dBdx[i] != 0)
                            {
                                dS -= -positive_w_log_P(_B_E_D, _recdx[i],
                                                        wp[2], wp[3],
                                                        _epsilon[i]);
                                dS += -positive_w_log_P(_B_E_D + dB_E_D,
                                                        _recdx[i] + _dBdx[i],
                                                        wp[2], wp[3],
                                                        _epsilon[i]);
                            }

                            if (dL == 0)
                            {
                                if (_B_E_D == 0 && dB_E_D > 0)
                                    dL++;
                                if (_B_E_D > 0 && _B_E_D + dB_E_D == 0)
                                    dL--;
                            }

                            if (_Lrecdx[0] >= 0)
                            {
                                size_t N_B_E_D = _B_E_D + dB_E_D;

                                dS -= -safelog(_B_E_D);
                                dS += -safelog(N_B_E_D);

                                _dBdx[i] = _recdx[i] * dB_E_D + _dBdx[i] * N_B_E_D;

                                if (_coupled_state == nullptr)
                                {
                                    size_t L = _Lrecdx[0];
                                    dS -= -positive_w_log_P(L, _Lrecdx[i+1],
                                                            wp[2], wp[3],
                                                            _epsilon[i]);
                                    dS += -positive_w_log_P(L + dL,
                                                            _Lrecdx[i+1] +
                                                            _dBdx[i], wp[2],
                                                            wp[3], _epsilon[i]);
                                }
                            }
                        }
                    }
                    break;
                case weight_type::DELTA_T:
                    break;
                }
            }
        }

        if (_coupled_state != nullptr)
        {
            bool r_vacate = (r != null_group) &&
                ( _overlap_stats.virtual_remove_size(v, r) == 0);
            bool nr_occupy = (nr != null_group) && (_wr[nr] == 0);
            if (r_vacate != nr_occupy)
            {
                scoped_lock lck(_lock);
                if (r_vacate)
                {
                    dS += _coupled_state->virtual_move(r,
                                                       _bclabel[r],
                                                       null_group,
                                                       _coupled_entropy_args);
                }

                if (nr_occupy)
                {
                    dS += _coupled_state->virtual_move(nr,
                                                       null_group,
                                                       _bclabel[r],
                                                       _coupled_entropy_args);
                }
            }

            if (ea.recs && !_rec_types.empty())
            {
                auto& recs_entries = m_entries._recs_entries;
                recs_entries.clear();
                entries_op(m_entries, _emat,
                           [&](auto r, auto s, auto& me, auto& delta)
                           {
                               recs_entries.emplace_back(r, s, me,
                                                         get<0>(delta),
                                                         get<1>(delta));
                           });
                scoped_lock lck(_lock);
                dS += _coupled_state->recs_dS(r, nr, recs_entries, _dBdx, dL);
            }
        }

        return dS;
    }

    double virtual_move(size_t v, size_t r, size_t nr, entropy_args_t ea)
    {
        return virtual_move(v, r, nr, ea, _m_entries);
    }

    double get_delta_partition_dl(size_t v, size_t r, size_t nr)
    {
        enable_partition_stats();
        return get_partition_stats(v).get_delta_partition_dl(v, r, nr, _g);
    }

    double recs_dS(size_t, size_t,
                   const std::vector<std::tuple<size_t, size_t,
                                                GraphInterface::edge_t, int,
                                                std::vector<double>>> &,
                   std::vector<double>&, int)
    {
        return 0;
    }

    // Sample node placement
    template <class RNG>
    size_t sample_block(size_t v, double c, double, RNG& rng)
    {
        // attempt random block
        size_t s = uniform_sample(_candidate_blocks, rng);

        if (!std::isinf(c))
        {
            size_t w = get_lateral_half_edge(v, rng);

            size_t u = _overlap_stats.get_out_neighbor(w);
            if (u >= num_vertices(_g))
                u = _overlap_stats.get_in_neighbor(w);

            size_t t = _b[u];
            double p_rand = 0;
            if (c > 0)
            {
                size_t B = num_vertices(_bg);
                if (is_directed::apply<g_t>::type::value)
                    p_rand = c * B / double(_mrp[t] + _mrm[t] + c * B);
                else
                    p_rand = c * B / double(_mrp[t] + c * B);
            }

            typedef std::uniform_real_distribution<> rdist_t;
            if (c == 0 || rdist_t()(rng) >= p_rand)
            {
                if (_egroups.empty())
                    _egroups.init(_b, _eweight, _g, _bg);
                const auto& e = _egroups.sample_edge(t, rng);
                s = _b[target(e, _g)];
                if (s == t)
                    s = _b[source(e, _g)];
            }
        }

        return s;
    }

    size_t sample_block(size_t v, double c, double d, rng_t& rng)
    {
        return sample_block<rng_t>(v, c, d, rng);
    }

    template <class RNG>
    size_t get_lateral_half_edge(size_t v, RNG& rng)
    {
        size_t vv = _overlap_stats.get_node(v);
        size_t w = _overlap_stats.sample_half_edge(vv, rng);
        return w;
    }

    template <class RNG>
    size_t random_neighbor(size_t v,  RNG& rng)
    {
        size_t w = get_lateral_half_edge(v, _overlap_stats, rng);

        size_t u = _overlap_stats.get_out_neighbor(w);
        if (u >= num_vertices(_g))
            u = _overlap_stats.get_in_neighbor(w);
        return u;
    }

    // Computes the move proposal probability
    template <class MEntries>
    double get_move_prob(size_t v, size_t r, size_t s, double c, double,
                         bool reverse, MEntries& m_entries)
    {
        typedef typename graph_traits<g_t>::vertex_descriptor vertex_t;
        size_t B = num_vertices(_bg);
        double p = 0;
        size_t w = 0;

        size_t kout = out_degreeS()(v, _g, _eweight);
        size_t kin = kout;
        if (is_directed::apply<g_t>::type::value)
            kin = in_degreeS()(v, _g, _eweight);

        size_t vi = _overlap_stats.get_node(v);
        auto& ns = _overlap_stats.get_half_edges(vi);

        for (size_t v: ns)
        {
            for (auto e : all_edges_range(v, _g))
            {
                vertex_t u = target(e, _g);
                if (is_directed::apply<g_t>::type::value && u == v)
                    u = source(e, _g);
                vertex_t t = _b[u];
                if (u == v)
                    t = r;
                size_t ew = _eweight[e];
                w += ew;

                int mts = 0;
                const auto& me = m_entries.get_me(t, s, _emat);
                if (me != _emat.get_null_edge())
                    mts = _mrs[me];
                int mtp = _mrp[t];
                int mst = mts;
                int mtm = mtp;

                if (is_directed::apply<g_t>::type::value)
                {
                    mst = 0;
                    const auto& me = m_entries.get_me(s, t, _emat);
                    if (me != _emat.get_null_edge())
                        mst = _mrs[me];
                    mtm = _mrm[t];
                }

                if (reverse)
                {
                    int dts = get<0>(m_entries.get_delta(t, s));
                    int dst = dts;
                    if (is_directed::apply<g_t>::type::value)
                        dst = get<0>(m_entries.get_delta(s, t));

                    mts += dts;
                    mst += dst;

                    if (t == s)
                    {
                        mtp -= kout;
                        mtm -= kin;
                    }

                    if (t == r)
                    {
                        mtp += kout;
                        mtm += kin;
                    }
                }

                if (is_directed::apply<g_t>::type::value)
                {
                    p += ew * ((mts + mst + c) / (mtp + mtm + c * B));
                }
                else
                {
                    if (t == s)
                        mts *= 2;
                    p += ew * (mts + c) / (mtp + c * B);
                }
            }
        }
        if (w > 0)
            return p / w;
        else
            return 1. / B;
    }

    double get_move_prob(size_t v, size_t r, size_t s, double c, double d,
                         bool reverse)
    {
        return get_move_prob(v, r, s, c, d, reverse, _m_entries);
    }

    bool is_last(size_t v)
    {
        auto r = _b[v];
        return _overlap_stats.virtual_remove_size(v, r) == 0;
    }

    size_t node_weight(size_t)
    {
        return 1;
    }

    double sparse_entropy(bool multigraph, bool deg_entropy, bool exact) const
    {
        double S = 0;
        if (exact)
        {
            for (auto e : edges_range(_bg))
                S += eterm_exact(source(e, _bg), target(e, _bg), _mrs[e], _bg);
            for (auto v : vertices_range(_bg))
                S += vterm_exact(_mrp[v], _mrm[v], _wr[v], _deg_corr, _bg);
        }
        else
        {
            for (auto e : edges_range(_bg))
                S += eterm(source(e, _bg), target(e, _bg), _mrs[e], _bg);
            for (auto v : vertices_range(_bg))
                S += vterm(_mrp[v], _mrm[v], _wr[v], _deg_corr, _bg);
        }

        if (_deg_corr && deg_entropy)
        {
            typedef gt_hash_map<int, int> map_t;

            map_t in_hist, out_hist;
            size_t N = _overlap_stats.get_N();

            for (size_t v = 0; v < N; ++v)
            {
                in_hist.clear();
                out_hist.clear();

                const auto& half_edges = _overlap_stats.get_half_edges(v);
                for (size_t u : half_edges)
                {
                    in_hist[_b[u]] += in_degreeS()(u, _g);
                    out_hist[_b[u]] += out_degree(u, _g);
                }

                for (auto& k_c : in_hist)
                    S -= lgamma_fast(k_c.second + 1);
                for (auto& k_c : out_hist)
                    S -= lgamma_fast(k_c.second + 1);
            }
        }

        if (multigraph)
            S += get_parallel_entropy();
        return S;
    }

    double dense_entropy(bool)
    {
        throw GraphException("Dense entropy for overlapping model not implemented!");
    }

    double entropy(bool dense, bool multigraph, bool deg_entropy, bool exact,
                   bool recs, bool recs_dl, bool adjacency)
    {
        double S = 0;
        if (adjacency)
        {
            if (dense)
                S = dense_entropy(multigraph);
            else
                S = sparse_entropy(multigraph, deg_entropy, exact);
        }

        if (recs)
        {
            for (size_t i = 0; i < _rec_types.size(); ++i)
            {
                auto& wp = _wparams[i];
                switch (_rec_types[i])
                {
                case weight_type::COUNT:
                    break;
                case weight_type::REAL_EXPONENTIAL:
                    for (auto me : edges_range(_bg))
                    {
                        auto ers = _brec[0][me];
                        auto xrs = _brec[i][me];
                        S += -positive_w_log_P(ers, xrs, wp[0], wp[1],
                                               _epsilon[i]);
                    }
                    if (recs_dl && std::isnan(wp[0]) && std::isnan(wp[1]))
                        S += -positive_w_log_P(_B_E, _recsum[i], wp[0], wp[1],
                                               _epsilon[i]);
                    break;
                case weight_type::DISCRETE_GEOMETRIC:
                    for (auto me : edges_range(_bg))
                    {
                        auto ers = _brec[0][me];
                        auto xrs = _brec[i][me];
                        S += -geometric_w_log_P(ers, xrs, wp[0], wp[1]);
                    }
                    if (recs_dl && std::isnan(wp[0]) && std::isnan(wp[1]))
                        S += -geometric_w_log_P(_B_E, _recsum[i], wp[0], wp[1]);
                    break;
                case weight_type::DISCRETE_POISSON:
                    for (auto me : edges_range(_bg))
                    {
                        auto ers = _brec[0][me];
                        auto xrs = _brec[i][me];
                        S += -poisson_w_log_P(ers, xrs, wp[0], wp[1]);
                    }
                    for (auto e : edges_range(_g))
                        S += lgamma(_rec[i][e] + 1);
                    if (recs_dl && std::isnan(wp[0]) && std::isnan(wp[1]))
                        S += -geometric_w_log_P(_B_E, _recsum[i], wp[0], wp[1]);
                    break;
                case weight_type::DISCRETE_BINOMIAL:
                    for (auto me : edges_range(_bg))
                    {
                        auto ers = _brec[0][me];
                        auto xrs = _brec[i][me];
                        S += -binomial_w_log_P(ers, xrs, wp[0], wp[1], wp[2]);
                    }
                    for (auto e : edges_range(_g))
                        S -= lbinom(wp[0], _rec[i][e]);
                    if (recs_dl && std::isnan(wp[1]) && std::isnan(wp[2]))
                        S += -geometric_w_log_P(_B_E, _recsum[i], wp[1], wp[2]);
                    break;
                case weight_type::REAL_NORMAL:
                    for (auto me : edges_range(_bg))
                    {
                        auto ers = _brec[0][me];
                        auto xrs = _brec[i][me];
                        auto x2rs = _bdrec[i][me];
                        S += -signed_w_log_P(ers, xrs, x2rs, wp[0], wp[1],
                                             wp[2], wp[3], _epsilon[i]);
                    }
                    if (std::isnan(wp[0]) && std::isnan(wp[1]))
                    {
                        if (recs_dl)
                            S += -signed_w_log_P(_B_E, _recsum[i], _recx2[i],
                                                 wp[0], wp[1], wp[2], wp[3],
                                                 _epsilon[i]);
                        S += -positive_w_log_P(_B_E_D, _recdx[i], wp[2], wp[3],
                                               _epsilon[i]);
                    }
                    break;
                case weight_type::DELTA_T: // waiting times
                    break;
                }
            }
        }
        return S;
    }

    double get_partition_dl()
    {
        if (!is_partition_stats_enabled())
            enable_partition_stats();
        double S = 0;
        for (auto& ps : _partition_stats)
            S += ps.get_partition_dl();
        return S;
    }

    double get_deg_dl(int kind)
    {
        if (!is_partition_stats_enabled())
            enable_partition_stats();
        double S = 0;
        for (auto& ps : _partition_stats)
            S += ps.get_deg_dl(kind);
        return S;
    }

    double get_parallel_entropy() const
    {
        double S = 0;
        for (const auto& h : _overlap_stats.get_parallel_bundles())
        {
            for (const auto& kc : h)
            {
                bool is_loop = get<2>(kc.first);
                auto m = kc.second;
                if (is_loop)
                {
                    assert(m % 2 == 0);
                    S += lgamma_fast(m/2 + 1) + m * log(2) / 2;
                }
                else
                {
                    S += lgamma_fast(m + 1);
                }
            }
        }
        return S;
    }

    void enable_partition_stats()
    {
        if (_partition_stats.empty())
        {

            size_t E = num_vertices(_g) / 2;
            size_t B = num_vertices(_bg);

            auto vi = std::max_element(vertices(_g).first, vertices(_g).second,
                                       [&](auto u, auto v)
                                       { return this->_pclabel[u] < this->_pclabel[v];});
            size_t C = _pclabel[*vi] + 1;

            vector<gt_hash_set<size_t>> vcs(C);
            vector<size_t> rc(num_vertices(_bg));
            for (auto v : vertices_range(_g))
            {
                vcs[_pclabel[v]].insert(_overlap_stats.get_node(v));
                rc[_b[v]] = _pclabel[v];
            }

            for (size_t c = 0; c < C; ++c)
                _partition_stats.emplace_back(_g, _b, vcs[c], E, B,
                                              _eweight, _overlap_stats,
                                              _bmap, _vmap, _allow_empty);

            for (size_t r = 0; r < num_vertices(_bg); ++r)
                _partition_stats[rc[r]].get_r(r);
        }
    }

    void disable_partition_stats()
    {
        _partition_stats.clear();
    }

    bool is_partition_stats_enabled() const
    {
        return !_partition_stats.empty();
    }

    overlap_partition_stats_t& get_partition_stats(size_t v)
    {
        return _partition_stats[_pclabel[v]];
    }

    void couple_state(BlockStateVirtualBase& s, entropy_args_t ea)
    {
        _coupled_state = &s;
        _coupled_entropy_args = ea;
    }

    void decouple_state()
    {
        _coupled_state = nullptr;
    }

    void clear_egroups()
    {
        _egroups.clear();
    }

    void rebuild_neighbor_sampler()
    {
    }

    void sync_emat()
    {
        _emat.sync(_bg);
    }

    size_t get_N()
    {
        return _overlap_stats.get_N();
    }

    template <class Graph, class EMap>
    void get_be_overlap(Graph& g, EMap be)
    {
        for (auto ei : edges_range(_g))
        {
            auto u = source(ei, _g);
            auto v = target(ei, _g);

            auto s = vertex(_node_index[u], g);
            auto t = vertex(_node_index[v], g);

            for (auto e : out_edges_range(s, g))
            {
                if (!be[e].empty() || target(e, g) != t)
                    continue;
                if (is_directed::apply<Graph>::type::value || s < target(e, g))
                    be[e] = {_b[u], _b[v]};
                else
                    be[e] = {_b[v], _b[u]};
                break;
            }

            for (auto e : in_edges_range(t, g))
            {
                if (!be[e].empty() || source(e, g) != s)
                    continue;
                be[e] = {_b[u], _b[v]};
                break;
            }
        }
    }

    template <class Graph, class VMap>
    void get_bv_overlap(Graph& g, VMap bv, VMap bc_in, VMap bc_out,
                        VMap bc_total)
    {
        typedef gt_hash_map<int, int> map_t;
        vector<map_t> hist_in;
        vector<map_t> hist_out;

        for (auto v : vertices_range(_g))
        {
            if (out_degree(v, _g) > 0)
            {
                size_t s = _node_index[v];
                if (s >= hist_out.size())
                    hist_out.resize(s + 1);
                hist_out[s][_b[v]]++;
            }

            if (in_degreeS()(v, _g) > 0)
            {
                size_t t = _node_index[v];
                if (t >= hist_in.size())
                    hist_in.resize(t + 1);
                hist_in[t][_b[v]]++;
            }
        }

        hist_in.resize(num_vertices(g));
        hist_out.resize(num_vertices(g));

        set<size_t> rs;
        for (auto i : vertices_range(g))
        {
            rs.clear();
            for (auto iter = hist_out[i].begin(); iter != hist_out[i].end(); ++iter)
                rs.insert(iter->first);
            for (auto iter = hist_in[i].begin(); iter != hist_in[i].end(); ++iter)
                rs.insert(iter->first);
            // if (rs.empty())
            //     throw GraphException("Cannot have empty overlapping block membership!");
            for (size_t r : rs)
            {
                bv[i].push_back(r);

                auto iter_in = hist_in[i].find(r);
                if (iter_in != hist_in[i].end())
                    bc_in[i].push_back(iter_in->second);
                else
                    bc_in[i].push_back(0);

                auto iter_out = hist_out[i].find(r);
                if (iter_out != hist_out[i].end())
                    bc_out[i].push_back(iter_out->second);
                else
                    bc_out[i].push_back(0);

                bc_total[i].push_back(bc_in[i].back() +
                                      bc_out[i].back());
            }
        }
    }

    template <class Graph, class VVProp, class VProp>
    void get_overlap_split(Graph& g, VVProp bv, VProp b) const
    {
        gt_hash_map<vector<int>, size_t> bvset;

        for (auto v : vertices_range(g))
        {
            auto r = bv[v];
            auto iter = bvset.find(r);
            if (iter == bvset.end())
                iter = bvset.insert(make_pair(r, bvset.size())).first;
            b[v] = iter->second;
        }
    }

    size_t add_block()
    {
        size_t r = boost::add_vertex(_bg);
        _wr.resize(num_vertices(_bg));
        _mrm.resize(num_vertices(_bg));
        _mrp.resize(num_vertices(_bg));
        _wr[r] = _mrm[r] = _mrp[r] = 0;
        _bclabel.resize(num_vertices(_bg));
        _candidate_blocks.push_back(r);
        _overlap_stats.add_block();
        for (auto& p : _partition_stats)
            p.add_block();
        if (!_egroups.empty())
            _egroups.init(_b, _eweight, _g, _bg);
        if (_coupled_state != nullptr)
            _coupled_state->coupled_resize_vertex(r);
        sync_emat();
        return r;
    }

    void add_edge(const GraphInterface::edge_t&)
    {
    }

    void remove_edge(const GraphInterface::edge_t&)
    {
    }

    void update_edge(const GraphInterface::edge_t&, std::vector<double>&)
    {
    }

    void init_mcmc(double c, double dl)
    {
        if (!std::isinf(c))
        {
            if (_egroups.empty())
                _egroups.init(_b, _eweight, _g, _bg);
        }
        else
        {
            _egroups.clear();
        }

        if (dl)
            enable_partition_stats();
        else
            disable_partition_stats();
    }

    bool check_edge_counts(bool emat=true)
    {
        gt_hash_map<std::pair<size_t, size_t>, size_t> mrs;
        for (auto e : edges_range(_g))
        {
            size_t r = _b[source(e, _g)];
            size_t s = _b[target(e, _g)];
            if (!is_directed::apply<g_t>::type::value && s < r)
                std::swap(r, s);
            mrs[std::make_pair(r, s)] += _eweight[e];
        }

        for (auto& rs_m : mrs)
        {
            auto r = rs_m.first.first;
            auto s = rs_m.first.second;
            if (rs_m.second == 0)
                continue;
            typename graph_traits<bg_t>::edge_descriptor me;
            if (emat)
            {
                me = _emat.get_me(r, s);
                if (me == _emat.get_null_edge())
                {
                    assert(false);
                    return false;
                }
            }
            else
            {
                auto ret = boost::edge(r, s, _bg);
                assert(ret.second);
                if (!ret.second)
                    return false;
                me = ret.first;
            }
            if (size_t(_mrs[me]) != rs_m.second)
            {
                assert(false);
                return false;
            }
        }
        if (_coupled_state != nullptr)
            if (!_coupled_state->check_edge_counts(false))
                return false;
        return true;
    }

    void add_partition_node(size_t, size_t) { }
    void remove_partition_node(size_t, size_t) { }
    void set_vertex_weight(size_t, int) { }
    void coupled_resize_vertex(size_t) { }
    void update_edge(const GraphInterface::edge_t&,
                     const std::vector<double>&) { }

//private:
    typedef typename
        std::conditional<is_directed::apply<g_t>::type::value,
                         GraphInterface::multigraph_t,
                         undirected_adaptor<GraphInterface::multigraph_t>>::type
        bg_t;
    bg_t& _bg;

    typename mrs_t::checked_t _c_mrs;
    std::vector<typename brec_t::value_type::checked_t> _c_brec;
    std::vector<typename brec_t::value_type::checked_t> _c_bdrec;
    std::vector<double> _recsum;
    std::vector<double> _recx2;
    std::vector<double> _dBdx;
    std::vector<double> _rdelta;
    size_t _B_E = 0;
    size_t _B_E_D = 0;
    int _rt = weight_type::NONE;

    typedef typename std::conditional<use_hash_t::value,
                                      EHash<bg_t>,
                                      EMat<bg_t>>::type
        emat_t;
    emat_t _emat;

    EGroups<g_t, mpl::false_> _egroups;
    bool _egroups_enabled;

    overlap_stats_t _overlap_stats;
    std::vector<overlap_partition_stats_t> _partition_stats;
    std::vector<size_t> _bmap;
    std::vector<size_t> _vmap;

    typedef SingleEntrySet<g_t, bg_t, int, std::vector<double>,
                           std::vector<double>> m_entries_t;
    m_entries_t _m_entries;

    UnityPropertyMap<int,GraphInterface::edge_t> _eweight;
    UnityPropertyMap<int,GraphInterface::vertex_t> _vweight;

    std::array<size_t, 0> _empty_blocks;

    BlockStateVirtualBase* _coupled_state;
    entropy_args_t _coupled_entropy_args;

    openmp_mutex _lock;
};

} // namespace graph_tool

#endif // GRAPH_BLOCKMODEL_OVERLAP_HH
