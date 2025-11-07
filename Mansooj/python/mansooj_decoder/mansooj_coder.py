
"""
Mansooj CoderEngine — Direct CTypes Binding
-------------------------------------------
Binds the native
"""

import ctypes

from ctypes import (
    c_int, c_size_t, c_char_p, c_ubyte, POINTER, c_bool, byref
)
from mansooj_loader import LIB_PATH
from .coderconfig import CoderConfig, CoderEngine, ENC_UTF8, DecodeFnEx,EncodeFnEx

# ─────────────────────────────────────────────
# Load shared Mansooj library
# ─────────────────────────────────────────────
_m = ctypes.CDLL(LIB_PATH)

# ─────────────────────────────────────────────
# FUNCTION BINDINGS
# ─────────────────────────────────────────────

# Lifecycle
_m.coder_engine_create.argtypes = [POINTER(CoderConfig)]
_m.coder_engine_create.restype = POINTER(CoderEngine)

_m.coder_engine_init.argtypes = [POINTER(CoderEngine), POINTER(CoderConfig)]
_m.coder_engine_init.restype = None

_m.coder_engine_destroy.argtypes = [POINTER(CoderEngine)]
_m.coder_engine_destroy.restype = None

# Core encode/decode
_m.coder_decode.argtypes = [
    POINTER(CoderEngine),
    POINTER(c_ubyte),
    c_size_t,
    POINTER(c_int),
    c_size_t,
]
_m.coder_decode.restype = c_size_t

_m.coder_encode.argtypes = [
    POINTER(CoderEngine),
    POINTER(c_int),
    c_size_t,
    POINTER(c_ubyte),
    c_size_t,
]
_m.coder_encode.restype = c_size_t

# UTF-8 helpers
_m.coder_from_utf8.argtypes = [POINTER(CoderEngine), c_char_p]
_m.coder_from_utf8.restype = POINTER(c_ubyte)

_m.coder_to_utf8.argtypes = [POINTER(CoderEngine), POINTER(c_ubyte), c_size_t]
_m.coder_to_utf8.restype = c_char_p

# Arabizi helpers
_m.decode_arabizi_ex.argtypes = [
    POINTER(c_ubyte),
    POINTER(c_size_t),
    c_size_t,
    c_bool,
]
_m.decode_arabizi_ex.restype = c_int

_m.encode_arabizi_ex.argtypes = [
    c_int,
    POINTER(c_ubyte),
    c_size_t,
]
_m.encode_arabizi_ex.restype = c_size_t

# Misc helper
_m.coder_is_multibyte.argtypes = [c_int]
_m.coder_is_multibyte.restype = c_bool




def create_default_coder_config():
    cfg = CoderConfig()
    cfg.encoding = ENC_UTF8
    cfg.reversible = True
    cfg.strict = False
    cfg.auto_free = True
    cfg.warn_on_invalid = False
    cfg.normalize_output = False
    cfg.decode_ex = DecodeFnEx()
    cfg.encode_ex = EncodeFnEx()
    return cfg


def create_custom_coder_config(encoding, reversible, strict, warn_on_invalid, normalize_output):
    cfg = CoderConfig()
    cfg.encoding = encoding
    cfg.reversible = reversible
    cfg.strict = strict
    cfg.auto_free = True          # enforced always true
    cfg.warn_on_invalid = warn_on_invalid
    cfg.normalize_output = normalize_output
    cfg.decode_ex = DecodeFnEx()
    cfg.encode_ex = EncodeFnEx()
    return cfg

def create_coder_engine(cfg):
    eng = _m.coder_engine_create(byref(cfg))
    if not eng:
        raise RuntimeError("coder_engine_create failed")
    return eng


def init_coder_engine(engine, cfg):
    _m.coder_engine_init(engine, byref(cfg))


# ─────────────────────────────────────────────
# PUBLIC EXPORTS
# ─────────────────────────────────────────────
coder_engine_create   = _m.coder_engine_create
coder_engine_init     = _m.coder_engine_init
coder_engine_destroy  = _m.coder_engine_destroy
coder_decode          = _m.coder_decode
coder_encode          = _m.coder_encode
coder_from_utf8       = _m.coder_from_utf8
coder_to_utf8         = _m.coder_to_utf8
decode_arabizi_ex     = _m.decode_arabizi_ex
encode_arabizi_ex     = _m.encode_arabizi_ex
coder_is_multibyte    = _m.coder_is_multibyte

__all__ = [
    "CoderEngine",
    "CoderConfig",
    "coder_engine_create",
    "coder_engine_init",
    "coder_engine_destroy",
    "coder_decode",
    "coder_encode",
    "coder_from_utf8",
    "coder_to_utf8",
    "decode_arabizi_ex",
    "encode_arabizi_ex",
    "coder_is_multibyte",
]
