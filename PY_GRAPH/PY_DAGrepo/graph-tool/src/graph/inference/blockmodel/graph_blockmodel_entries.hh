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

#ifndef GRAPH_BLOCKMODEL_ENTRIES_HH
#define GRAPH_BLOCKMODEL_ENTRIES_HH


namespace std
{
template <class T, class V>
void operator+=(vector<T>& ret, const V& v)
{
    ret.resize(max(ret.size(), v.size()));
    for (size_t i = 0; i < v.size(); ++i)
        ret[i] += v[i];
}

template <class T, class V>
void operator-=(vector<T>& ret, const V& v)
{
    ret.resize(max(ret.size(), v.size()));
    for (size_t i = 0; i < v.size(); ++i)
        ret[i] -= v[i];
}

template <class T1, class T2>
void operator*=(vector<T1>& ret, const T2& v)
{
    for (auto& x : ret)
        x *= v;
}

template <class T1, class T2>
void operator/=(vector<T1>& ret, const T2& v)
{
    for (auto& x : ret)
        x /= v;
}
}

namespace graph_tool
{

template <class PMap>
class VAdapter
{
public:
    typedef typename boost::property_traits<PMap>::key_type key_t;
    typedef typename boost::property_traits<PMap>::value_type val_t;
    VAdapter(std::vector<PMap>& v, const key_t& e)
        : _v(v), _e(e) {}

    size_t size() const { return _v.size(); }
    val_t& operator[](size_t i) { return _v[i][_e]; }
    const val_t& operator[](size_t i) const { return _v[i][_e]; }

    std::vector<PMap>& _v;
    const key_t& _e;
};

template <class PMap>
VAdapter<PMap> make_vadapter(std::vector<PMap>& v,
                             const typename VAdapter<PMap>::key_t& e)
{
    return VAdapter<PMap>(v, e);
}

// tuple utils
template <size_t i, class T, class OP>
void tuple_op_imp(T&, OP&&)
{
}

template <size_t i, class T, class OP, class Ti, class... Ts>
void tuple_op_imp(T& tuple, OP&& op, Ti&& v, Ts&&... vals)
{
    op(get<i>(tuple), v);
    tuple_op_imp<i+1>(tuple, op, vals...);
}

template <class OP, class T, class... Ts>
__attribute__((flatten))
void tuple_op(T& tuple, OP&& op, Ts&&... vals)
{
    tuple_op_imp<0>(tuple, op, vals...);
}

namespace detail {
   template <class F, class Tuple, std::size_t... I>
   constexpr decltype(auto) tuple_apply_impl(F&& f, Tuple&& t,
                                             std::index_sequence<I...>)
   {
       return f(std::get<I>(std::forward<Tuple>(t))...);
   }
} // namespace detail

template <class F, class Tuple>
constexpr decltype(auto) tuple_apply(F&& f, Tuple&& t)
{
    return detail::tuple_apply_impl
        (std::forward<F>(f), std::forward<Tuple>(t),
         std::make_index_sequence<std::tuple_size<std::decay_t<Tuple>>{}>{});
}

// Manage a set of block pairs and corresponding edge counts that will be
// updated

template <class Graph, class BGraph, class... EVals>
class EntrySet
{
public:
    typedef typename graph_traits<BGraph>::edge_descriptor bedge_t;

    EntrySet(size_t B)
        : _dummy(_null)
    {
        _r_out_field.resize(B, _null);
        _nr_out_field.resize(B, _null);
        _r_in_field.resize(B, _null);
        _nr_in_field.resize(B, _null);
    }

    void set_move(size_t r, size_t nr, size_t B)
    {
        clear();
        _rnr = make_pair(r, nr);
        if (B > _r_out_field.size())
        {
            _r_out_field.resize(B, _null);
            _nr_out_field.resize(B, _null);
            _r_in_field.resize(B, _null);
            _nr_in_field.resize(B, _null);
        }
    }

