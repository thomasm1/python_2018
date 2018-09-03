## Process this file with automake to produce Makefile.in

AM_CPPFLAGS = $(MOD_CPPFLAGS)

AM_CFLAGS = $(AM_CXXFLAGS)

libgraph_tool_inferencedir = $(MOD_DIR)/inference

libgraph_tool_inference_LTLIBRARIES = libgraph_tool_inference.la

libgraph_tool_inference_la_includedir = $(MOD_DIR)/include/inference

libgraph_tool_inference_la_LIBADD = $(MOD_LIBADD)

libgraph_tool_inference_la_LDFLAGS = $(MOD_LDFLAGS)

libgraph_tool_inference_la_SOURCES = \
    blockmodel/graph_blockmodel.cc \
    blockmodel/graph_blockmodel_em.cc \
    blockmodel/graph_blockmodel_exhaustive.cc \
    blockmodel/graph_blockmodel_gibbs.cc \
    blockmodel/graph_blockmodel_imp.cc \
    blockmodel/graph_blockmodel_imp2.cc \
    blockmodel/graph_blockmodel_marginals.cc \
    blockmodel/graph_blockmodel_mcmc.cc \
    blockmodel/graph_blockmodel_merge.cc \
    blockmodel/graph_blockmodel_multicanonical.cc \
    blockmodel/graph_blockmodel_multicanonical_multiflip.cc \
    blockmodel/graph_blockmodel_multiflip_mcmc.cc \
    overlap/graph_blockmodel_overlap.cc \
    overlap/graph_blockmodel_overlap_exhaustive.cc \
    overlap/graph_blockmodel_overlap_gibbs.cc \
    overlap/graph_blockmodel_overlap_mcmc.cc \
    overlap/graph_blockmodel_overlap_mcmc_bundled.cc \
    overlap/graph_blockmodel_overlap_multicanonical.cc \
    overlap/graph_blockmodel_overlap_multicanonical_multiflip.cc \
    overlap/graph_blockmodel_overlap_multiflip_mcmc.cc \
    overlap/graph_blockmodel_overlap_vacate.cc \
    layers/graph_blockmodel_layers.cc \
    layers/graph_blockmodel_layers_exhaustive.cc \
    layers/graph_blockmodel_layers_gibbs.cc \
    layers/graph_blockmodel_layers_imp.cc \
    layers/graph_blockmodel_layers_mcmc.cc \
    layers/graph_blockmodel_layers_merge.cc \
    layers/graph_blockmodel_layers_multicanonical.cc \
    layers/graph_blockmodel_layers_multicanonical_multiflip.cc \
    layers/graph_blockmodel_layers_multiflip_mcmc.cc \
    layers/graph_blockmodel_layers_overlap.cc \
    layers/graph_blockmodel_layers_overlap_exhaustive.cc \
    layers/graph_blockmodel_layers_overlap_gibbs.cc \
    layers/graph_blockmodel_layers_overlap_mcmc.cc \
    layers/graph_blockmodel_layers_overlap_mcmc_bundled.cc \
    layers/graph_blockmodel_layers_overlap_multicanonical.cc \
    layers/graph_blockmodel_layers_overlap_multicanonical_multiflip.cc \
    layers/graph_blockmodel_layers_overlap_multiflip_mcmc.cc \
    layers/graph_blockmodel_layers_overlap_vacate.cc \
    support/cache.cc \
    support/int_part.cc \
    support/spence.cc \
    graph_inference.cc \
    graph_modularity.cc

libgraph_tool_inference_la_include_HEADERS = \
    blockmodel/graph_blockmodel.hh \
    blockmodel/graph_blockmodel_em.hh \
    blockmodel/graph_blockmodel_emat.hh \
    blockmodel/graph_blockmodel_elist.hh \
    blockmodel/graph_blockmodel_entries.hh \
    blockmodel/graph_blockmodel_entropy.hh \
    blockmodel/graph_blockmodel_exhaustive.hh \
    blockmodel/graph_blockmodel_gibbs.hh \
    blockmodel/graph_blockmodel_mcmc.hh \
    blockmodel/graph_blockmodel_merge.hh \
    blockmodel/graph_blockmodel_multicanonical.hh \
    blockmodel/graph_blockmodel_multiflip_mcmc.hh \
    blockmodel/graph_blockmodel_partition.hh \
    blockmodel/graph_blockmodel_util.hh \
    blockmodel/graph_blockmodel_weights.hh \
    graph_modularity.hh \
    layers/graph_blockmodel_layers.hh \
    layers/graph_blockmodel_layers_util.hh \
    loops/bundled_vacate_loop.hh \
    loops/exhaustive_loop.hh \
    loops/gibbs_loop.hh \
    loops/mcmc_loop.hh \
    loops/merge_loop.hh \
    overlap/graph_blockmodel_overlap.hh \
    overlap/graph_blockmodel_overlap_mcmc_bundled.hh \
    overlap/graph_blockmodel_overlap_util.hh \
    overlap/graph_blockmodel_overlap_vacate.hh \
    overlap/graph_blockmodel_overlap_partition.hh \
    support/cache.hh \
    support/graph_neighbor_sampler.hh \
    support/graph_state.hh \
    support/int_part.hh \
    support/parallel_rng.hh \
    support/util.hh
