
# -*- coding: utf-8 -*-
"""
Mansooj JoinEngine Config
--------------------------
Defines enums, callback types, and structures for joinengine binding.

"""

import ctypes
from ctypes import (
    c_bool, c_int, c_size_t, c_char_p, POINTER, CFUNCTYPE
)
from mansooj_decoder.coderconfig import CoderEngine, CoderConfig, DecodeFnEx, EncodeFnEx

# ─────────────────────────────────────────────
# CALLBACK TYPES
# ─────────────────────────────────────────────

CustomPolicyFn = CFUNCTYPE(
    None,
    c_char_p,  # prev char pointer
    c_char_p,  # curr char pointer
    c_char_p,  # next char pointer
)

CustomOutputFilterFn = CFUNCTYPE(
    None,
    POINTER(c_int),     # joined codepoints
    POINTER(c_size_t),  # length
)


# ─────────────────────────────────────────────
# JoinConfig and JoinEngine
# ─────────────────────────────────────────────
class JoinConfig(ctypes.Structure):
    _fields_ = [
        ("coder_config", CoderConfig),
        ("encoding", c_int),
        ("decode_ex", DecodeFnEx),
        ("encode_ex", EncodeFnEx),
        ("is_multibyte", c_bool),
        ("reversible", c_bool),
        ("allow_tatweel", c_bool),
        ("skip_non_letters", c_bool),
        ("include_glyphs", c_bool),
        ("auto_free", c_bool),
        ("custom_policy", CustomPolicyFn),
        ("custom_output_filter", CustomOutputFilterFn),
    ]


# ─────────────────────────────────────────────
# STRUCTS (matches C side)
# ─────────────────────────────────────────────

class JoinEngine(ctypes.Structure):
    """typedef struct { ... } JoinEngine;"""
    _fields_ = [
        ("coder", CoderEngine),
        ("allow_tatweel", c_bool),
        ("skip_non_letters", c_bool),
        ("include_glyphs", c_bool),
        ("auto_free", c_bool),
        ("custom_policy", CustomPolicyFn),
        ("custom_output_filter", CustomOutputFilterFn),
    ]
