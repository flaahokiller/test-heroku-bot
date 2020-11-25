#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from botname import LOG
from os.path import dirname, basename, isfile
import glob


def list_funcs():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_funcs = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_funcs


ALL_FUNCS = sorted(list_funcs())
LOG.info("funcs loaded: %s", str(ALL_FUNCS))
__all__ = ALL_FUNCS + ["ALL_FUNCS"]
