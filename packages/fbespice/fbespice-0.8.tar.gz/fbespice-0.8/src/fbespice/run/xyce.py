# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .base import SpiceBase
from ..results import read_xyce, XyceResID
import pandas as pd

#########################################################

class Xyce(SpiceBase):
    """Create a Xyce object with all parameters to simulate a `design`.

       Manage Xyce simulations, from netlist creation to reading results. All results files are stored in the same directory as the `design` file.

       Parameters:
         design: a string with the path to the (meta-) netlist file to be simulated without extension.
         exec_name: the Xyce program name (the full path if not on PATH).
         exec_options: options to pass to Xyce on top of the netlist name.
         netlist_ext: the extension of the netlist file (without dot).
         meta_netlist_ext: the extension of the meta-netlist file (without dot).
         step_ext: the extension of the auxiliary file produced by Xyce in SPICE `.step` simulations (without dot).
    """

    def _results_ext_fn(self, resid) -> str:
        match resid:
         case XyceResID.HB.value:
             return "HB.FD.prn"
         case XyceResID.HB_TD.value:
             return "HB.TD.prn"
         case XyceResID.HB_IC.value:
             return "hb.ic.prn"
         case XyceResID.HB_STARTUP.value:
             return "startup.prn"
         case XyceResID.AC.value:
             return "FD.prn"
         case XyceResID.AC_IC.value:
             return "TD.prn"
         case XyceResID.DC.value:
             return "prn"
         case XyceResID.NOISE.value:
             return "NOISE.prn"
         case XyceResID.TRAN.value:
             return "prn"
         case XyceResID.DC_SENS.value:
             return "SENS.prn"
         case XyceResID.TRAN_SENS.value:
             return "SENS.prn"
         case XyceResID.TRAN_ADJ.value:
             return "TRADJ.prn"
         case XyceResID.AC_SENS.value:
             return "FD.SENS.prn"
         case XyceResID.ES.value:
             return "ES.prn"
         case s:
             print(f"Xyce._results_ext_fn: unexpected resid {s}")
             return ""

    def __init__(self,
                 design : str,
                 exec_name : str = "Xyce",
                 exec_options : list = ["-quiet"],
                 netlist_ext : str = "cir",
                 meta_netlist_ext : str = "mcir",
                 step_ext : str = "res") -> None:
        SpiceBase.__init__(self,
                           design,
                           exec_name,
                           exec_options,
                           netlist_ext,
                           meta_netlist_ext,
                           step_ext,
                           "raw")

    def run(self):
        """Run the simulation."""
        SpiceBase._run(self, False)
        return self

    def read_results(self, resid : XyceResID, step : bool = False) -> pd.DataFrame:
        """Read the simulation results.

        Parameters:
          resid: define the simulation result file to read (the result file name is simulation type dependent).
          step: set to ``True`` if the simulation includes a SPICE `.step` command.

        Returns:
          a :py:class:`pandas.DataFram` with columns named after the stored simulation variables (see :py:func:`read_xyce`).
        """
        res = self._join_w_dot([self._design,
                                self._netlist_ext,
                                self._results_ext_fn(resid)])
        stps = self._join_w_dot([self._design,
                                self._netlist_ext,
                                 self._step_ext])
        return read_xyce(res) if not step else read_xyce(res, stps)
