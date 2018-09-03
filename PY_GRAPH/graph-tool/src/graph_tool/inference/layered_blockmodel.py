#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# graph_tool -- a general graph manipulation python module
#
# Copyright (C) 2006-2017 Tiago de Paula Peixoto <tiago@skewed.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division, absolute_import, print_function
import sys
if sys.version_info < (3,):
    range = xrange

from .. import _degree, _prop, Graph, GraphView, libcore, _get_rng, PropertyMap, \
    conv_pickle_state
import random
from numpy import *
import numpy
from collections import defaultdict
from scipy.special import gammaln
import copy
import warnings

from .. import group_vector_property, ungroup_vector_property, Vector_size_t, \
    perfect_prop_hash

from .. decorators import _wraps

from .. dl_import import dl_import
dl_import("from . import libgraph_tool_inference as libinference")

from .. generation import graph_union
from .. stats import vertex_hist

from . blockmodel import *
from . blockmodel import _bm_test
from . overlap_blockmodel import *

class LayeredBlockState(OverlapBlockState, BlockState):
    r"""The (possibly overlapping) block state of a given graph, where the edges are
    divided into discrete layers.

    Parameters
    ----------
    g : :class:`~graph_tool.Graph`
        Graph to be modelled.
    ec : :class:`~graph_tool.PropertyMap` Edge :class:`~graph_tool.PropertyMap`
        containing discrete edge covariates that will split the network in
        discrete layers.
    recs : list of :class:`~graph_tool.PropertyMap` instances (optional, default: ``[]``)
        List of real or discrete-valued edge covariates.
    rec_types : list of edge covariate types (optional, default: ``[]``)
        List of types of edge covariates. The possible types are:
        ``"real-exponential"``, ``"real-normal"``, ``"discrete-geometric"``,
        ``"discrete-poisson"`` or ``"discrete-binomial"``.
    rec_params : list of ``dict`` (optional, default: ``[]``)
        Model hyperparameters for edge covariates. This should a list of
        ``dict`` instances. See :class:`~graph_tool.inference.BlockState` for
        more details.
    eweight : :class:`~graph_tool.PropertyMap` (optional, default: ``None``)
        Edge multiplicities (for multigraphs or block graphs).
    vweight : :class:`~graph_tool.PropertyMap` (optional, default: ``None``)
        Vertex multiplicities (for block graphs).
    b : :class:`~graph_tool.PropertyMap` or :class:`numpy.ndarray` (optional, default: ``None``)
        Initial block labels on the vertices or half-edges. If not supplied, it
        will be randomly sampled.
    B : ``int`` (optional, default: ``None``)
        Number of blocks (or vertex groups). If not supplied it will be obtained
        from the parameter ``b``.
    clabel : :class:`~graph_tool.PropertyMap` (optional, default: ``None``)
        Constraint labels on the vertices. If supplied, vertices with different
        label values will not be clustered in the same group.
    pclabel : :class:`~graph_tool.PropertyMap` (optional, default: ``None``)
        Partition constraint labels on the vertices. This has the same
        interpretation as ``clabel``, but will be used to compute the partition
        description length.
    layers : ``bool`` (optional, default: ``False``)
        If ``layers == True``, the "independent layers" version of the model is
        used, instead of the "edge covariates" version.
    deg_corr : ``bool`` (optional, default: ``True``)
        If ``True``, the degree-corrected version of the blockmodel ensemble will
        be assumed, otherwise the traditional variant will be used.
    overlap : ``bool`` (optional, default: ``False``)
        If ``True``, the overlapping version of the model will be used.
    allow_empty : ``bool`` (optional, default: ``True``)
        If ``True``, partition description length computed will allow for empty
        groups.
    max_BE : ``int`` (optional, default: ``1000``)
        If the number of blocks exceeds this value, a sparse matrix is used for
        the block graph. Otherwise a dense matrix will be used.
    """

    def __init__(self, g, ec, eweight=None, vweight=None, recs=[], rec_types=[],
                 rec_params=[], b=None, B=None, clabel=None, pclabel=False,
                 layers=False, deg_corr=True, overlap=False, allow_empty=False,
                 **kwargs):

        kwargs = kwargs.copy()

        self.g = g

        if kwargs.pop("ec_done", False) or ec is None:
            self.ec = ec
        else:
            self.ec = ec = perfect_prop_hash([ec], "int32_t")[0]

        if ec is not None:
            self.C = ec.fa.max() + 1
        else:
            self.C = len(kwargs.get("gs"))
        self.layers = layers

        if "max_BE" in kwargs:
            del kwargs["max_BE"]
        max_BE = 0

        if vweight is None:
            vweight = g.new_vp("int", 1)

        if eweight is None:
            eweight = g.new_ep("int", 1)

        self.Lrecdx = kwargs.pop("Lrecdx", [])
        while len(self.Lrecdx) < self.C + 1:
            self.Lrecdx.append(libcore.Vector_double(1))
            self.Lrecdx[-1][0] = -1

        if not overlap:
            kwargs = dmask(kwargs, ["base_g", "node_index", "eindex",
                                    "half_edges"])
            ldegs = kwargs.pop("degs", None)
            if ldegs is not None:
                tdegs = libinference.get_mapped_block_degs(self.g._Graph__graph,
                                                           ldegs, 0,
                                                           _prop("v", self.g,
                                                                 self.g.vertex_index.copy("int")))
            else:
                tdegs = None

            agg_state = BlockState(g, b=b, B=B,
                                   eweight=eweight, vweight=vweight, recs=recs,
                                   rec_types=rec_types, rec_params=rec_params,
                                   clabel=clabel, pclabel=pclabel,
                                   deg_corr=deg_corr, allow_empty=allow_empty,
                                   max_BE=max_BE, degs=tdegs,
                                   Lrecdx=self.Lrecdx[0],
                                   **dmask(kwargs, ["degs", "lweights", "gs"]))
        else:
            kwargs = dmask(kwargs, ["degs"])
            ldegs = None
            agg_state = OverlapBlockState(g, b=b, B=B, recs=recs,
                                          rec_types=rec_types,
                                          rec_params=rec_params, clabel=clabel,
                                          pclabel=pclabel, deg_corr=deg_corr,
                                          allow_empty=allow_empty, max_BE=max_BE,
                                          Lrecdx=self.Lrecdx[0],
                                          **dmask(kwargs, ["degs", "lweights",
                                                           "gs"]))
            self.base_g = agg_state.base_g
            self.g = agg_state.g
            eweight = self.g.new_ep("int", 1)
            vweight = self.g.new_vp("int", 1)
            kwargs = dmask(kwargs, ["base_g", "node_index", "eindex",
                                    "half_edges"])

        self.agg_state = agg_state

        if overlap and self.ec is not None:
            self.base_ec = self.base_g.own_property(ec.copy())
            ec = agg_state.eindex.copy()
            pmap(ec, self.ec)
            self.ec = ec.copy("int")

        self.eweight = eweight
        self.vweight = vweight
        if not overlap:
            self.is_weighted = agg_state.is_weighted
        else:
            self.is_weighted = False

        self.allow_empty = agg_state.allow_empty

        self.rec = agg_state.rec
        self.drec = agg_state.drec
        self.rec_types = agg_state.rec_types
        self.rec_params = agg_state.rec_params
        self.epsilon = agg_state.epsilon

        self.b = agg_state.b
        self.B = agg_state.B
        self.clabel = agg_state.clabel
        self.pclabel = agg_state.pclabel
        self.bclabel = agg_state.bclabel

        self.deg_corr = deg_corr
        self.overlap = overlap

        self.vc = self.g.new_vp("vector<int>")
        self.vmap = self.g.new_vp("vector<int>")

        self.gs = kwargs.pop("gs", [])
        self.block_map = libinference.bmap_t()
        lweights = kwargs.pop("lweights", self.g.new_vp("vector<int>"))

        if len(self.gs) == 0:
            for l in range(0, self.C):
                u = Graph(directed=g.is_directed())
                u.vp["b"] = u.new_vp("int")
                u.vp["weight"] = u.new_vp("int")
                u.ep["weight"] = u.new_ep("int")
                u.gp["rec"] = u.new_gp("object", val=[u.new_ep("double") for i in range(len(self.rec))])
                u.gp["drec"] = u.new_gp("object", val=[u.new_ep("double") for i in range(len(self.drec))])
                u.vp["brmap"] = u.new_vp("int")
                u.vp["vmap"] = u.new_vp("int")
                self.gs.append(u)

            libinference.split_layers(self.g._Graph__graph,
                                      _prop("e", self.g, self.ec),
                                      _prop("v", self.g, self.b),
                                      [_prop("e", self.g, x) for x in self.rec],
                                      [_prop("e", self.g, x) for x in self.drec],
                                      _prop("e", self.g, self.eweight),
                                      _prop("v", self.g, self.vweight),
                                      _prop("v", self.g, self.vc),
                                      _prop("v", self.g, self.vmap),
                                      _prop("v", self.g, lweights),
                                      [u._Graph__graph for u in self.gs],
                                      [_prop("v", u, u.vp["b"]) for u in self.gs],
                                      [[_prop("e", u, x) for x in u.gp["rec"]] for u in self.gs],
                                      [[_prop("e", u, x) for x in u.gp["drec"]] for u in self.gs],
                                      [_prop("e", u, u.ep["weight"]) for u in self.gs],
                                      [_prop("v", u, u.vp["weight"]) for u in self.gs],
                                      self.block_map,
                                      [_prop("v", u, u.vp["brmap"]) for u in self.gs],
                                      [_prop("v", u, u.vp["vmap"]) for u in self.gs])
        else:
            libinference.split_groups(_prop("v", self.g, self.b),
                                      _prop("v", self.g, self.vc),
                                      _prop("v", self.g, self.vmap),
                                      [u._Graph__graph for u in self.gs],
                                      [_prop("v", u, u.vp["b"]) for u in self.gs],
                                      [_prop("v", u, u.vp["weight"]) for u in self.gs],
                                      self.block_map,
                                      [_prop("v", u, u.vp["brmap"]) for u in self.gs],
                                      [_prop("v", u, u.vp["vmap"]) for u in self.gs])

        if self.g.get_vertex_filter()[0] is not None:
            for u in self.gs:
                u.set_vertex_filter(u.new_vp("bool", True))

        self.master = not self.layers

        if not overlap:
            self.degs = agg_state.degs
            self.merge_map = agg_state.merge_map

        self.layer_states = []

        self.max_BE = max_BE
        self.bg = agg_state.bg
        self.wr = agg_state.wr
        self.mrs = agg_state.mrs
        self.mrp = agg_state.mrp
        self.mrm = agg_state.mrm
        self.brec = agg_state.brec
        self.bdrec = agg_state.bdrec
        self.rec_params = agg_state.rec_params
        self.wparams = agg_state.wparams
        self.epsilon = agg_state.epsilon
        self._entropy_args = agg_state._entropy_args
        self.recdx = agg_state.recdx
        if not self.overlap:
            self.empty_blocks = agg_state.empty_blocks
            self.empty_pos = agg_state.empty_pos

        self._coupled_state = None

        for l, u in enumerate(self.gs):
            state = self.__gen_state(l, u, ldegs)
            self.layer_states.append(state)

        if ec is None:
            self.ec = self.g.new_ep("int")

        if not self.overlap:
            self._state = \
                libinference.make_layered_block_state(agg_state._state,
                                                      self)
        else:
            self._state = \
                libinference.make_layered_overlap_block_state(agg_state._state,
                                                              self)
        if ec is None:
            self.ec = None

        if _bm_test():
            assert self.mrs.fa.sum() == self.eweight.fa.sum(), "inconsistent mrs!"

        kwargs.pop("recs", None)
        kwargs.pop("drec", None)
        kwargs.pop("rec_params", None)
        kwargs.pop("Lrecdx", None)
        kwargs.pop("epsilon", None)

        if len(kwargs) > 0:
            warnings.warn("unrecognized keyword arguments: " +
                          str(list(kwargs.keys())))

    def get_N(self):
        r"Returns the total number of edges."
        return self.agg_state.get_N()

    def get_E(self):
        r"Returns the total number of nodes."
        return self.agg_state.get_E()

    def get_B(self):
        r"Returns the total number of blocks."
        return self.agg_state.get_B()

    def get_nonempty_B(self):
        r"Returns the total number of nonempty blocks."
        return self.agg_state.get_nonempty_B()

    def __get_base_u(self, u):
        node_index = u.vp["vmap"].copy("int64_t")
        pmap(node_index, self.agg_state.node_index)
        base_u, nindex, vcount, ecount = \
            condensation_graph(u, node_index,
                               self_loops=True,
                               parallel_edges=True)[:4]
        rindex = zeros(nindex.a.max() + 1, dtype="int64")
        reverse_map(nindex, rindex)
        pmap(node_index, rindex)
        base_u.vp["vmap"] = nindex
        return base_u, node_index

    def __gen_state(self, l, u, ldegs):
        B = u.num_vertices() + 1
        if not self.overlap:
            if ldegs is not None:
                degs = libinference.get_mapped_block_degs(u._Graph__graph,
                                                          ldegs, l + 1,
                                                           _prop("v", u,
                                                                 u.vp.vmap))
            else:
                degs = None
            state = BlockState(u, b=u.vp["b"],
                               B=B,
                               recs=u.gp["rec"],
                               drec=u.gp["drec"],
                               rec_types=self.rec_types,
                               rec_params=self.rec_params,
                               epsilon=self.epsilon,
                               Lrecdx=self.Lrecdx[l+1],
                               eweight=u.ep["weight"],
                               vweight=u.vp["weight"],
                               deg_corr=self.deg_corr,
                               degs=degs,
                               allow_empty=self.allow_empty,
                               max_BE=self.max_BE)
        else:
            base_u, node_index = self.__get_base_u(u)
            state = OverlapBlockState(u, b=u.vp["b"].fa,
                                      B=B,
                                      recs=u.gp["rec"],
                                      drec=u.gp["drec"],
                                      rec_types=self.rec_types,
                                      rec_params=self.rec_params,
                                      epsilon=self.epsilon,
                                      Lrecdx=self.Lrecdx[l+1],
                                      node_index=node_index,
                                      base_g=base_u,
                                      deg_corr=self.deg_corr,
                                      max_BE=self.max_BE)
        state.block_rmap = u.vp["brmap"]
        state.vmap = u.vp["vmap"]
        state.free_blocks = Vector_size_t()
        return state

    def __getstate__(self):
        state = dict(g=self.g,
                     ec=self.ec,
                     recs=self.rec,
                     drec=self.drec,
                     rec_types=self.rec_types,
                     rec_params=self.rec_params,
                     layers=self.layers,
                     eweight=self.eweight,
                     vweight=self.vweight,
                     b=self.b,
                     B=self.B,
                     clabel=self.clabel,
                     deg_corr=self.deg_corr,
                     allow_empty=self.allow_empty)
        return state

    def __setstate__(self, state):
        conv_pickle_state(state)
        self.__init__(**state)

    def __copy__(self):
        return self.copy()

    def __deepcopy__(self, memo):
        g = copy.deepcopy(self.g, memo)
        ec = g.own_property(copy.deepcopy(self.ec, memo))
        return self.copy(g=g, ec=ec)

    def copy(self, g=None, eweight=None, vweight=None, b=None, B=None,
             deg_corr=None, clabel=None, pclabel=None, overlap=None,
             layers=None, ec=None, **kwargs):
        r"""Copies the block state. The parameters override the state properties, and
         have the same meaning as in the constructor."""
        lweights = self.g.new_vp("vector<int>")
        degs = None
        if not self.overlap:
            libinference.get_lweights(self.g._Graph__graph,
                                      _prop("v", self.g, self.vc),
                                      _prop("v", self.g, self.vmap),
                                      _prop("v", self.g, lweights),
                                      [_prop("v", state.g, state.vweight)
                                       for state in self.layer_states])
            if not isinstance(self.agg_state.degs, libinference.simple_degs_t):
                degs = libinference.get_ldegs(self.g._Graph__graph,
                                              _prop("v", self.g, self.vc),
                                              _prop("v", self.g, self.vmap),
                                              [self.agg_state.degs] +
                                              [state.degs for state
                                               in self.layer_states])
            else:
                degs = None

        ec = self.ec if ec is None else ec
        gs = [u.copy() for u in self.gs] if ec is None else []

        if len(gs) > 0:
            libinference.get_rvmap(self.g._Graph__graph,
                                   _prop("v", self.g, self.vc),
                                   _prop("v", self.g, self.vmap),
                                   [_prop("v", u, u.vp.vmap) for u in gs])
            for u in gs:
                u.gp.rec = [u.own_property(x.copy()) for x in u.gp.rec]
                if u.gp.drec is not None:
                    u.gp.drec = [u.own_property(x.copy()) for x in u.gp.drec]

        state = LayeredBlockState(self.g if g is None else g,
                                  ec=ec, gs=gs,
                                  eweight=self.eweight if eweight is None else eweight,
                                  vweight=self.vweight if vweight is None else vweight,
                                  recs=kwargs.pop("recs", self.rec),
                                  drec=kwargs.pop("drec", self.drec),
                                  rec_types=kwargs.pop("rec_types", self.rec_types),
                                  rec_params=kwargs.pop("rec_params", self.rec_params),
                                  b=self.b if b is None else b,
                                  B=(self.B if b is None else None) if B is None else B,
                                  clabel=self.clabel.fa if clabel is None else clabel,
                                  pclabel=self.pclabel if pclabel is None else pclabel,
                                  deg_corr=self.deg_corr if deg_corr is None else deg_corr,
                                  overlap=self.overlap if overlap is None else overlap,
                                  allow_empty=kwargs.pop("allow_empty",
                                                         self.allow_empty),
                                  layers=self.layers if layers is None else layers,
                                  base_g=self.base_g if self.overlap else None,
                                  half_edges=self.agg_state.half_edges if self.overlap else None,
                                  node_index=self.agg_state.node_index if self.overlap else None,
                                  eindex=self.agg_state.eindex if self.overlap else None,
                                  ec_done=ec is not None,
                                  degs=degs, lweights=lweights,
                                  Lrecdx=kwargs.pop("Lrecdx",
                                                    [x.copy() for x in self.Lrecdx]),
                                  epsilon=kwargs.pop("epsilon", self.epsilon.copy()),
                                  **kwargs)

        if self._coupled_state is not None:
            state._couple_state(state.get_block_state(b=state.get_bclabel(),
                                                      copy_bg=False,
                                                      vweight="nonempty",
                                                      Lrecdx=state.Lrecdx,
                                                      allow_empty=False),
                                self._coupled_state[1])
        return state

    def __repr__(self):
        return "<LayeredBlockState object with %d %sblocks, %d %s,%s%s for graph %s, at 0x%x>" % \
            (self.B, "overlapping " if self.overlap else "",
             self.C, "layers" if self.layers else "edge covariates",
             " degree-corrected," if self.deg_corr else "",
             ((" with %d edge covariate%s," % (len(self.rec_types),
                                               "s" if len(self.rec_types) > 1 else ""))
              if len(self.rec_types) > 0 else ""),
             str(self.base_g if self.overlap else self.g), id(self))

    def get_bg(self):
        r"""Returns the block graph."""

        bg = Graph(directed=self.g.is_directed())
        mrs = bg.new_ep("int")
        ec = bg.new_ep("int")
        rec = bg.new_edge_property("vector<double>")
        drec = bg.new_edge_property("vector<double>")

        for l in range(self.C):
            u = GraphView(self.g, efilt=self.ec.a == l)
            ug = get_block_graph(u, self.B, self.b, self.vweight, self.eweight,
                                 rec=self.rec, drec=self.drec)
            uec = ug.new_ep("int")
            uec.a = l
            if len(ug.gp.rec) > 0:
                urec = group_vector_property(ug.gp.rec)
                udrec = group_vector_property(ug.gp.drec)
            else:
                urec = ug.new_ep("vector<double>")
                udrec = ug.new_ep("vector<double>")
            bg, props = graph_union(bg, ug,
                                    props=[(mrs, ug.ep["count"]),
                                           (ec, uec),
                                           (rec, urec),
                                           (drec, udrec)],
                                    intersection=ug.vertex_index,
                                    include=True)
            mrs = props[0]
            ec = props[1]
            rec = props[2]
            drec = props[3]

        rec = ungroup_vector_property(rec, range(len(self.rec)))
        drec = ungroup_vector_property(drec, range(len(self.drec)))

        return bg, mrs, ec, rec, drec

    def get_block_state(self, b=None, vweight=False, deg_corr=False,
                        overlap=False, layers=None, **kwargs):
        r"""Returns a :class:`~graph_tool.inference.LayeredBlockState`` corresponding
        to the block graph. The parameters have the same meaning as the in the
        constructor."""


        copy_bg = kwargs.pop("copy_bg", True)

        if copy_bg:
            bg, mrs, ec, brec, bdrec = self.get_bg()
            gs = []
        else:
            gs = []
            for l, s in enumerate(self.layer_states):
                u = GraphView(s.bg)
                u.ep.weight = s.mrs
                u.vp.vmap = u.own_property(s.g.vp.brmap).copy()
                u.vp.b = u.new_vp("int")
                if vweight == True:
                    u.vp.weight = u.own_property(s.wr)
                else:
                    u.vp.weight = u.new_vp("int", s.wr.a > 0)
                u.vp.brmap = u.new_vp("int")
                u.gp.rec = u.new_gp("object", val=s.brec)
                u.gp.drec = u.new_gp("object", val=s.bdrec)
                gs.append(u)
            bg = self.agg_state.bg
            mrs = self.agg_state.mrs
            ec = None
            brec = self.brec
            bdrec = self.bdrec

        lweights = bg.new_vp("vector<int>")
        if not overlap and vweight == True:
            degs = libinference.get_layered_block_degs(self.g._Graph__graph,
                                                       _prop("e", self.g,
                                                             self.eweight),
                                                       _prop("v", self.g,
                                                             self.vweight),
                                                       _prop("e", self.g,
                                                             self.ec),
                                                       _prop("v", self.g,
                                                             self.b))
            libinference.get_blweights(self.g._Graph__graph,
                                       _prop("v", self.g, self.b),
                                       _prop("v", self.g, self.vc),
                                       _prop("v", self.g, self.vmap),
                                       _prop("v", bg, lweights),
                                       [_prop("v", state.g, state.vweight)
                                        for state in self.layer_states])
        else:
            degs = None

        copy_coupled = False
        recs = False
        if vweight == "nonempty":
            vweight = bg.new_vp("int", self.wr.a > 0)
            layers = True if layers is None else layers
        elif vweight == "unity":
            vweight = bg.new_vp("int", 1)
            layers = True if layers is None else layers
        elif vweight == True:
            if copy_bg:
                vweight = bg.own_property(self.wr.copy())
            else:
                vweight = self.wr
            recs = True
            copy_coupled = True
            kwargs["Lrecdx"] = kwargs.get("Lrecdx",
                                          [x.copy() for x in self.Lrecdx])
        else:
            vweight = None
            layers = True if layers is None else layers

        if recs:
            rec_types = kwargs.pop("rec_types", self.rec_types)
            recs = kwargs.pop("recs", brec)
            drec = kwargs.pop("drec", bdrec)
            rec_params = kwargs.pop("rec_params", self.rec_params)
        else:
            recs = []
            drec = None
            for u in gs:
                u.gp.drec = None
                u.gp.rec = []
            rec_types = []
            rec_params = []
            for i, (rt, rp, r) in enumerate(zip(self.rec_types, self.wparams,
                                                brec)):
                if rt == libinference.rec_type.count:
                    recs.append(bg.new_ep("double", mrs.fa > 0))
                    for l, u in enumerate(gs):
                        u.gp.rec.append(u.new_ep("double", u.ep.weight.fa > 0))
                    rec_types.append(rt)
                    rec_params.append("microcanonical")
                elif numpy.isnan(rp.a).sum() == 0:
                    continue
                elif rt in [libinference.rec_type.discrete_geometric,
                            libinference.rec_type.discrete_binomial,
                            libinference.rec_type.discrete_poisson]:
                    recs.append(r)
                    for l, u in enumerate(gs):
                        u.gp.rec.append(self.layer_states[l].brec[i])
                    rec_types.append(libinference.rec_type.discrete_geometric)
                    rec_params.append("microcanonical")
                elif rt == libinference.rec_type.real_exponential:
                    recs.append(r)
                    for l, u in enumerate(gs):
                        u.gp.rec.append(self.layer_states[l].brec[i])
                    rec_types.append(rt)
                    rec_params.append("microcanonical")
                elif rt == libinference.rec_type.real_normal:
                    recs.append(r)
                    for l, u in enumerate(gs):
                        u.gp.rec.append(self.layer_states[l].brec[i])
                    rec_types.append(rt)
                    rec_params.append("microcanonical")
            rec_params = kwargs.pop("rec_params", rec_params)

        state = LayeredBlockState(bg, ec, eweight=mrs,
                                  vweight=vweight,
                                  gs=gs,
                                  rec_types=rec_types,
                                  recs=recs,
                                  drec=drec,
                                  rec_params=rec_params,
                                  b=bg.vertex_index.copy("int") if b is None else b,
                                  deg_corr=deg_corr,
                                  overlap=overlap,
                                  allow_empty=kwargs.pop("allow_empty",
                                                         self.allow_empty),
                                  max_BE=self.max_BE,
                                  layers=self.layers if layers is None else layers,
                                  ec_done=True,
                                  degs=degs, lweights=lweights,
                                  clabel=kwargs.pop("clabel",
                                                    self.agg_state.get_bclabel()),
                                  pclabel=kwargs.pop("pclabel",
                                                     self.agg_state.get_bpclabel()),
                                  epsilon=kwargs.pop("epsilon",
                                                     self.epsilon.copy()),
                                  **kwargs)

        if copy_coupled and self._coupled_state is not None:
            state._couple_state(state.get_block_state(b=state.get_bclabel(),
                                                      copy_bg=False,
                                                      vweight="nonempty",
                                                      Lrecdx=state.Lrecdx,
                                                      allow_empty=False),
                                self._coupled_state[1])

        return state

    def _set_bclabel(self, bstate):
        BlockState._set_bclabel(self, bstate)
        self._state.sync_bclabel()
        # for s, sn in zip(self.layer_states, bstate.layer_states):
        #     s.bclabel.a = sn.b.a

    def get_edge_blocks(self):
        r"""Returns an edge property map which contains the block labels pairs for each
        edge."""
        if not self.overlap:
            raise ValueError("edge blocks only available if overlap == True")
        return self.agg_state.get_edge_blocks()

    def get_overlap_blocks(self):
        r"""Returns the mixed membership of each vertex.

        Returns
        -------
        bv : :class:`~graph_tool.PropertyMap`
           A vector-valued vertex property map containing the block memberships
           of each node.
        bc_in : :class:`~graph_tool.PropertyMap`
           The labelled in-degrees of each node, i.e. how many in-edges belong
           to each group, in the same order as the ``bv`` property above.
        bc_out : :class:`~graph_tool.PropertyMap`
           The labelled out-degrees of each node, i.e. how many out-edges belong
           to each group, in the same order as the ``bv`` property above.
        bc_total : :class:`~graph_tool.PropertyMap`
           The labelled total degrees of each node, i.e. how many incident edges
           belong to each group, in the same order as the ``bv`` property above.

        """
        if not self.overlap:
            raise ValueError("overlap blocks only available if overlap == True")
        return self.agg_state.get_overlap_blocks()

    def get_nonoverlap_blocks(self):
        r"""Returns a scalar-valued vertex property map with the block mixture
        represented as a single number."""

        if not self.overlap:
            return self.b.copy()
        else:
            return self.agg_state.get_nonoverlap_blocks()

    def get_majority_blocks(self):
        r"""Returns a scalar-valued vertex property map with the majority block
        membership of each node."""

        if not self.overlap:
            return self.b.copy()
        else:
            return self.agg_state.get_majority_blocks()

    def _couple_state(self, state, entropy_args):
        if state is None:
            self._coupled_state = None
            self._state.decouple_state()
        else:
            if _bm_test():
                assert state.g.base is self.bg.base
                assert state.agg_state.g.base is self.agg_state.bg.base
                for l, (s1, s2) in enumerate(zip(state.layer_states,
                                                 self.layer_states)):
                    assert s1.g.base is s2.bg.base, (l, s1, s2)

            self._coupled_state = (state, entropy_args)
            eargs = get_entropy_args(dict(self._entropy_args,
                                          **entropy_args))
            self._state.couple_state(state._state, eargs)
            self._set_bclabel(state)

    def _set_bclabel(self, bstate):
        BlockState._set_bclabel(self, bstate)
        for s, bs in zip(self.layer_states,
                         bstate.layer_states):
            s._set_bclabel(bs)

    def _check_clabel(self, clabel=None, b=None):
        if not BlockState._check_clabel(self, clabel, b):
            return False
        if self._coupled_state is not None:
            for s, bs in zip(self.layer_states,
                             self._coupled_state[0].layer_states):
                b = s.bclabel
                mask = bs.vweight.fa > 0
                if any(b.fa[mask] != bs.b.fa[mask]):
                    return False
        return True

    def entropy(self, adjacency=True, dl=True, partition_dl=True,
                degree_dl=True, degree_dl_kind="distributed", edges_dl=True,
                dense=False, multigraph=True, deg_entropy=True, exact=True,
                **kwargs):
        r"""Calculate the entropy associated with the current block partition. The
        meaning of the parameters are the same as in
        :meth:`graph_tool.inference.BlockState.entropy`.
        """

        if _bm_test() and kwargs.get("test", True):
            args = dict(**locals())
            args.update(**kwargs)
            del args["self"]
            del args["kwargs"]

        S = BlockState.entropy(self, adjacency=adjacency, dl=dl,
                               partition_dl=partition_dl, degree_dl=degree_dl,
                               degree_dl_kind=degree_dl_kind, edges_dl=False,
                               dense=dense, multigraph=multigraph,
                               deg_entropy=deg_entropy, exact=exact,
                               **dict(kwargs, test=False))

        if dl and edges_dl:
            if self.layers:
                for state in self.layer_states:
                    if not self.allow_empty:
                        actual_B = (state.wr.a > 0).sum()
                    else:
                        actual_B = self.B
                    S += model_entropy(actual_B, 0, state.get_E(),
                                       directed=self.g.is_directed(),
                                       nr=False)
            else:
                if not self.allow_empty:
                    actual_B = (self.wr.a > 0).sum()
                else:
                    actual_B = self.B
                for state in self.layer_states:
                    S += model_entropy(actual_B, 0, state.get_E(),
                                       directed=self.g.is_directed(),
                                       nr=False)

        if _bm_test() and kwargs.get("test", True):
            assert not isnan(S) and not isinf(S), \
                "invalid entropy %g (%s) " % (S, str(args))

            state = self.copy()
            Salt = state.entropy(test=False, **args)
            assert math.isclose(S, Salt, abs_tol=1e-8), \
                "entropy discrepancy after copying (%g %g)" % (S, Salt)

        return S

    def _get_lvertex(self, v, l):
        i = numpy.searchsorted(self.vc[v].a, l)
        if i >= len(self.vc[v]) or l != self.vc[v][i]:
            raise ValueError("vertex %d not present in layer %d" % (v, l))
        u = self.vmap[v][i]
        return u

    def get_edges_prob(self, missing, spurious=[], entropy_args={}):
        """Compute the joint log-probability of the missing and spurious edges given by
        ``missing`` and ``spurious`` (a list of ``(source, target, layer)``
        tuples, or :meth:`~graph_tool.Edge` instances), together with the
        observed edges.

        More precisely, the log-likelihood returned is

        .. math::

            \ln \frac{P(\boldsymbol G + \delta \boldsymbol G | \boldsymbol b)}{P(\boldsymbol G| \boldsymbol b)}

        where :math:`\boldsymbol G + \delta \boldsymbol G` is the modified graph
        (with missing edges added and spurious edges deleted).

        The values in ``entropy_args`` are passed to
        :meth:`graph_tool.BlockState.entropy()` to calculate the
        log-probability.
        """

        Si = self.entropy(**dict(dict(partition_dl=False), **entropy_args))


        pos = {}
        nes = []
        for e in itertools.chain(missing, spurious):
            try:
                u, v = e
                l = self.ec[e]
            except (TypeError, ValueError):
                u, v, l = e

            pos[u] = self.b[u]
            pos[v] = self.b[v]

            nes.append((u, v, (l, False)))
            nes.append((self._get_lvertex(u, l),
                        self._get_lvertex(v, l), (l, True)))

        edge_list = nes

        self.remove_vertex(pos.keys())

        agg_state = self.agg_state

        try:
            new_es = []
            for u, v, l in missing:
                if not l[1]:
                    state = self.agg_state
                else:
                    state = self.layer_states[l[0]]
                e = state.g.add_edge(u, v)
                if not l[1]:
                    self.ec[e] = l[0]
                if state.is_weighted:
                    state.eweight[e] = 1
                new_es.append((e, l))

            old_es = []
            for u, v, l in spurious:
                if not l[1]:
                    state = self.agg_state
                    es = state.g.edge(u, v, all_edges=True)
                    es = [e for e in es if self.ec[e] == l[0]]
                    if len(es) > 0:
                        e = es[0]
                    else:
                        e = None
                else:
                    state = self.layer_states[l[0]]
                    e = state.g.edge(u, v)
                if e is None:
                    raise ValueError("edge not found: (%d, %d, %d)" % \
                                     (int(u), int(v), l[0]))

                if state.is_weighted:
                    staete.eweight[e] -= 1
                    if state.eweight[e] == 0:
                        state.g.remove_edge(e)
                else:
                    state.g.remove_edge(e)
                old_es.append((u, v, l))

            self.add_vertex(pos.keys(), pos.values())

            Sf = self.entropy(**dict(dict(partition_dl=False), **entropy_args))

            self.remove_vertex(pos.keys())

        finally:
            for e, l in new_es:
                if not l[1]:
                    state = self.agg_state
                else:
                    state = self.layer_states[l[0]]
                state.g.remove_edge(e)
            for u, v, l in old_es:
                if not l[1]:
                    state = self.agg_state
                else:
                    state = self.layer_states[l[0]]
                if state.is_weighted:
                    e = state.g.edge(u, v)
                    if e is None:
                        e = state.g.add_edge(u, v)
                        state.eweight[e] = 0
                        if not l[1]:
                            self.ec[e] = l[0]
                    state.eweight[e] += 1
                else:
                    e = state.g.add_edge(u, v)
                    if not l[1]:
                        self.ec[e] = l[0]
            self.add_vertex(pos.keys(), pos.values())

        L = Si - Sf

        if _bm_test():
            state = self.copy()
            set_test(False)
            L_alt = state.get_edges_prob(edge_list, missing=missing,
                                         entropy_args=entropy_args)
            set_test(True)
            assert math.isclose(L, L_alt, abs_tol=1e-8), \
                "inconsistent missing=%s edge probability (%g, %g): %s, %s" % \
                (str(missing), L, L_alt,  str(entropy_args), str(edge_list))

        return L

    def _mcmc_sweep_dispatch(self, mcmc_state):
        if not self.overlap:
            return libinference.mcmc_layered_sweep(mcmc_state, self._state,
                                                   _get_rng())
        else:
            dS, nmoves = libinference.mcmc_layered_overlap_sweep(mcmc_state,
                                                                 self._state,
                                                                 _get_rng())
            if self.__bundled:
                ret = libinference.mcmc_layered_overlap_bundled_sweep(mcmc_state,
                                                                      self._state,
                                                                      _get_rng())
                dS += ret[0]
                nmoves += ret[1]
            return dS, nmoves

    def mcmc_sweep(self, bundled=False, **kwargs):
        r"""Perform sweeps of a Metropolis-Hastings rejection sampling MCMC to sample
        network partitions. If ``bundled == True`` and the state is an
        overlapping one, the half-edges incident of the same node that belong to
        the same group are moved together. All remaining parameters are passed
        to :meth:`graph_tool.inference.BlockState.mcmc_sweep`."""

        self.__bundled = bundled
        return BlockState.mcmc_sweep(self, **kwargs)

    def _multiflip_mcmc_sweep_dispatch(self, mcmc_state):
        if not self.overlap:
            return libinference.multiflip_mcmc_layered_sweep(mcmc_state,
                                                             self._state,
                                                             _get_rng())
        else:
            return libinference.multiflip_mcmc_layered_overlap_sweep(mcmc_state,
                                                                     self._state,
                                                                     _get_rng())

    def _gibbs_sweep_dispatch(self, mcmc_state):
        if not self.overlap:
            return libinference.gibbs_layered_sweep(mcmc_state, self._state,
                                                    _get_rng())
        else:
            return libinference.gibbs_layered_overlap_sweep(mcmc_state,
                                                            self._state,
                                                            _get_rng())

    def _multicanonical_sweep_dispatch(self, mcmc_state):
        if not self.overlap:
            if mcmc_state.multiflip:
                return libinference.multicanonical_layered_multiflip_sweep(mcmc_state,
                                                                           self._state,
                                                                           _get_rng())
            else:
                return libinference.multicanonical_layered_sweep(mcmc_state,
                                                                 self._state,
                                                                 _get_rng())
        else:
            if mcmc_state.multiflip:
                return libinference.multicanonical_layered_overlap_multiflip_sweep(mcmc_state,
                                                                                   self._state,
                                                                                   _get_rng())
            else:
                return libinference.multicanonical_layered_overlap_sweep(mcmc_state,
                                                                         self._state,
                                                                         _get_rng())

    def _exhaustive_sweep_dispatch(self, exhaustive_state, callback, hist):
        if not self.overlap:
            if callback is not None:
                return libinference.exhaustive_layered_sweep(exhaustive_state,
                                                             self._state,
                                                             callback)
            else:
                if hist is None:
                    return libinference.exhaustive_layered_sweep_iter(exhaustive_state,
                                                                      self._state)
                else:
                    return libinference.exhaustive_layered_sweep_dens(exhaustive_state,
                                                                      self._state,
                                                                      hist[0],
                                                                      hist[1],
                                                                      hist[2])
        else:
            if callback is not None:
                return libinference.exhaustive_layered_overlap_sweep(exhaustive_state,
                                                                     self._state,
                                                                     callback)
            else:
                if hist is None:
                    return libinference.exhaustive_layered_overlap_sweep_iter(exhaustive_state,
                                                                              self._state)
                else:
                    return libinference.exhaustive_layered_overlap_dens(exhaustive_state,
                                                                        self._state,
                                                                        hist[0],
                                                                        hist[1],
                                                                        hist[2])
    def _merge_sweep_dispatch(self, merge_state):
        if not self.overlap:
            return libinference.merge_layered_sweep(merge_state, self._state,
                                                    _get_rng())
        else:
            return libinference.vacate_layered_overlap_sweep(merge_state,
                                                             self._state,
                                                             _get_rng())

    def shrink(self, B, **kwargs):
        """Reduces the order of current state by progressively merging groups, until
        only ``B`` are left. All remaining keyword arguments are passed to
        :meth:`graph_tool.inference.BlockState.shrink` or
        :meth:`graph_tool.inference.OverlapBlockState.shrink`, as appropriate.

        This function leaves the current state untouched and returns instead a
        copy with the new partition.
        """

        if not self.overlap:
            return BlockState.shrink(self, B, **kwargs)
        else:
            return OverlapBlockState.shrink(self, B, **kwargs)

    def draw(self, **kwargs):
        """Convenience function to draw the current state. All keyword arguments are
        passed to :meth:`graph_tool.inference.BlockState.draw` or
        :meth:`graph_tool.inference.OverlapBlockState.draw`, as appropriate.
        """

        self.agg_state.draw(**kwargs)


def init_layer_confined(g, ec):
    tmp_state = CovariateBlockState(g, ec=ec, B=g.num_vertices())
    tmp_state = tmp_state.copy(overlap=True)
    be = tmp_state.get_edge_blocks()
    ba = ungroup_vector_property(be, [0])[0]
    ba.fa = ba.fa + ec.fa * (ba.fa.max() + 1)
    continuous_map(ba)
    be = group_vector_property([ba, ba])
    return be