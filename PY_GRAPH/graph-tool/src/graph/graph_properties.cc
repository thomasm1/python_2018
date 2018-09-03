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

#include "graph_python_interface.hh"
#include "graph.hh"
#include "graph_properties.hh"
#include "graph_filtering.hh"
#include "graph_selectors.hh"
#include "graph_util.hh"
#include "hash_map_wrap.hh"

#include <boost/mpl/for_each.hpp>

#include <boost/python/extract.hpp>

using namespace std;
using namespace boost;
using namespace graph_tool;

namespace graph_tool
{

// global property types' names
const char* type_names[] =
    {"bool", "int16_t", "int32_t", "int64_t", "double", "long double",
     "string", "vector<bool>", "vector<int16_t>", "vector<int32_t>",
     "vector<int64_t>", "vector<double>", "vector<long double>",
     "vector<string>", "python::object"};


struct do_shift_vertex_property
{
    template <class PropertyMap, class Vec>
    void operator()(PropertyMap, const GraphInterface::multigraph_t& g,
                    boost::any map, const Vec& vi, bool& found) const
    {
        try
        {
            PropertyMap pmap = any_cast<PropertyMap>(map);
            size_t back = num_vertices(g) - 1;
            for (auto v : vi)
            {
                for (size_t i = v; i < back; ++i)
                    pmap[vertex(i, g)] = pmap[vertex(i + 1, g)];
                back--;
            }
            found = true;
        }
        catch (bad_any_cast&) {}
    }
};

// this function will shift all the properties when a vertex is to be deleted
void GraphInterface::shift_vertex_property(boost::any prop, python::object oindex) const
{
    boost::multi_array_ref<int64_t,1> index = get_array<int64_t,1>(oindex);
    bool found = false;
    mpl::for_each<writable_vertex_properties>
        (std::bind(do_shift_vertex_property(), std::placeholders::_1,
                   std::ref(*_mg), prop, index, std::ref(found)));
    if (!found)
        throw GraphException("invalid writable property map");
}

struct do_move_vertex_property
{
    template <class PropertyMap, class Vec>
    void operator()(PropertyMap, const GraphInterface::multigraph_t& g,
                    boost::any map, const Vec& vi, size_t back,
                    bool& found) const
    {
        try
        {
            PropertyMap pmap = any_cast<PropertyMap>(map);
            for (auto v : vi)
            {
                pmap[vertex(v, g)] = pmap[vertex(back, g)];
                back--;
            }
            found = true;
        }
        catch (bad_any_cast&) {}
    }
};

// this function will move the back of the property map when a vertex in the middle is to be deleted
void GraphInterface::move_vertex_property(boost::any prop, python::object oindex) const
{
    boost::multi_array_ref<int64_t,1> index = get_array<int64_t,1>(oindex);
    size_t back = num_vertices(*_mg) - 1;
    bool found = false;
    mpl::for_each<writable_vertex_properties>
        (std::bind(do_move_vertex_property(), std::placeholders::_1, std::ref(*_mg),
                   prop, index, back, std::ref(found)));
    if (!found)
        throw GraphException("invalid writable property map");
}


struct reindex_vertex_property
{
    template <class PropertyMap, class IndexMap>
    void operator()(PropertyMap, const GraphInterface::multigraph_t& g,
                    boost::any map, IndexMap old_index, bool& found) const
    {
        try
        {
            PropertyMap pmap = any_cast<PropertyMap>(map);
            for (size_t i = 0; i < num_vertices(g); ++i)
            {
                GraphInterface::vertex_t v = vertex(i, g);
                if (old_index[v] != int(i))
                    pmap[v] = pmap[vertex(old_index[v], g)];
            }
            found = true;
        }
        catch (bad_any_cast&) {}
    }
};


void GraphInterface::re_index_vertex_property(boost::any map,
                                              boost::any aold_index) const
{
    typedef vprop_map_t<int64_t>::type index_prop_t;
    index_prop_t old_index = any_cast<index_prop_t>(aold_index);

    bool found = false;
    mpl::for_each<writable_vertex_properties>
        (std::bind(reindex_vertex_property(), std::placeholders::_1, std::ref(*_mg),
                   map, old_index, std::ref(found)));
    if (!found)
        throw GraphException("invalid writable property map");

}

} // graph_tool namespace


struct do_infect_vertex_property
{
    template <class Graph, class IndexMap, class PropertyMap>
    void operator()(Graph& g, IndexMap index, PropertyMap prop,
                    boost::python::object oval) const
    {
        typedef typename property_traits<PropertyMap>::value_type val_t;
        bool all = false;

        std::unordered_set<val_t> vals;
        if (oval == boost::python::object())
        {
            all = true;
        }
        else
        {
            for (int i = 0; i < len(oval); ++i)
            {
                val_t val = boost::python::extract<val_t>(oval[i]);
                vals.insert(val);
            }
        }

        unchecked_vector_property_map<bool, IndexMap>
            marked(index, num_vertices(g));

        PropertyMap temp(index, num_vertices(g));

        parallel_vertex_loop
            (g,
             [&](auto v)
             {
                 if (!all && vals.find(prop[v]) == vals.end())
                     return;
                 for (auto a : adjacent_vertices_range(v, g))
                 {
                     if (prop[a] == prop[v])
                         continue;
                     marked[a] = true;
                     temp[a] = prop[v];
                 }
             });

        parallel_vertex_loop
            (g,
             [&](auto v)
             {
                 if (marked[v])
                     prop[v] = temp[v];
             });
    }
};

void infect_vertex_property(GraphInterface& gi, boost::any prop,
                            boost::python::object val)
{
        run_action<>()(gi, std::bind(do_infect_vertex_property(), std::placeholders::_1,
                                     gi.get_vertex_index(), std::placeholders::_2, val),
                   writable_vertex_properties())(prop);
}

template <class Value>
vector<Value> operator-(const vector<Value>& a, const vector<Value>& b)
{
    vector<Value> c(a);
    c.resize(max(a.size(), b.size()), Value(0));
    for (size_t i = 0; i < b.size(); ++i)
        c[i] = a[i] - b[i];
    return c;
}

struct do_mark_edges
{
    template <class Graph, class EdgePropertyMap>
    void operator()(Graph& g, EdgePropertyMap prop) const
    {
        parallel_edge_loop
            (g,
             [&](auto e)
             {
                 prop[e] = true;
             });
    }
};

void mark_edges(GraphInterface& gi, boost::any prop)
{
    run_action<>()
        (gi, bind<void>(do_mark_edges(), _1, _2),
         writable_edge_scalar_properties())(prop);
}
