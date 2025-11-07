<?php
# Mansooj CoderEngine — Direct Binding
# ------------------------------------
# Binds the native Mansooj library (PHP version)

require_once __DIR__ . '/../mansooj_loader.php';
require_once __DIR__ . '/coderconfig.php';

$LIB_PATH = _detect_lib();

# ─────────────────────────────────────────────
# FUNCTION BINDINGS (placeholders for mapping)
# ─────────────────────────────────────────────
$coder_engine_create   = 'coder_engine_create';
$coder_engine_init     = 'coder_engine_init';
$coder_engine_destroy  = 'coder_engine_destroy';
$coder_decode          = 'coder_decode';
$coder_encode          = 'coder_encode';
$coder_from_utf8       = 'coder_from_utf8';
$coder_to_utf8         = 'coder_to_utf8';
$decode_arabizi_ex     = 'decode_arabizi_ex';
$encode_arabizi_ex     = 'encode_arabizi_ex';
$coder_is_multibyte    = 'coder_is_multibyte';

# ─────────────────────────────────────────────
# CONFIG HELPERS
# ─────────────────────────────────────────────
function create_default_coder_config(): array {
    global $ENC_UTF8;
    return [
        "encoding" => $ENC_UTF8,
        "reversible" => true,
        "strict" => false,
        "auto_free" => true,
        "warn_on_invalid" => false,
        "normalize_output" => false,
        "decode_ex" => null,
        "encode_ex" => null
    ];
}

function create_custom_coder_config($encoding, $reversible, $strict, $warn_on_invalid, $normalize_output): array {
    return [
        "encoding" => $encoding,
        "reversible" => $reversible,
        "strict" => $strict,
        "auto_free" => true,
        "warn_on_invalid" => $warn_on_invalid,
        "normalize_output" => $normalize_output,
        "decode_ex" => null,
        "encode_ex" => null
    ];
}

function create_coder_engine(array $cfg) {
    return ["engine" => $cfg];
}

function init_coder_engine(&$engine, array $cfg): void {
    $engine["config"] = $cfg;
}

# ─────────────────────────────────────────────
# EXPORTS
# ─────────────────────────────────────────────
return [
    "coder_engine_create" => $coder_engine_create,
    "coder_engine_init" => $coder_engine_init,
    "coder_engine_destroy" => $coder_engine_destroy,
    "coder_decode" => $coder_decode,
    "coder_encode" => $coder_encode,
    "coder_from_utf8" => $coder_from_utf8,
    "coder_to_utf8" => $coder_to_utf8,
    "decode_arabizi_ex" => $decode_arabizi_ex,
    "encode_arabizi_ex" => $encode_arabizi_ex,
    "coder_is_multibyte" => $coder_is_multibyte
];
?>
