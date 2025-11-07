
"""
Mansooj CoderEngine Config
--------------------------
Defines enums, callback types, and structures for coderengine binding.
Matches
"""

import ctypes
from ctypes import (
    c_bool, c_int, c_size_t, POINTER, CFUNCTYPE, c_ubyte
)

# ─────────────────────────────────────────────
# ENCODING ENUM (matches base.h)
# ─────────────────────────────────────────────
ENC_RAW_BYTE            = 0
ENC_CP1256              = 1
ENC_ISO_8859_6          = 2
ENC_CP864               = 3
ENC_CP720               = 4
ENC_CP1006              = 5
ENC_MAC_ARABIC          = 6
ENC_PRES_FORMS_DECIMAL  = 7
ENC_ASCII               = 8
ENC_UTF8                = 9
ENC_UTF16_LE            = 10
ENC_UTF16_BE            = 11
ENC_UTF32_LE            = 12
ENC_UTF32_BE            = 13
ENC_ARABIZI             = 14
ENC_MANSOOJ_INTERNAL    = 15
ENC_HEX_STREAM          = 16   # (optional extension for hex dump enc)
ENC_BINARY_RAW          = 17   # (reserved for low-level binary engine)

# ─────────────────────────────────────────────
# CALLBACK TYPES
# ─────────────────────────────────────────────
DecodeFnEx = CFUNCTYPE(
    c_int,
    POINTER(c_ubyte),   # source bytes
    POINTER(c_size_t),  # offset pointer
    c_size_t,           # total length
    c_bool,             # strict mode
)

EncodeFnEx = CFUNCTYPE(
    c_size_t,
    c_int,              # codepoint
    POINTER(c_ubyte),   # destination buffer
    c_size_t,           # max length
)

CustomFilterFn = CFUNCTYPE(
    None,
    POINTER(c_int),     # pointer to codepoint array
    POINTER(c_size_t),  # pointer to length
)

# ─────────────────────────────────────────────
# STRUCTS (matches C side)
# ─────────────────────────────────────────────
class CoderEngine(ctypes.Structure):
    """typedef struct { ... } CoderEngine;"""
    _fields_ = [
        ("encoding", c_int),
        ("decode_ex", DecodeFnEx),
        ("encode_ex", EncodeFnEx),
        ("is_multibyte", c_bool),
        ("reversible", c_bool),
    ]


class CoderConfig(ctypes.Structure):
    """typedef struct { ... } CoderConfig;"""
    _fields_ = [
        ("encoding", c_int),
        ("decode_ex", DecodeFnEx),
        ("encode_ex", EncodeFnEx),
        ("is_multibyte", c_bool),
        ("reversible", c_bool),
        ("strict", c_bool),
        ("auto_free", c_bool),
        ("warn_on_invalid", c_bool),
        ("normalize_output", c_bool),
        ("custom_filter", CustomFilterFn),
    ]
