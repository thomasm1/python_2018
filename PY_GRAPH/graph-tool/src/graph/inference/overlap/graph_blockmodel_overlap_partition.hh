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

#ifndef GRAPH_BLOCKMODEL_OVERLAP_PARTITION_HH
#define GRAPH_BLOCKMODEL_OVERLAP_PARTITION_HH

#include <functional>
#include "graph_blockmodel_overlap_util.hh"
#include "boost/container/small_vector.hpp"

namespace std
{

template <class Value, size_t N>
struct hash<boost::container::small_vector<Value, N>>
{
    size_t operator()(const boost::container::small_vector<Value, N>& v) const
    {
        std::size_t seed = 0;
        for (auto& x : v)
            _hash_combine(seed, x);
        return seed;
    }
};
}

template <class Value, size_t N>
struct empty_key<boost::container::small_vector<Value, N>>
{
    static boost::container::small_vector<Value, N> get()
    {
        boost::container::small_vector<Value, N> key(1);
        key[0] = empty_key<Value>::get();
        return key;
    }
};

template <class Value, size_t N>
struct deleted_key<boost::container::small_vector<Value, N>>
{
    static boost::container::small_vector<Value, N> get()
    {
        boost::container::small_vector<Value, N> key(1);
        key[0] = deleted_key<Value>::get();
        return key;
    }
};


namespace graph_tool
{

//=============================
// Partition Description length
//=============================

struct overlap_partition_stats_t
{
    typedef std::tuple<int, int> deg_t;
    typedef boost::container::small_vector<deg_t, 64> cdeg_t;

    typedef boost::container::small_vector<int, 64> bv_t;

    typedef gt_hash_map<bv_t, size_t> bhist_t;
    typedef gt_hash_map<cdeg_t, size_t, std::hash<cdeg_t>> cdeg_hist_t;

    typedef gt_hash_map<bv_t, cdeg_hist_t> deg_hist_t;

    typedef gt_hash_map<bv_t, vector<size_t>> ebhist_t;

    typedef gt_hash_map<int, int> dmap_t;

    template <class Graph, class Vprop, class Eprop, class Vlist>
    overlap_partition_stats_t(Graph& g, Vprop& b, Vlist& vlist, size_t E,
                              size_t B, Eprop& eweight, overlap_stats_t& ostats,
                              std::vector<size_t>& bmap,
                              std::vector<size_t>& vmap,
                              bool allow_empty)
        : _overlap_stats(ostats), _bmap(bmap), _vmap(vmap),
          _allow_empty(allow_empty),
          _directed(is_directed::apply<Graph>::type::value)

    {
        _D = 0;
        _N = vlist.size();
        _E = E;
        _total_B = B;
        _dhist.resize(1);

        dmap_t in_hist, out_hist;
        for (size_t v : vlist)
        {
            auto nv = get_v(v);

            dmap_t in_hist, out_hist;
            set<size_t> rs;

            get_bv_deg(v, b, eweight, g, rs, in_hist, out_hist);

            bv_t bv;
            cdeg_t cdeg;
            for (auto r : rs)
            {
                cdeg.emplace_back(in_hist[r], out_hist[r]);
                bv.push_back(r);
            }

            assert(bv.size() > 0);

            _bvs[nv] = bv;
            _degs[nv] = cdeg;

            auto & cdh = _deg_hist[bv];
            cdh[cdeg]++;

            size_t d = bv.size();
            _D = std::max(_D, d);
            _dhist[d]++;
            _bhist[bv]++;

            auto& bmh = _embhist[bv];
            auto& bph = _epbhist[bv];
            bmh.resize(bv.size());
            bph.resize(bv.size());

            for (size_t i = 0; i < bv.size(); ++i)
            {
                size_t r = bv[i];
                auto& deg = cdeg[i];
                _emhist[r] += get<0>(deg);
                _ephist[r] += get<1>(deg);
                bmh[i] += get<0>(deg);
                bph[i] += get<1>(deg);
            }
        }

        for (auto& bv_c : _bhist)
        {
            assert(bv_c.second > 0);
            for (auto r : bv_c.first)
                _r_count[r] += 1;
        }

        _actual_B = _r_count.size();
    }

