# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import pandas as pd
import numpy as np
from enum import StrEnum, auto

#########################################################

class XyceResID(StrEnum):
    HB = auto()
    HB_TD = auto()
    HB_IC = auto()
    HB_STARTUP = auto()
    AC = auto()
    AC_IC = auto()
    DC = auto()
    NOISE = auto()
    TRAN = auto()
    DC_SENS = auto()
    TRAN_SENS = auto()
    TRAN_ADJ = auto()
    AC_SENS = auto()
    ES = auto()
    def __format__(self, _):
        return f'{self.name}'

##########################################################

def read_xyce(fn : str, stpfile : str | None = None) -> pd.DataFrame:
    """Read the ASCII result file produced by Xyce in STD mode.

    Parameters:
      fn: file name
      stpfile: when performing a `.step` SPICE simulation it should be a string with the name of the auxiliary Xyce result file (`.res`). Its content (swept parameters, ...) will also be read and combined with simulation results.

    Returns:
      Since Xyce currently can only run one simulation type at a time, this function doesn't return a dictionary indexed by simulation type as :py:func:`read_raw`, but directly a :py:class:`pandas.DataFrame` whose columns are the simulation vectors printed to the output file (with SPICE `.print` commands), plus optionally the content of the auxiliary result file.
    """
    df = pd.read_csv(fn,
                     skipfooter=1,
                     sep='\\s+',
                     index_col='Index',
                     engine='python')
    df.rename(columns=str.lower, inplace=True)
    if stpfile:
        stps = pd.read_csv(stpfile,
                           skipfooter=1,
                           sep='\\s+',
                           index_col='Index',
                           engine='python')
        stps.rename(columns=str.lower, inplace=True)
        stps_len = len(df.groupby(df.columns[0]).groups.keys())
        df = pd.concat([df,
                        stps.apply(lambda x: np.repeat(x, stps_len)).reset_index(drop=True) ],
                       axis=1)

    return df
