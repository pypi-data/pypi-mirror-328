#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""LISA Instrument module."""

import importlib_metadata

from .hexagon import Hexagon
from .instrument import Instrument

# Automatically set by `poetry dynamic-versioning`
__version__ = "1.8.0"


try:
    metadata = importlib_metadata.metadata("lisainstrument").json
    __author__ = metadata["author"]
    __email__ = metadata["author_email"]
except importlib_metadata.PackageNotFoundError:
    pass
