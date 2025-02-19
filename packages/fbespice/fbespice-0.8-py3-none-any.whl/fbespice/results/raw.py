# SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from io import BufferedReader
import os
import sys
import re
import struct
from enum import StrEnum, auto
import warnings
import numpy as np
# from numpy.dtypes import StringDType # from numpy 2
import pandas as pd
from typing import IO, Any
import numpy.typing as npt

# Requires Python 3.12+
# type SimResult = dict[str, str|int|npt.NDArray]

######################################################
# Simulation types

class RawResID(StrEnum):
    OP = auto()
    AC = auto()
    SP = auto()
    TF = auto()
    NOISE = auto()
    NOISE_INT = auto()
    DC = auto()
    PZ = auto()
    SENS = auto()
    TRAN = auto()
    DISTO2 = auto()
    DISTO3 = auto()
    def __format__(self, _):
        return f'{self.name}'

######################################################
# Simulation types

__sim_step_regex = r"step analysis:\s+step\s+(\d+)\s+of\s+\d+\s+params:\s+name\s+=\s+(\w+)\s+value\s+=\s+([+\-0-9a-zA-Z\.]+)\s+(.+)$"

__sim_nested_step_regex = r"name\s+=\s+(\w+)\s+value\s+=\s+([+\-0-9a-zA-Z\.]+)\s+(.+)$"

def _sim_type(plot_name : str) -> str:
    match plot_name.lower():
        case s if "step analysis:" in s:  # Xyce .step
            m = re.match(__sim_step_regex, s)
            assert(isinstance(m, re.Match))
            ty = _sim_type(m.group(4))
            return ty
        case s if s.startswith("name"):
            m = re.match(__sim_nested_step_regex, s)
            assert(isinstance(m, re.Match))
            return _sim_type(m.group(3))
        case s if "operating point" in s:
            return RawResID.OP.value
        case s if "ac analysis" in s:
            return RawResID.AC.value
        case s if "sp analysis" in s:
            return RawResID.SP.value
        case s if "transfer function" in s:
            return RawResID.TF.value
        case s if "pole-zero analysis" in s:
            return RawResID.PZ.value
        case s if "sensitivity analysis" in s:
            return RawResID.SENS.value
        case s if "distortion - 2nd harmonic" in s:
            return RawResID.DISTO2.value
        case s if "distortion - 3rd harmonic" in s:
            return RawResID.DISTO3.value
        case s if "noise analysis" in s: # Xyce
            warnings.warn("XYCE currently doesn't store NOISE data in raw files.\nAC data returned!")
            return RawResID.NOISE.value
        case s if "noise spectral density curves" in s: # ngspice
            return RawResID.NOISE.value
        case s if "integrated noise" in s: # ngspice
            return RawResID.NOISE_INT.value
        case s if "dc transfer characteristic" in s:
            return RawResID.DC.value
        case s if "transient analysis" in s:
            return RawResID.TRAN.value
        case s:
            warnings.warn(f"Unsupported simulation type: {s}.")
            return "unknown"

######################################################
# Read raw result file

def _header_value(hl : bytes) -> str:
    return hl.decode("ascii").split(':',1)[-1].strip(' \n')

def _read_variable(fh : IO[bytes]) -> list[str]:
    return re.split('\\s+', fh.readline().decode("ascii").strip(' \t\n'))

def _read_variables(fh : IO[bytes], no_vars : int) -> list[list[str]]:
    vs : list[list[str]] = [[""] * 4 for _ in range(no_vars)]
    for i in range(no_vars):
        v = _read_variable(fh)
        for j in range(3):
            vs[i][j] = v[j]
        if len(v) == 4:
            vs[i][3] = v[3]
    return vs

def _read_bin_data(fh : IO[bytes], shape : tuple[int,int], ty : str) -> npt.NDArray:
    if ty == 'real':
        dtype = float
    else:
        dtype = complex
    ds = np.empty(shape, dtype=dtype)
    for i in range(shape[0]):
        for j in range(shape[1]):
            ds[i,j] = _read_bin_value(fh, ty)
    return ds

