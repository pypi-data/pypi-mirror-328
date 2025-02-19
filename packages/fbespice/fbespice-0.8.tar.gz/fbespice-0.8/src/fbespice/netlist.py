# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import functools

######################################################

def netlist_from_meta(vs, infile, outfile):
    with open(infile, 'r') as fi:
        mnl = fi.read()
    nl = functools.reduce(
        lambda acc,v: acc.replace('$$'+v+'$$', str(vs[v])),
        vs,
        mnl)
    with open(outfile, 'w') as fo:
        fo.write(nl)
