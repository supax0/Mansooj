



"""
Mansooj JoinEngine — Direct CTypes Binding
------------------------------------------

"""

import ctypes
from ctypes import c_int, c_bool, c_char_p, POINTER

from mansooj_loader import LIB_PATH
from .joinconfig import (
    JoinEngine,
    JoinConfig,
    CustomPolicyFn,
    CustomOutputFilterFn,
)
from mansooj_decoder.coderconfig import (
    CoderConfig,
    DecodeFnEx,
    EncodeFnEx,
    ENC_UTF8,
)

# ─────────────────────────────────────────────
# Load native lib
# ─────────────────────────────────────────────
_m = ctypes.CDLL(LIB_PATH)

# ─────────────────────────────────────────────
# Bindings (signatures must match C exactly)
# ─────────────────────────────────────────────

# Connectivity checks
_m.connects_forward.argtypes = [POINTER(c_int)]
_m.connects_forward.restype = c_bool

_m.connects_backward.argtypes = [POINTER(c_int)]
_m.connects_backward.restype = c_bool

# Engine lifecycle (note: Create takes JoinConfig*)
_m.join_engine_create.argtypes = [POINTER(JoinConfig)]
_m.join_engine_create.restype = POINTER(JoinEngine)

# Init takes (JoinEngine*, JoinConfig*)
_m.join_engine_init.argtypes = [POINTER(JoinEngine), POINTER(JoinConfig)]
_m.join_engine_init.restype = None

_m.join_engine_destroy.argtypes = [POINTER(JoinEngine)]
_m.join_engine_destroy.restype = None

# Policy configuration
_m.set_custom_policy.argtypes = [
    POINTER(JoinEngine),
    ctypes.CFUNCTYPE(None, c_char_p, c_char_p, c_char_p),
]
_m.set_custom_policy.restype = None

# Default joining logic
_m.default_joining_type.argtypes = [c_int, c_int, c_int]
_m.default_joining_type.restype = c_int

# Core processing
_m.join_text.argtypes = [POINTER(JoinEngine), c_char_p]
_m.join_text.restype = None

# Runtime integration
_m.mansooj_init_join.argtypes = [ctypes.c_void_p, POINTER(JoinConfig)]
_m.mansooj_init_join.restype = c_int


# The goal of this function is to give control over join engine cleanup
# But it is not fully implemented yet. so keep clean to auto true and dont use those yet.
# _m.mansooj_cleanup_join.argtypes = [ctypes.c_void_p]
# _m.mansooj_cleanup_join.restype = None

# Punctuation helpers
_m.is_join_punctuation.argtypes = [c_int]
_m.is_join_punctuation.restype = c_bool

_m.join_swap_punctuation_text.argtypes = [c_char_p]
_m.join_swap_punctuation_text.restype = c_char_p

# Word swapping
_m.join_swap_words.argtypes = [c_char_p, c_bool]
_m.join_swap_words.restype = c_char_p

# Mixed text processing
_m.join_text_mixed.argtypes = [POINTER(JoinEngine), c_char_p]
_m.join_text_mixed.restype = None

# Swap a specific word via engine
_m.join_engine_swap_word.argtypes = [
    POINTER(JoinEngine),
    c_char_p,
    c_char_p,
    c_char_p,
]
_m.join_engine_swap_word.restype = c_char_p

# ─────────────────────────────────────────────
# Config helpers (no *args, no annotations)
# ─────────────────────────────────────────────

def create_default_join_config():
    cfg = JoinConfig()

    coder = CoderConfig()
    coder.encoding = ENC_UTF8
    coder.is_multibyte = True
    coder.reversible = True
    coder.strict = False
    coder.auto_free = True          # enforced auto-clean on coder
    coder.warn_on_invalid = False
    coder.normalize_output = False
    coder.decode_ex = DecodeFnEx()  # NULL → use built-in by encoding
    coder.encode_ex = EncodeFnEx()

    cfg.coder_config = coder
    cfg.encoding = ENC_UTF8
    cfg.decode_ex = DecodeFnEx()    # NULL → use built-in by encoding
    cfg.encode_ex = EncodeFnEx()
    cfg.is_multibyte = True
    cfg.reversible = True
    cfg.allow_tatweel = True
    cfg.skip_non_letters = True
    cfg.include_glyphs = False
    cfg.auto_free = True            # enforced auto-clean on engine
    cfg.custom_policy = CustomPolicyFn()
    cfg.custom_output_filter = CustomOutputFilterFn()
    return cfg


def create_join_engine(cfg):
    """Allocate engine from config (JoinConfig* → JoinEngine*)."""
    eng_ptr = _m.join_engine_create(ctypes.byref(cfg))
    if not eng_ptr:
        raise RuntimeError("join_engine_create failed")
    return eng_ptr


def init_join_engine(engine, cfg):
    """Init an existing engine with config (JoinEngine*, JoinConfig*)."""
    _m.join_engine_init(engine, ctypes.byref(cfg))


# ─────────────────────────────────────────────
# Public exports
# ─────────────────────────────────────────────
connects_forward           = _m.connects_forward
connects_backward          = _m.connects_backward
join_engine_create         = _m.join_engine_create
join_engine_init           = _m.join_engine_init
join_engine_destroy        = _m.join_engine_destroy
set_custom_policy          = _m.set_custom_policy
default_joining_type       = _m.default_joining_type
join_text                  = _m.join_text
mansooj_init_join          = _m.mansooj_init_join
# mansooj_cleanup_join       = _m.mansooj_cleanup_join #dont use this yet.
is_join_punctuation        = _m.is_join_punctuation
join_swap_punctuation_text = _m.join_swap_punctuation_text
join_swap_words            = _m.join_swap_words
join_text_mixed            = _m.join_text_mixed
join_engine_swap_word      = _m.join_engine_swap_word

__all__ = [
    "JoinEngine",
    "JoinConfig",
    "connects_forward",
    "connects_backward",
    "join_engine_create",
    "join_engine_init",
    "join_engine_destroy",
    "set_custom_policy",
    "default_joining_type",
    "join_text",
    "mansooj_init_join",
    # "mansooj_cleanup_join",  # dont use this yet.
    "is_join_punctuation",
    "join_swap_punctuation_text",
    "join_swap_words",
    "join_text_mixed",
    "join_engine_swap_word",
    "create_default_join_config",
    "create_join_engine",
    "init_join_engine",
]