def _read_bin_value(fh : IO[bytes], ty : str) -> float | complex:
    re = struct.unpack('d',fh.read(8))[0]
    if ty == "complex":
        im = struct.unpack('d',fh.read(8))[0]
        return complex(real=re, imag=im)
    else:
        return re

def _skip_bin_data(fh : IO[bytes], shape : tuple[int,int], ty : str) -> None:
    if ty == 'real':
        fh.seek(8*shape[0]*shape[1], os.SEEK_CUR)
    else:
        fh.seek(16*shape[0]*shape[1], os.SEEK_CUR)

def _peek_isequal(fh: BufferedReader, name: str) -> bool:
    no_bytes = len(name)
    bs = fh.peek(no_bytes)
    nxt = bs[0:no_bytes].decode('ascii')
    return nxt.lower() == name

def _read_sim_header(f: BufferedReader) -> dict[str,Any]:
    title = _header_value(f.readline()) if _peek_isequal(f, "title") else ""
    date = _header_value(f.readline()) if _peek_isequal(f, "date") else ""
    plot_name = _header_value(f.readline())
    flags = _header_value(f.readline())
    no_vars = int(_header_value(f.readline()))
    no_points = int(_header_value(f.readline()))
    variables = (lambda _: _read_variables(f, no_vars))(f.readline())
    raw_type = f.readline().decode("ascii").strip(' :\n')
    return { 'title' : title,
             'date' : date,
             'plot_name' : plot_name,
             'flags' : flags,
             'no_vars' : no_vars,
             'no_points' : no_points,
             'variables' : variables,
             'raw_type' : raw_type }

def _maybe_read_single_sim(f: BufferedReader, simid : None | RawResID =None ) -> dict[str,Any] | None:
    hdr = _read_sim_header(f)
    if (simid == None) | (simid == _sim_type(hdr['plot_name'])):
        data = _read_bin_data(f,
                             (hdr['no_points'], hdr['no_vars']),
                             hdr['flags'])
        hdr.update({'data' : data})
        return hdr
    else:
        _skip_bin_data(f, (hdr['no_points'], hdr['no_vars']), hdr['flags'])
        return None

def _read_raw_file(fn : str, simid=None) -> list:
    """Read the SPICE raw data from file `fn`.

    If `simid` is `None`, return all simulations in the file.
    Otherwise return the indicated simulation. `simid` must
    be a value of the enumeration `RawResID`.

    The result is a `list` The simulation data is isomorphic to
    the raw SPIcE content.

    Example:
    ac_data = _read_raw_file("results.raw", RawResID.AC.value)

    """
    sims = []
    with open(fn, 'rb') as f:
        while len(f.peek(1)) != 0:
            sim = _maybe_read_single_sim(f, simid)
            if sim != None:
                sims.append(sim)
    return sims

def _sim_step_vars(plot_name : str, stp : int =-1, vs : dict ={}) -> dict[str, int | float]:
    match plot_name.lower():
        case s if s.startswith("step analysis:"):
            m = re.match(__sim_step_regex, s)
            assert(isinstance(m, re.Match))
            stp = int(m.group(1))
            vs.update({'step' : stp, m.group(2) : float(m.group(3))})
            _sim_step_vars(m.group(4), stp, vs)
        case s if s.startswith("name"):
            m = re.match(__sim_nested_step_regex, s)
            assert(isinstance(m, re.Match))
            vs.update({m.group(1) : float(m.group(2))})
            _sim_step_vars(m.group(3), stp, vs)
        case _:
            pass
    return vs

