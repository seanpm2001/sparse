import ctypes
import os
import pathlib

from mlir.ir import Context

DEBUG = bool(int(os.environ.get("DEBUG", "0")))
SCRIPT_PATH = pathlib.Path(__file__).parent

MLIR_C_RUNNER_UTILS = ctypes.util.find_library("mlir_c_runner_utils")
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.free.argtypes = [ctypes.c_void_p]
libc.free.restype = None

# TODO: remove global state
ctx = Context()