    size_t get_v(size_t v)
    {
        constexpr size_t null =
            std::numeric_limits<size_t>::max();
        if (v >= _vmap.size())
            _vmap.resize(v + 1, null);
        size_t nv = _vmap[v];
        if (nv == null)
            nv = _vmap[v] = _bvs.size();
        if (nv >= _bvs.size())
        {
            _bvs.resize(nv + 1);
            _degs.resize(nv + 1);
        }
        return nv;
    }

    size_t get_r(size_t r)
    {
        constexpr size_t null =
            std::numeric_limits<size_t>::max();
        if (r >= _bmap.size())
            _bmap.resize(r + 1, null);
        size_t nr = _bmap[r];
        if (nr == null)
            nr = _bmap[r] = _r_count.size();
        if (nr >= _r_count.size())
        {
            _r_count.resize(nr + 1);
            _dhist.resize(nr + 2);
            _emhist.resize(nr + 1);
            _ephist.resize(nr + 1);
        }
        return nr;
    }


    template <class Graph, class Vprop, class Eprop>
    void get_bv_deg(size_t v, Vprop& b, Eprop&, Graph& g, set<size_t>& rs,
                    dmap_t& in_hist, dmap_t& out_hist)
    {
        auto& half_edges = _overlap_stats.get_half_edges(v);
        for (size_t u : half_edges)
        {
            size_t kin = in_degreeS()(u, g);
            size_t kout = out_degreeS()(u, g);

            auto r = get_r(b[u]);
            in_hist[r] += kin;
            out_hist[r] += kout;
        }

        for (auto& rk : in_hist)
            rs.insert(rk.first);
    }

    double get_partition_dl() const
    {
        double S = 0;
        for (size_t d = 1; d < _dhist.size(); ++d)
        {
            size_t nd = _dhist[d];
            if (nd == 0)
                continue;
            double x;
            if (_allow_empty)
                x = lbinom_fast(_total_B, d);
            else
                x = lbinom_fast(_actual_B, d);
            double ss = lbinom_careful((exp(x) + nd) - 1, nd); // not fast
            if (std::isinf(ss) || std::isnan(ss))
                ss = nd * x - lgamma_fast(nd + 1);
            assert(!std::isinf(ss));
            assert(!std::isnan(ss));
            S += ss;
        }

        S += lbinom_fast(_D + _N - 1, _N) + lgamma_fast(_N + 1);

        for (auto& bh : _bhist)
            S -= lgamma_fast(bh.second + 1);

        return S;
    }

    double get_deg_dl_ent() const
    {
        double S = 0;
        for (auto& ch : _deg_hist)
        {
            auto& bv = ch.first;
            auto& cdeg_hist = ch.second;

            size_t n_bv = _bhist.find(bv)->second;

            S += xlogx(n_bv);
            for (auto& dh : cdeg_hist)
                S -= xlogx(dh.second);
        }
        return S;
    }

    double get_deg_dl_uniform() const
    {
        double S = 0;

        for (auto& ch : _deg_hist)
        {
            auto& bv = ch.first;
            size_t n_bv = _bhist.find(bv)->second;

            if (n_bv == 0)
                continue;

            const auto& bmh = _embhist.find(bv)->second;
            const auto& bph = _epbhist.find(bv)->second;

            for (size_t i = 0; i < bv.size(); ++i)
            {
                S += lbinom(n_bv + bmh[i] - 1, bmh[i]);
                S += lbinom(n_bv + bph[i] - 1, bph[i]);
            }
        }

        for (size_t r = 0; r < _r_count.size(); ++r)
        {
            if (_r_count[r] == 0)
                continue;
            S += lbinom(_r_count[r] + _emhist[r] - 1,  _emhist[r]);
            S += lbinom(_r_count[r] + _ephist[r] - 1,  _ephist[r]);
        }

        return S;
    }

