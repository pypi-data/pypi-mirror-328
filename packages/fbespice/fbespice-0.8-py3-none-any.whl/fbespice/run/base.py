# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import subprocess
from os.path import dirname, basename
from typing import Any
from .. import netlist

#########################################################

class SpiceBase:
    _exec_name : str
    _exec_options : list
    _netlist_ext :str
    _meta_netlist_ext : str
    _results_ext : str # raw results
    _step_ext : str
    # full file path without extension
    _design : str

    @property
    def exec_name(self):
        return self._exec_name

    @property
    def exec_options(self):
        return self._exec_options

    @property
    def netlist_ext(self):
        return self._netlist_ext

    @property
    def meta_netlist_ext(self):
        return self._meta_netlist_ext

    @property
    def results_ext(self):
        return self._results_ext

    @property
    def step_ext(self):
        return self._step_ext

    @property
    def design(self):
        return self._design

    def __init__(self,
                 design : str,
                 exec_name : str,
                 exec_options : list,
                 netlist_ext : str = "cir",
                 meta_netlist_ext : str = "mcir",
                 step_ext : str = "res",
                 results_ext : str = "raw"):
        self._design = design
        self._exec_name = exec_name
        self._exec_options = exec_options
        self._netlist_ext = netlist_ext
        self._meta_netlist_ext = meta_netlist_ext
        self._step_ext = step_ext
        self._results_ext = results_ext

    def _run(self, raw : bool):
        netlist = self._join_w_dot([self._design, self._netlist_ext])
        dn = dirname(netlist)
        fn = basename(netlist)
        results = basename(self._join_w_dot([self._design, self._results_ext]))
        subprocess.run([self._exec_name] +
                       (["-r", results] if raw else []) +
                       self._exec_options +
                       [fn],
                       cwd=dn)
        return self

    def netlist_from_meta(self, sim_vars: dict[str,Any]):
        """Convert the meta-netlist into a simulable netlist.

        Parameters:
          sim_vars: Mapping of meta-variable names to values.
        """
        mnl = self._join_w_dot([self._design,self._meta_netlist_ext])
        nl = self._join_w_dot([self._design,self._netlist_ext])
        netlist.netlist_from_meta(sim_vars, mnl, nl)
        return self

    def _join_w_dot(self, ls : list[str]) -> str:
        return '.'.join(ls)
