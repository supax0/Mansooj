<?php
/**
 * Mansooj CoderEngine Config
 * --------------------------
 * Defines enums, callback types, and structures for coderengine binding.
 */

// ─────────────────────────────────────────────
// ENCODING ENUM (matches base.h)
// ─────────────────────────────────────────────
const ENC_RAW_BYTE            = 0;
const ENC_CP1256              = 1;
const ENC_ISO_8859_6          = 2;
const ENC_CP864               = 3;
const ENC_CP720               = 4;
const ENC_CP1006              = 5;
const ENC_MAC_ARABIC          = 6;
const ENC_PRES_FORMS_DECIMAL  = 7;
const ENC_ASCII               = 8;
const ENC_UTF8                = 9;
const ENC_UTF16_LE            = 10;
const ENC_UTF16_BE            = 11;
const ENC_UTF32_LE            = 12;
const ENC_UTF32_BE            = 13;
const ENC_ARABIZI             = 14;
const ENC_MANSOOJ_INTERNAL    = 15;
const ENC_HEX_STREAM          = 16;  // optional extension for hex dump enc
const ENC_BINARY_RAW          = 17;  // reserved for low-level binary engine

// ─────────────────────────────────────────────
// CALLBACK TYPES (placeholders for callable refs)
// ─────────────────────────────────────────────
class DecodeFnEx {}
class EncodeFnEx {}
class CustomFilterFn {}

// ─────────────────────────────────────────────
// STRUCTS (matches C side)
// ─────────────────────────────────────────────
class CoderEngine {
    public int $encoding;
    public ?DecodeFnEx $decode_ex;
    public ?EncodeFnEx $encode_ex;
    public bool $is_multibyte;
    public bool $reversible;
}

class CoderConfig {
    public int $encoding;
    public ?DecodeFnEx $decode_ex;
    public ?EncodeFnEx $encode_ex;
    public bool $is_multibyte;
    public bool $reversible;
    public bool $strict;
    public bool $auto_free;
    public bool $warn_on_invalid;
    public bool $normalize_output;
    public ?CustomFilterFn $custom_filter;
}
?>
