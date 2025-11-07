"""
Mansooj Loader — internal
"""

import os
import platform
import ctypes

def _detect_lib() -> str:
    sysname = platform.system().lower()
    base = os.path.join(os.path.dirname(__file__), "../lib")

    if "darwin" in sysname:
        path = os.path.join(base, "macos", "mansoojlib.dylib")
    elif "linux" in sysname:
        path = os.path.join(base, "linux", "mansoojlib.so")
    elif "windows" in sysname:
        path = os.path.join(base, "windows", "mansoojlib.dll")
    else:
        raise OSError(f"Unsupported platform: {sysname}")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Mansooj library not found at: {path}")

    return os.path.realpath(path)

LIB_PATH = _detect_lib()
core = ctypes.CDLL(LIB_PATH)

__all__ = ["core", "LIB_PATH"]