    double get_deg_dl_dist() const
    {
        double S = 0;
        for (auto& ch : _deg_hist)
        {
            auto& bv = ch.first;
            auto& cdeg_hist = ch.second;

            size_t n_bv = _bhist.find(bv)->second;

            if (n_bv == 0)
                continue;

            const auto& bmh = _embhist.find(bv)->second;
            const auto& bph = _epbhist.find(bv)->second;

            for (size_t i = 0; i < bv.size(); ++i)
            {
                if (_directed)
                {
                    S += log_q(bmh[i], n_bv);
                    S += log_q(bph[i], n_bv);
                }
                else
                {
                    S += log_q(bph[i] - n_bv, n_bv);
                }
            }

            S += lgamma_fast(n_bv + 1);

            for (auto& dh : cdeg_hist)
                S -= lgamma_fast(dh.second + 1);
        }

        for (size_t r = 0; r < _r_count.size(); ++r)
        {
            if (_r_count[r] == 0)
                continue;
            S += lbinom(_r_count[r] + _emhist[r] - 1,  _emhist[r]);
            S += lbinom(_r_count[r] + _ephist[r] - 1,  _ephist[r]);
        }
        return S;
    }

    double get_deg_dl(int kind) const
    {
        switch (kind)
        {
        case deg_dl_kind::ENT:
            return get_deg_dl_ent();
        case deg_dl_kind::UNIFORM:
            return get_deg_dl_uniform();
        case deg_dl_kind::DIST:
            return get_deg_dl_dist();
        default:
            return numeric_limits<double>::quiet_NaN();
        }
    }

    template <class Graph>
    bool get_n_bv(size_t v, size_t r, size_t nr, const bv_t& bv,
                  const cdeg_t& deg, bv_t& n_bv, cdeg_t& n_deg, Graph& g,
                  size_t in_deg = 0, size_t out_deg = 0) const
    {
        size_t kin = (in_deg + out_deg == 0) ? in_degreeS()(v, g) : in_deg;
        size_t kout = (in_deg + out_deg == 0) ? out_degreeS()(v, g) : out_deg;

        static gt_hash_map<size_t, std::pair<int, int>> deg_delta;
        static vector<size_t> rs;

        auto& d_r = deg_delta[r];
        d_r.first -= kin;
        d_r.second -= kout;

        auto& d_nr = deg_delta[nr];
        d_nr.first += kin;
        d_nr.second += kout;

        n_deg.clear();
        n_bv.clear();
        bool is_same_bv = true;
        bool has_r = false, has_nr = false;
        for (size_t i = 0; i < bv.size(); ++i)
        {
            size_t s = bv[i];
            auto k_s = deg[i];

            auto& d_s = deg_delta[s];
            get<0>(k_s) += d_s.first;
            get<1>(k_s) += d_s.second;

            d_s.first = d_s.second = 0;

            if (s == r)
                has_r = true;
            else if (s == nr)
                has_nr = true;
            else
                rs.push_back(s);

            if ((get<0>(k_s) + get<1>(k_s)) > 0)
            {
                n_bv.push_back(s);
                n_deg.push_back(k_s);
            }
            else
            {
                is_same_bv = false;
            }
        }

        if (!has_r || !has_nr)
        {
            is_same_bv = false;
            std::array<size_t, 2> ss = {{r, nr}};
            for (auto s : ss)
            {
                auto& d_s = deg_delta[s];
                if (d_s.first + d_s.second == 0)
                    continue;
                size_t kin = d_s.first;
                size_t kout = d_s.second;
                auto pos = std::lower_bound(n_bv.begin(), n_bv.end(), s);
                auto dpos = n_deg.begin();
                std::advance(dpos, pos - n_bv.begin());
                n_bv.insert(pos, s);
                n_deg.insert(dpos, make_pair(kin, kout));
            }
        }

        deg_delta[r] = {0, 0};
        deg_delta[nr] = {0, 0};
        for (auto s : rs)
            deg_delta[s] = {0, 0};
        rs.clear();

        return is_same_bv;
    }

    // get deg counts without increasing the container
    size_t get_deg_count(const bv_t& bv, const cdeg_t& deg) const
    {
        auto iter = _deg_hist.find(bv);
        if (iter == _deg_hist.end())
            return 0;
        auto& hist = iter->second;
        if (hist.empty())
            return 0;
        auto diter = hist.find(deg);
        if (diter == hist.end())
            return 0;
        return diter->second;
    }

    // get bv counts without increasing the container
    size_t get_bv_count(const bv_t& bv) const
    {
        auto iter = _bhist.find(bv);
        if (iter == _bhist.end())
            return 0;
        return iter->second;
    }

