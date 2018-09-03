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

#ifndef GRAPH_BLOCKMODEL_UTIL_HH
#define GRAPH_BLOCKMODEL_UTIL_HH

#include "config.h"

#include "graph_blockmodel_entropy.hh"
#include "graph_blockmodel_partition.hh"
#include "graph_blockmodel_entries.hh"
#include "graph_blockmodel_emat.hh"
#include "graph_blockmodel_elist.hh"
#include "graph_blockmodel_weights.hh"
#include "../support/graph_neighbor_sampler.hh"

namespace graph_tool
{

class BlockStateVirtualBase {
public:
    virtual void add_partition_node(size_t v, size_t r) = 0;
    virtual void remove_partition_node(size_t v, size_t r) = 0;
    virtual void set_vertex_weight(size_t v, int w) = 0;
    virtual void coupled_resize_vertex(size_t v) = 0;
    virtual double virtual_move(size_t v, size_t r, size_t nr,
                                entropy_args_t eargs) = 0;
    virtual size_t add_block() = 0;
    virtual void add_edge(const GraphInterface::edge_t& e) = 0;
    virtual void remove_edge(const GraphInterface::edge_t& e) = 0;
    virtual void update_edge(const GraphInterface::edge_t& e,
                             const std::vector<double>& delta) = 0;
    virtual double recs_dS(size_t, size_t,
                           const std::vector<std::tuple<size_t, size_t,
                                             GraphInterface::edge_t, int,
                                             std::vector<double>>>&,
                           std::vector<double>&, int) = 0;
    virtual bool check_edge_counts(bool emat=true) = 0;
};



} // graph_tool namespace

#endif //GRAPH_BLOCKMODEL_UTIL_HH
