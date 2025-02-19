# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Interaction with SPICE-like simulators.

The library support the generation of netlists from so-called *meta-netlists*, running SPICE-like simulators and reading back the results. Currently the following simulators are supported:

* ngspice
* Xyce

These capabilities are implemented in the objects :py:class:`NGSpice` and :py:class:`Xyce` respectively.

A *meta-netlist* is a netlist with *meta-netlist variables* denoted by alphanumerical variables surrounded by double dollers ``$$var$$``. This allows, for example, to

* Check performance across corners.
* Sweep parameters in netlist places where SPICE expressions/variables are not permitted.
* Run multiple simulation types without manually editing the netlist.
* ...

Given a meta-netlist with variables ``s1_dc``, ``s1_mag``, ``sim_cmd`` and ``sim_output``, a basic usage example is as follows:
  >>> import matplotlib.pyplot as plt
  >>> from fbespice import *
  >>> sim_vars = { 's1_dc' : 0.65,
                   's1_mag' : 0.4,
                   's1_freq' : 100e6}
  >>> tran_vars = dict(sim_vars,
        **{'sim_cmd' : " ".join([".tran",
                         str(0.1/sim_vars['s1_freq']),
                         str(100/sim_vars['s1_freq'])]),
           'sim_output' : ".print tran v(out)"})
  >>> xyce = Xyce("path/to/testbench")
  >>> xyce.netlist_from_meta(tran_vars)
  >>> df_tr = xyce.run().read_results(XyceResID.TRAN)
  >>> ac_vars = dict(sim_vars,
        **{'sim_cmd' : ".ac dec 5 1k 1e9",
           'sim_output' : ".print ac vdb(out) vp(out)"})
  >>> xyce.netlist_from_meta(ac_vars)
  >>> df_ac = xyce.run().read_results(XyceResID.AC)
  >>> plt.plot(df_tr['time'], df_tr['v(out)'])
  >>> plt.semilogx(df_ac['freq'], df_ac['vdb(out)'])

ngspice simulation results are expected in `raw` format and can be read, on top of the :py:meth:`NGSpice.read_results`, also by :py:func:`read_raw`. The library also supports reaing Xyre results in `raw` format. However, given that Xyce can only output results in raw format for a subset of its simulation capabilities, Xyce results are expected in it's native STD format by :py:meth:`Xyce.read_results` and can also be read with :py:func:`read_xyce`.
"""
######################################################

from .netlist import netlist_from_meta
from .results import read_raw, RawResID, read_xyce
from .run import Xyce, XyceResID, NGSpice