    template <class Graph>
    double get_delta_partition_dl(size_t v, size_t r, size_t nr, const Graph& g,
                                  size_t in_deg = 0, size_t out_deg = 0)
    {
        if (r == nr)
            return 0;

        size_t o_r = r;
        size_t o_nr = nr;
        r = get_r(r);
        nr = get_r(nr);

        size_t u = _overlap_stats.get_node(v);

        u = get_v(u);

        auto& bv = _bvs[u];
        assert(bv.size() > 0);
        bv_t n_bv;
        size_t d = bv.size();
        const cdeg_t& deg = _degs[u];
        cdeg_t n_deg;

        bool is_same_bv = get_n_bv(v, r, nr, bv, deg, n_bv, n_deg, g, in_deg,
                                   out_deg);

        assert(n_bv.size() > 0);
        if (is_same_bv)
            return 0;

        size_t n_d = n_bv.size();
        size_t n_D = _D;

        if (d == _D && n_d < d && _dhist[d] == 1 && _D > 1)
        {
            n_D = _D - 1;
            while (_dhist[n_D] == 0)
            {
                if (n_D == 0)
                    break;
                n_D--;
            }
        }

        n_D = std::max(n_D, n_d);

        double S_a = 0, S_b = 0;

        if (n_D != _D)
        {
            S_b += lbinom_fast(_D  + _N - 1, _N);
            S_a += lbinom_fast(n_D + _N - 1, _N);
        }

        int dB = 0;
        if (_overlap_stats.virtual_remove_size(v, o_r, in_deg, out_deg) == 0)
            dB--;
        if (_overlap_stats.get_block_size(o_nr) == 0)
            dB++;

        auto get_S_d = [&] (size_t d_i, int delta, int dB) -> double
            {
                int nd = int(_dhist[d_i]) + delta;
                if (nd == 0)
                    return 0.;
                double x;
                if (_allow_empty)
                    x = lbinom_fast(_total_B + dB, d_i);
                else
                    x = lbinom_fast(_actual_B + dB, d_i);
                double S = lbinom_careful(exp(x) + nd - 1, nd); // not fast
                if (std::isinf(S) || std::isnan(S))
                    S = nd * x - lgamma_fast(nd + 1);
                return S;
            };

        if (dB == 0 || _allow_empty)
        {
            if (n_d != d)
            {
                S_b += get_S_d(d,  0, 0) + get_S_d(n_d, 0, 0);
                S_a += get_S_d(d, -1, 0) + get_S_d(n_d, 1, 0);
            }
        }
        else
        {
            for (size_t di = 0; di < min(_actual_B + abs(dB) + 1, _dhist.size()); ++di)
            {
                if (d != n_d)
                {
                    if (di == d)
                    {
                        S_b += get_S_d(d,  0, 0);
                        S_a += get_S_d(d, -1, dB);
                        continue;
                    }
                    if (di == n_d)
                    {
                        S_b += get_S_d(n_d, 0, 0);
                        S_a += get_S_d(n_d, 1, dB);
                        continue;
                    }
                }
                if (_dhist[di] == 0)
                    continue;
                S_b += get_S_d(di, 0, 0);
                S_a += get_S_d(di, 0, dB);
            }
        }

        size_t bv_count = get_bv_count(bv);
        assert(bv_count > 0);
        size_t n_bv_count = get_bv_count(n_bv);

        auto get_S_b = [&] (bool is_bv, int delta) -> double
            {
                assert(int(bv_count) + delta >= 0);
                if (is_bv)
                    return -lgamma_fast(bv_count + delta + 1);
                return -lgamma_fast(n_bv_count + delta + 1);
            };

        S_b += get_S_b(true,  0) + get_S_b(false, 0);
        S_a += get_S_b(true, -1) + get_S_b(false, 1);

        return S_a - S_b;
    }

    template <class Graph>
    double get_delta_edges_dl(size_t v, size_t r, size_t nr, size_t actual_B,
                              const Graph&)
    {
        if (r == nr || _allow_empty)
            return 0;

        double S_b = 0, S_a = 0;

        int dB = 0;
        if (_overlap_stats.virtual_remove_size(v, r) == 0)
            dB--;
        if (_overlap_stats.get_block_size(nr) == 0)
            dB++;

        if (dB != 0)
        {
            auto get_x = [](size_t B) -> size_t
                {
                    if (is_directed::apply<Graph>::type::value)
                        return B * B;
                    else
                        return (B * (B + 1)) / 2;
                };

            S_b += lbinom(get_x(actual_B) + _E - 1, _E);
            S_a += lbinom(get_x(actual_B + dB) + _E - 1, _E);
        }

        return S_a - S_b;
    }