    size_t& get_field(size_t s, size_t t)
    {
        if (!is_directed::apply<Graph>::type::value && s > t)
            std::swap(s, t);

        if (s == _rnr.first)
            return _r_out_field[t];
        else if (s == _rnr.second)
            return _nr_out_field[t];
        else if (t == _rnr.first)
            return _r_in_field[s];
        else if (t == _rnr.second)
            return _nr_in_field[s];
        else
            return _dummy;
    }

    template <bool Add, class... DVals>
    __attribute__((flatten))
    void insert_delta(size_t s, size_t t, DVals&&... delta)
    {
        auto& f = get_field(s, t);
        if (f == _null)
        {
            f = _entries.size();
            _entries.emplace_back(s, t);
            _delta.emplace_back();
        }

        if (Add)
            tuple_op(_delta[f], [&](auto& r, auto& v){ r += v; },
                     delta...);
        else
            tuple_op(_delta[f], [&](auto& r, auto& v){ r -= v; },
                     delta...);
    }

    const auto& get_delta(size_t r, size_t s)
    {
        size_t f = get_field(r, s);
        if (f == _null)
            return _null_delta;
        return _delta[f];
    }

    void clear()
    {
        for (const auto& rs : _entries)
        {
            size_t r = rs.first;
            size_t s = rs.second;
            auto& f = get_field(r, s);
            f = _null;
        }
        _entries.clear();
        _delta.clear();
        _mes.clear();
        _recs_entries.clear();
    }

    const vector<pair<size_t, size_t> >& get_entries() { return _entries; }
    const vector<std::tuple<EVals...>>& get_delta() { return _delta; }

    template <class Emat>
    vector<bedge_t>& get_mes(Emat& emat)
    {
        _mes.reserve(_entries.size());
        for (size_t i = _mes.size(); i < _entries.size(); ++i)
        {
            auto& rs = _entries[i];
            _mes.push_back(emat.get_me(rs.first, rs.second));
            assert(_mes.back() != emat.get_null_edge() || get<0>(_delta[i]) >= 0);
        }
        return _mes;
    }

    template <class Emat>
    const bedge_t& get_me(size_t r, size_t s, Emat& emat)
    {
        size_t field = get_field(r, s);
        if (field >= _mes.size())
            return emat.get_me(r, s);
        return _mes[field];
    }

    std::tuple<EVals...> _self_weight;

    std::vector<std::tuple<size_t, size_t,
                           GraphInterface::edge_t, int, std::vector<double>>>
        _recs_entries;

private:
    static constexpr size_t _null = numeric_limits<size_t>::max();
    static const std::tuple<EVals...> _null_delta;

