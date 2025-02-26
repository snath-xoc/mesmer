# MESMER, land-climate dynamics group, S.I. Seneviratne
# Copyright (c) 2021 ETH Zurich, MESMER contributors listed in AUTHORS.
# Licensed under the GNU General Public License v3.0 or later see LICENSE or
# https://www.gnu.org/licenses/
"""
The mesmer package provides tools to train the MESMER emulator, create emulations, and
analyze the results.
"""
# flake8: noqa

from . import calibrate_mesmer, create_emulations, io, utils

try:
    from importlib.metadata import version as _get_version
except ImportError:
    # importlib.metadata not available in python 3.7
    import pkg_resources

    _get_version = lambda pkg: pkg_resources.get_distribution(pkg).version

try:
    __version__ = _get_version("mesmer-emulator")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"
