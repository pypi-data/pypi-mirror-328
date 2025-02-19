<!--
SPDX-FileCopyrightText: 2025 Federico Beffa <beffa@fbengineering.ch>

SPDX-License-Identifier: CC-BY-4.0
-->

# FBESpice

Python library to interact with SPICE-like circuit simulators.

For analog-/mixed-signal design engineers a schematic is a graphical language conveying much more than the connectivity of devices. A good schematic, on top of connectivity, provides information about required matching properties and strategies, information relevant for reliability, nodes where parasitic resistance and/or capacitance is critically important, etc. 
Current days netlist formats only capture connectivity information. Therefore, in the analog-/mixed-signal, RF and mmW worlds, netlists can not be seen as substitutes for schematics. However, a circuit netlist is necessary for simulation, and it's usually generated automatically from schematics.

Unfortunately, open-source SPICE-like simulators are quite restrictive in the accepted netlist format. For example, the [Xyce](https://xyce.sandia.gov) simulator offers advanced Harmonic-Balance simulation capabilities, but it's not possible to specify the fundamental frequencies through variables. Therefore, for every test frequency, it's necessary to change their values in several places (sources, simulation statements, ...) which is tedious and error-prone. To solve this problem, this library introduces the concept of a [meta-netlist](https://fbengineering.gitlab.io/fbespice/intro.html) which is similar to a netlist, but with holes where you can insert the value of meta-variables. The flow is then:

1. Generate the meta-netlist from a schematic.
2. Convert the meta-netlist into a final netlist from a Pytohn program or REPL.
3. Run the simulation.
4. Analyse the results in Python (or by other means).

This flow is easily amenable to a complete and automated characterisation over PVT of a system or circuit. For more details see the [documentation](https://fbengineering.gitlab.io/fbespice).

Dependencies
------------

`fbespice` depends on the following Python libraries:

* NumPy
* Pandas

Installation
------------

`fbespice` is available on [PyPi](https://pypi.org/). The easiest way to install it on Unix-like systems is via `pip`:

```bash
pip install fbespice
```

Alternatively you can download the Python distribution archives from the release page, or download the source code and add its location to the environment variable `PYTHONPATH`.