    template <class Graph, class EWeight>
    double get_delta_deg_dl(size_t v, size_t r, size_t nr, const EWeight&,
                            const Graph& g, size_t in_deg = 0,
                            size_t out_deg = 0)
    {
        if (r == nr)
            return 0;

        r = get_r(r);
        nr = get_r(nr);

        double S_b = 0, S_a = 0;

        size_t u = get_v(_overlap_stats.get_node(v));
        auto& bv = _bvs[u];
        bv_t n_bv;

        const cdeg_t& deg = _degs[u];
        cdeg_t n_deg;

        bool is_same_bv = get_n_bv(v, r, nr, bv, deg, n_bv, n_deg, g, in_deg,
                                   out_deg);

        size_t bv_count = get_bv_count(bv);
        size_t n_bv_count = bv_count;

        auto get_S_bv = [&] (bool is_bv, int delta) -> double
            {
                if (is_bv)
                    return lgamma_fast(bv_count + delta + 1);
                return lgamma_fast(n_bv_count + delta + 1);
            };

        auto get_S_e = [&] (bool is_bv, int bdelta, int deg_delta) -> double
            {
                size_t bv_c = ((is_bv) ? bv_count : n_bv_count) + bdelta;
                if (bv_c == 0)
                    return 0.;

                const cdeg_t& deg_i = (is_bv) ? deg : n_deg;
                const auto& bv_i = (is_bv) ? bv : n_bv;

                double S = 0;
                if (((is_bv) ? bv_count : n_bv_count) > 0)
                {
                    const auto& bmh = _embhist.find(bv_i)->second;
                    const auto& bph = _epbhist.find(bv_i)->second;

                    assert(bmh.size() == bv_i.size());
                    assert(bph.size() == bv_i.size());

                    for (size_t i = 0; i < bv_i.size(); ++i)
                    {
                        if (_directed)
                        {
                            S += log_q(size_t(bmh[i] + deg_delta * int(get<0>(deg_i[i]))), bv_c);
                            S += log_q(size_t(bph[i] + deg_delta * int(get<1>(deg_i[i]))), bv_c);
                        }
                        else
                        {
                            S += log_q(size_t(bph[i] + deg_delta * int(get<1>(deg_i[i]))) - bv_c, bv_c);
                        }
                    }
                }
                else
                {
                    for (size_t i = 0; i < bv_i.size(); ++i)
                    {
                        if (_directed)
                        {
                            S += log_q(size_t(deg_delta * int(get<0>(deg_i[i]))), bv_c);
                            S += log_q(size_t(deg_delta * int(get<1>(deg_i[i]))), bv_c);
                        }
                        else
                        {
                            S += log_q(size_t(deg_delta * int(get<1>(deg_i[i]))) - bv_c, bv_c);
                        }
                    }
                }

                return S;
            };

        auto get_S_e2 = [&] (int deg_delta, int ndeg_delta) -> double
            {
                double S = 0;
                const auto& bmh = _embhist.find(bv)->second;
                const auto& bph = _epbhist.find(bv)->second;

                for (size_t i = 0; i < bv.size(); ++i)
                {
                    if (_directed)
                    {
                        S += log_q(size_t(bmh[i] +
                                          deg_delta * int(get<0>(deg[i])) +
                                          ndeg_delta * int(get<0>(n_deg[i]))),
                                   bv_count);
                        S += log_q(size_t(bph[i] +
                                          deg_delta * int(get<1>(deg[i])) +
                                          ndeg_delta * int(get<1>(n_deg[i]))),
                                   bv_count);
                    }
                    else
                    {
                        S += log_q(size_t(bph[i] +
                                          deg_delta * int(get<1>(deg[i])) +
                                          ndeg_delta * int(get<1>(n_deg[i])))
                                   - bv_count,
                                   bv_count);
                    }
                }
                return S;
            };

        if (!is_same_bv)
        {
            n_bv_count = get_bv_count(n_bv);

            S_b += get_S_bv(true,  0) + get_S_bv(false, 0);
            S_a += get_S_bv(true, -1) + get_S_bv(false, 1);

            S_b += get_S_e(true,  0,  0) + get_S_e(false, 0, 0);
            S_a += get_S_e(true, -1, -1) + get_S_e(false, 1, 1);
        }
        else
        {
            S_b += get_S_e2( 0, 0);
            S_a += get_S_e2(-1, 1);
        }

        size_t deg_count = get_deg_count(bv, deg);
        size_t n_deg_count = get_deg_count(n_bv, n_deg);

        auto get_S_deg = [&] (bool is_deg, int delta) -> double
            {
                if (is_deg)
                    return -lgamma_fast(deg_count + delta + 1);
                return -lgamma_fast(n_deg_count + delta + 1);
            };

        S_b += get_S_deg(true,  0) + get_S_deg(false, 0);
        S_a += get_S_deg(true, -1) + get_S_deg(false, 1);

        auto is_in = [&] (const bv_t& bv, size_t r) -> bool
            {
                auto iter = lower_bound(bv.begin(), bv.end(), r);
                if (iter == bv.end())
                    return false;
                if (size_t(*iter) != r)
                    return false;
                return true;
            };

        for (size_t s : bv)
        {
            S_b += lbinom_fast(_r_count[s] + _emhist[s] - 1, _emhist[s]);
            S_b += lbinom_fast(_r_count[s] + _ephist[s] - 1, _ephist[s]);
        }

        for (size_t s : n_bv)
        {
            if (is_in(bv, s))
                continue;
            S_b += lbinom_fast(_r_count[s] + _emhist[s] - 1, _emhist[s]);
            S_b += lbinom_fast(_r_count[s] + _ephist[s] - 1, _ephist[s]);
        }

        static gt_hash_map<size_t, pair<int, int>> deg_delta;
        static gt_hash_map<size_t, int> r_count_delta;

        if (bv != n_bv)
        {
            if (n_bv_count == 0)
            {
                for (auto s : n_bv)
                    r_count_delta[s] += 1;
            }

            if (bv_count == 1)
            {
                for (auto s : bv)
                   r_count_delta[s] -= 1;
            }
        }

        if (r != nr)
        {
            size_t kin = (in_deg + out_deg == 0) ? in_degreeS()(v, g) : in_deg;
            size_t kout = (in_deg + out_deg == 0) ? out_degreeS()(v, g) : out_deg;

            auto& d_r = deg_delta[r];
            d_r.first -= kin;
            d_r.second -= kout;

            auto& d_nr = deg_delta[nr];
            d_nr.first += kin;
            d_nr.second += kout;
        }

        for (size_t s : bv)
        {
            S_a += lbinom_fast(_r_count[s] + r_count_delta[s] + _emhist[s] + deg_delta[s].first - 1,
                               _emhist[s] + deg_delta[s].first);
            S_a += lbinom_fast(_r_count[s] + r_count_delta[s] + _ephist[s] + deg_delta[s].second - 1,
                               _ephist[s] + deg_delta[s].second);
        }

        for (size_t s : n_bv)
        {
            if (!is_in(bv, s))
            {
                S_a += lbinom_fast(_r_count[s] + r_count_delta[s] + _emhist[s] + deg_delta[s].first - 1,
                                   _emhist[s] + deg_delta[s].first);
                S_a += lbinom_fast(_r_count[s] + r_count_delta[s] + _ephist[s] + deg_delta[s].second - 1,
                                   _ephist[s] + deg_delta[s].second);
            }
        }

        if (bv != n_bv)
        {
            if (n_bv_count == 0)
            {
                for (auto s : n_bv)
                    r_count_delta[s] -= 1;
            }

            if (bv_count == 1)
            {
                for (auto s : bv)
                   r_count_delta[s] += 1;
            }
        }

        if (r != nr)
        {
            size_t kin = (in_deg + out_deg == 0) ? in_degreeS()(v, g) : in_deg;
            size_t kout = (in_deg + out_deg == 0) ? out_degreeS()(v, g) : out_deg;

            auto& d_r = deg_delta[r];
            d_r.first += kin;
            d_r.second += kout;

            auto& d_nr = deg_delta[nr];
            d_nr.first -= kin;
            d_nr.second -= kout;
        }

        return S_a - S_b;
    }

