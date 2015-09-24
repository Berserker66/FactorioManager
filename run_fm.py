#! python3
# coding=utf-8
__author__ = 'Fabian'

import runpy
from multiprocessing import freeze_support
if __name__ == "__main__":
    freeze_support()
    runpy.run_module('FactorioManager', run_name="__main__")

if False:
    import omnitool  # freeze hook