def _format_for_user(sims : list) -> dict[RawResID, pd.DataFrame]:
    res = {}
    utys = set(map(lambda d: _sim_type(d['plot_name']), sims))
    # process simulations of the same type (e.g., '.AC').
    for ty in utys:
        # all simulations of the same type
        ty_sims = list(filter(lambda d: _sim_type(d['plot_name']) == ty, sims))
        ty_sims_no = len(ty_sims)
        df_ty = pd.DataFrame()
        vs: list[str] = []
        for s in ty_sims:
            vs = list(map(lambda v: v[1], s['variables']))
            if s['no_points'] > 1:
                df_ty = pd.concat((df_ty, pd.DataFrame(s['data'], columns=vs)))
            else:
                df_ty = pd.concat((df_ty, pd.DataFrame(s['data'], columns=vs, index=pd.Index([0]))))
        df_ty = df_ty.reset_index(drop=True)
        # normalize column names to lower-case
        df_ty.rename(columns=str.lower, inplace=True)
        # make independent variable real
        df_ty[df_ty.columns[0]] = df_ty.iloc[:,0].apply(np.real)
        # combine multiple simulations of the same type
        # ngspice: loops are a sequence of plots. If more than one result
        # of the same type, we must distinguish them. We use a consecutive int.
        # Xyce: .step provides parameter info in the 'plot_name' field
        # that we extract with  _sim_step_vars
        if ty_sims_no > 1:
            stps_len = len(df_ty.groupby(df_ty.columns[0]).groups.keys())
            stp_params = list(map(
                lambda s: _sim_step_vars(s['plot_name'], -1, {}), ty_sims))
            df_stps = pd.DataFrame()
            for ps in zip(stp_params, 1+np.arange(ty_sims_no)):
                if ps[0] != {}:
                    df_stps = pd.concat(
                        (df_stps, pd.DataFrame(ps[0], index=pd.Index([0]))))
                else:
                    df_stps = pd.concat(
                        (df_stps, pd.DataFrame({'step' : ps[1]}, index=pd.Index([0]))))
            df_stps = df_stps.apply(lambda x: np.repeat(x, stps_len))
            df_stps = df_stps.reset_index(drop=True)
            df_ty = pd.concat([df_ty, df_stps], axis=1)
        res.update({ty : df_ty})
    return res

######################################################
# Main user facing function

def _showwarning(message, category, filename, lineno, file=None, line=None):
    msg = warnings.WarningMessage(message, category, filename, lineno, file, line)
    file = msg.file
    if file is None:
        file = sys.stderr
        if file is None:
            # sys.stderr is None when run with pythonw.exe:
            # warnings get lost
            return
    category = msg.category.__name__
    text =  f"{msg.filename}:{msg.lineno}: {category}: {msg.message}\n"
    try:
        file.write(text)
    except OSError:
        # the file (probably stderr) is invalid - this warning gets lost.
        pass

def read_raw(fn : str, simid : None | RawResID = None) -> dict[RawResID, pd.DataFrame]:
    """Read the SPICE raw data from file `fn`.

    Parameters:
      fn: raw results file name.
      simid: if `None` return all simulations in the file. Otherwise return the indicated simulation. `simid` must be a value of the enumeration `RawResID`. If the file includes multiple results of type `simid`, the first one is returned.

    Returns:
      A :py:class:`dict` mapping :py:class:`fbespice.RawResID` to simulations results in the file. The simulation data is a :py:class:`pandas.DataFrame` whose columns are the SPICE variables stored in the file.

    Both, the types of simulation results and the variables in each,
    can be obtained with the standard dictionary/DataFrame methods.

    Example:
      >>> sim = read_raw("results.raw")
      >>> f = sim[RawResID.AC]['frequency']
      >>> vop = sim[RawResID.AC]['v(vop)']
    """
    try:
        warnings.showwarning = _showwarning
        ud = _format_for_user(_read_raw_file(fn, simid))
    except FileNotFoundError:
        print(f"open_raw: file {fn} not found.")
        return {}
    except PermissionError as err:
        print(f"open_raw: {err}.")
        return {}
    except ValueError:
        print(f"open_raw: the format of file {fn} not supported.")
        return {}
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    return ud