    pair<size_t, size_t> _rnr;
    vector<size_t> _r_out_field;
    vector<size_t> _r_in_field;
    vector<size_t> _nr_out_field;
    vector<size_t> _nr_in_field;
    vector<pair<size_t, size_t>> _entries;
    vector<std::tuple<EVals...>> _delta;
    vector<bedge_t> _mes;
    size_t _dummy;

};

template <class Graph, class BGraph, class... EVals>
constexpr size_t EntrySet<Graph, BGraph, EVals...>::_null;

template <class Graph, class BGraph, class... EVals>
const std::tuple<EVals...> EntrySet<Graph, BGraph, EVals...>::_null_delta;

struct is_loop_nop
{
    bool operator()(size_t) const { return false; }
};

template <bool Add, class Vertex, class Graph, class Vprop,
          class Eprop, class MEntries, class Efilt, class IL, class... Eprops>
__attribute__((flatten))
void modify_entries(Vertex v, Vertex r, Vprop& _b, Graph& g, Eprop& eweights,
                    MEntries& m_entries, Efilt&& efilt, IL&& is_loop,
                    Eprops&... eprops)
{
    typedef typename graph_traits<Graph>::vertex_descriptor vertex_t;
    auto& self_weight = m_entries._self_weight;
    if (!is_directed::apply<Graph>::type::value)
    {
        tuple_apply([&](auto&&... vals)
                    {
                        auto op = [](auto& x) -> auto& { x *= 0; return x; };
                        auto f = [](auto&...) {};
                        f(op(vals)...);
                    }, self_weight);
    }

    for (auto e : out_edges_range(v, g))
    {
        if (efilt(e))
            continue;
        vertex_t u = target(e, g);
        vertex_t s = _b[u];
        int ew = eweights[e];
        //assert(ew > 0);

        if (Add && u == v)
            s = r;

        m_entries.template insert_delta<Add>(r, s, ew,
                                             make_vadapter(eprops, e)...);

        if ((u == v || is_loop(v)) && !is_directed::apply<Graph>::type::value)
            tuple_op(self_weight, [&](auto& r, auto& v){ r += v; },
                     ew, make_vadapter(eprops, e)...);
    }

    if (get<0>(self_weight) > 0 && get<0>(self_weight) % 2 == 0 &&
        !is_directed::apply<Graph>::type::value)
    {
        tuple_apply([&](auto&&... vals)
                    {
                        auto op = [](auto& x) -> auto& { x /= 2; return x; };
                        m_entries.template insert_delta<!Add>(r, r,
                                                              op(vals)...);
                    }, self_weight);
    }

    for (auto e : in_edges_range(v, g))
    {
        if (efilt(e))
            continue;
        vertex_t u = source(e, g);
        if (u == v)
            continue;
        vertex_t s = _b[u];
        int ew = eweights[e];

        m_entries.template insert_delta<Add>(s, r, ew,
                                             make_vadapter(eprops, e)...);
    }
}

// obtain the necessary entries in the e_rs matrix which need to be modified
// after the move
template <class Graph, class Vertex, class VProp, class Eprop,
          class MEntries, class EFilt, class IL, class... Eprops>
void move_entries(Vertex v, size_t r, size_t nr, VProp& _b, Graph& g,
                  Eprop& eweights, size_t B, MEntries& m_entries,
                  EFilt&& efilt, IL&& is_loop, Eprops&... eprops)
{
    m_entries.set_move(r, nr, B);

    if (r != null_group)
        modify_entries<false>(v, r, _b, g, eweights, m_entries,
                              std::forward<EFilt>(efilt),
                              std::forward<IL>(is_loop), eprops...);
    if (nr != null_group)
        modify_entries<true>(v, nr, _b, g, eweights, m_entries,
                             std::forward<EFilt>(efilt),
                             std::forward<IL>(is_loop), eprops...);
}


// operation on a set of entries
template <class MEntries, class EMat, class OP>
void entries_op(MEntries& m_entries, EMat& emat, OP&& op)
{
    const auto& entries = m_entries.get_entries();
    const auto& delta = m_entries.get_delta();
    auto& mes = m_entries.get_mes(emat);

    for (size_t i = 0; i < entries.size(); ++i)
    {
        auto& entry = entries[i];
        auto er = entry.first;
        auto es = entry.second;
        op(er, es, mes[i], delta[i]);
    }
}

// obtain the entropy difference given a set of entries in the e_rs matrix
template <bool exact, class MEntries, class Eprop, class EMat, class BGraph>
double entries_dS(MEntries& m_entries, Eprop& mrs, EMat& emat, BGraph& bg)
{
    double dS = 0;
    entries_op(m_entries, emat,
               [&](auto r, auto s, auto& me, auto& delta)
               {
                   size_t ers = 0;
                   if (me != emat.get_null_edge())
                       ers = mrs[me];
                   int d = get<0>(delta);
                   assert(int(ers) + d >= 0);
                   if (exact)
                       dS += eterm_exact(r, s, ers + d, bg) - eterm_exact(r, s, ers, bg);
                   else
                       dS += eterm(r, s, ers + d, bg) - eterm(r, s, ers, bg);
               });
    return dS;
}

} // namespace graph_tool

#endif // GRAPH_BLOCKMODEL_ENTRIES_HH
