# Time-stamp: <2024-10-02 16:16:49 Tao Liu>

"""Description: Naive call peaks from a single bedGraph track for
scores.

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file LICENSE included with
the distribution).
"""

# ------------------------------------
# python modules
# ------------------------------------
import os
from MACS3.IO import BedGraphIO
# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------
from MACS3.Utilities.Logger import logging

logger = logging.getLogger(__name__)
debug = logger.debug
info = logger.info
error = logger.critical
warn = logger.warning
# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main function
# ------------------------------------


def run(options):
    info("Read and build bedGraph...")
    bio = BedGraphIO.bedGraphIO(options.ifile)
    btrack = bio.read_bedGraph(baseline_value=0)

    if options.cutoff_analysis:
        info("Analyze cutoff vs number of peaks/total length of peaks/average length of peak")
        cutoff_analysis_result = btrack.cutoff_analysis(int(options.maxgap), int(options.minlen), min_score=btrack.minvalue, max_score=int(options.cutoff_analysis_max), steps=int(options.cutoff_analysis_steps))
        info("Write report...")
        if options.ofile:
            fhd = open(os.path.join(options.outdir, options.ofile), 'w')
        else:
            fhd = open(os.path.join(options.outdir, "%s_l%d_g%d_cutoff_analysis.txt" % (options.oprefix,options.minlen, options.maxgap)), "w")
        fhd.write(cutoff_analysis_result)
        info("Done")
    else:
        info("Call peaks from bedGraph...")
        peaks = btrack.call_peaks(cutoff=float(options.cutoff), min_length=int(options.minlen), max_gap=int(options.maxgap), call_summits=options.call_summits)

        info("Write peaks...")
        if options.ofile:
            options.oprefix = options.ofile
            nf = open(os.path.join(options.outdir, options.ofile), 'w')
        else:
            nf = open(os.path.join(options.outdir, "%s_c%.1f_l%d_g%d_peaks.narrowPeak" % (options.oprefix, options.cutoff, options.minlen, options.maxgap)), "w")
        peaks.write_to_narrowPeak(nf, name=options.oprefix.encode(), name_prefix=(options.oprefix+"_narrowPeak").encode(), score_column="score", trackline=options.trackline)
        info("Done")