    template <class Graph>
    void move_vertex(size_t v, size_t r, size_t nr, bool, Graph& g,
                     size_t in_deg = 0, size_t out_deg = 0)
    {
        if (r == nr)
            return;

        r = get_r(r);
        nr = get_r(nr);

        auto u =_overlap_stats.get_node(v);
        u = get_v(u);
        auto& bv = _bvs[u];
        assert(!bv.empty());
        bv_t n_bv;
        cdeg_t& deg = _degs[u];
        cdeg_t n_deg;
        size_t d = bv.size();

        bool is_same_bv = get_n_bv(v, r, nr, bv, deg, n_bv, n_deg, g, in_deg,
                                   out_deg);
        assert(!n_bv.empty());
        size_t n_d = n_bv.size();

        if (!is_same_bv)
        {
            _dhist[d] -= 1;
            auto& bv_count = _bhist[bv];
            bv_count -= 1;

            if (bv_count == 0)
            {
                _bhist.erase(bv);
                for (auto s : bv)
                {
                    _r_count[s]--;
                    if (_r_count[s] == 0)
                        _actual_B--;
                }
            }

            if (d == _D && _dhist[d] == 0 && _D > 1)
            {
                _D--;
                while (_dhist[_D] == 0)
                {
                    if (_D == 0)
                        break;
                    _D--;
                }
            }

            _dhist[n_d] += 1;
            auto& n_bv_count = _bhist[n_bv];
            n_bv_count += 1;

            if (n_bv_count == 1)
            {
                for (auto s : n_bv)
                {
                    if (_r_count[s] == 0)
                        _actual_B++;
                    _r_count[s]++;
                }
            }

            if (n_d > _D)
                _D = n_d;
        }

        auto& deg_h = _deg_hist[bv];
        auto& deg_count = deg_h[deg];
        deg_count -= 1;
        if (deg_count == 0)
            deg_h.erase(deg);
        auto& bmh = _embhist[bv];
        auto& bph = _epbhist[bv];
        assert(bmh.size() == bv.size());
        assert(bph.size() == bv.size());
        for (size_t i = 0; i < bv.size(); ++i)
        {
            bmh[i] -= get<0>(deg[i]);
            bph[i] -= get<1>(deg[i]);
        }

        if (deg_h.empty())
        {
            _deg_hist.erase(bv);
            _embhist.erase(bv);
            _epbhist.erase(bv);
        }

        size_t kin = (in_deg + out_deg == 0) ? in_degreeS()(v, g) : in_deg;
        size_t kout = (in_deg + out_deg == 0) ? out_degreeS()(v, g) : out_deg;
        _emhist[r] -= kin;
        _ephist[r] -= kout;

        auto& hist = _deg_hist[n_bv];
        hist[n_deg] += 1;
        auto& n_bmh = _embhist[n_bv];
        auto& n_bph = _epbhist[n_bv];
        n_bmh.resize(n_bv.size());
        n_bph.resize(n_bv.size());
        for (size_t i = 0; i < n_bv.size(); ++i)
        {
            n_bmh[i] += get<0>(n_deg[i]);
            n_bph[i] += get<1>(n_deg[i]);
        }

        _emhist[nr] += kin;
        _ephist[nr] += kout;

        _bvs[u].swap(n_bv);
        _degs[u].swap(n_deg);
        assert(_bvs[u].size() > 0);

    }

    size_t get_actual_B()
    {
        return _actual_B;
    }

    void add_block()
    {
        _total_B++;
    }

private:
    overlap_stats_t& _overlap_stats;
    vector<size_t>& _bmap;
    vector<size_t>& _vmap;
    size_t _N;
    size_t _E;
    size_t _actual_B;
    size_t _total_B;
    size_t _D;
    bool _allow_empty;
    bool _directed;
    vector<int> _dhist;        // d-histogram
    vector<int> _r_count;      // m_r
    bhist_t _bhist;            // b-histogram
    vector<size_t> _emhist;    // e-_r histogram
    vector<size_t> _ephist;    // e+_r histogram
    ebhist_t _embhist;         // e+^r_b histogram
    ebhist_t _epbhist;         // e+^r_b histogram
    deg_hist_t _deg_hist;      // n_k^b histogram
    vector<bv_t> _bvs;         // bv node map
    vector<cdeg_t> _degs;      // deg node map
};

} // namespace graph_tool

#endif // GRAPH_BLOCKMODEL_OVERLAP_PARTITION_HH
