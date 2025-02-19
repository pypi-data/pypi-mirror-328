# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .base import SpiceBase
from ..results import read_raw, RawResID

#########################################################

class NGSpice(SpiceBase):
    """Create a NGSpice object with all parameters to simulate a `design`.

    Create objects to Manage ngspice simulations, from netlist creation to reading results. All results file are stored in the same directory as the `design` file.

    Parameters:
      design: a string with the path to the (meta-) netlist file to be simulated without extension.
      exec_name: the ngspice program name (the full path if not on PATH).
      exec_options: options to pass to ngspice on top of the netlist name. Note that the option "-r" always implicitly added to produce results in the raw data format.
      netlist_ext: the extension of the netlist file (without dot).
      meta_netlist_ext: the extension of the meta-netlist file (without dot).
      results_ext: the extension to be used for the raw result file produced by ngspice (without dot).
    """

    def __init__(self,
                 design : str,
                 exec_name : str = "ngspice",
                 exec_options : list = ["-b"],
                 netlist_ext : str = "cir",
                 meta_netlist_ext : str = "mcir",
                 results_ext : str = "raw") -> None:
        SpiceBase.__init__(self,
                           design,
                           exec_name,
                           exec_options,
                           netlist_ext,
                           meta_netlist_ext,
                           "",
                           results_ext)
    def run(self):
        """Run the simulation."""
        SpiceBase._run(self, True)
        return self

    def read_results(self, resid : RawResID | None = None) -> dict:
        """Read the results of the simulation (raw file).

        Parameters:
          resid: Define the simulation result type to read. 'Note' to read all results.

        Returns:
          :py:class:`dict` mapping :py:class:`fbespice.RawResID` to simulations results in the file. The simulation data is a :py:class:`pandas.DataFrame` whose columns are the SPICE variables stored in the file (see :py:func:`fbespice.read_raw`).

        """
        res = self._join_w_dot([self._design, self._results_ext])
        return read_raw(res, resid)
