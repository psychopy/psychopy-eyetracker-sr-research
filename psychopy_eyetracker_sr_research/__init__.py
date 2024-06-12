# -*- coding: utf-8 -*-
# Part of the PsychoPy library
# Copyright (C) 2012-2020 iSolver Software Solutions (C) 2021 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

"""Extension package for PsychoPy which adds support for various hardware
devices by SR Research (via ioHub).
"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("psychopy-eyetracker-sr-research")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.dev"
