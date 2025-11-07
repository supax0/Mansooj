<?php
/**
 * Mansooj JoinEngine — Direct Binding (PHP)

 */

$loader   = include(__DIR__ . '/../mansooj_loader.php'); // once
$LIB_PATH = $loader['LIB_PATH'];

require_once __DIR__ . '/joinconfig.php';
require_once __DIR__ . '/../mansoojdecoder/coderconfig.php';

/** Native symbol placeholders (1:1 with C names) */
class _m {
    public static $connects_forward            = 'native:connects_forward';
    public static $connects_backward           = 'native:connects_backward';
    public static $join_engine_create          = 'native:join_engine_create';
    public static $join_engine_init            = 'native:join_engine_init';
    public static $join_engine_destroy         = 'native:join_engine_destroy';
    public static $set_custom_policy           = 'native:set_custom_policy';
    public static $default_joining_type        = 'native:default_joining_type';
    public static $join_text                   = 'native:join_text';
    public static $mansooj_init_join           = 'native:mansooj_init_join';
    // public static $mansooj_cleanup_join     = 'native:mansooj_cleanup_join'; // not used
    public static $is_join_punctuation         = 'native:is_join_punctuation';
    public static $join_swap_punctuation_text  = 'native:join_swap_punctuation_text';
    public static $join_swap_words             = 'native:join_swap_words';
    public static $join_text_mixed             = 'native:join_text_mixed';
    public static $join_engine_swap_word       = 'native:join_engine_swap_word';
}

/** Config helpers (names match Python) */
function create_default_join_config(): JoinConfig {
    $cfg = new JoinConfig();

    $coder = new CoderConfig();
    $coder->encoding          = 9;        // ENC_UTF8
    $coder->is_multibyte      = true;
    $coder->reversible        = true;
    $coder->strict            = false;
    $coder->auto_free         = true;
    $coder->warn_on_invalid   = false;
    $coder->normalize_output  = false;
    $coder->decode_ex         = new DecodeFnEx();
    $coder->encode_ex         = new EncodeFnEx();

    $cfg->coder_config        = $coder;
    $cfg->encoding            = 9;        // ENC_UTF8
    $cfg->decode_ex           = new DecodeFnEx();
    $cfg->encode_ex           = new EncodeFnEx();
    $cfg->is_multibyte        = true;
    $cfg->reversible          = true;
    $cfg->allow_tatweel       = true;
    $cfg->skip_non_letters    = true;
    $cfg->include_glyphs      = false;
    $cfg->auto_free           = true;
    $cfg->custom_policy       = new CustomPolicyFn();
    $cfg->custom_output_filter= new CustomOutputFilterFn();
    return $cfg;
}

function create_join_engine(JoinConfig $cfg): JoinEngine {
    // placeholder: native would allocate; we mirror Python return type
    $eng = new JoinEngine();
    $eng->coder               = $cfg->coder_config;
    $eng->allow_tatweel       = $cfg->allow_tatweel;
    $eng->skip_non_letters    = $cfg->skip_non_letters;
    $eng->include_glyphs      = $cfg->include_glyphs;
    $eng->auto_free           = $cfg->auto_free;
    $eng->custom_policy       = $cfg->custom_policy;
    $eng->custom_output_filter= $cfg->custom_output_filter;
    $eng->cfg                 = $cfg; // mirror Python helper behavior
    return $eng;
}

function init_join_engine(JoinEngine $engine, JoinConfig $cfg): void {
    // placeholder: native call; mirror Python signature
    $engine->cfg = $cfg;
}

/** Public exports (names match Python __all__) */
$connects_forward            = _m::$connects_forward;
$connects_backward           = _m::$connects_backward;
$join_engine_create          = _m::$join_engine_create;
$join_engine_init            = _m::$join_engine_init;
$join_engine_destroy         = _m::$join_engine_destroy;
$set_custom_policy           = _m::$set_custom_policy;
$default_joining_type        = _m::$default_joining_type;
$join_text                   = _m::$join_text;
$mansooj_init_join           = _m::$mansooj_init_join;
// $mansooj_cleanup_join     = _m::$mansooj_cleanup_join;
$is_join_punctuation         = _m::$is_join_punctuation;
$join_swap_punctuation_text  = _m::$join_swap_punctuation_text;
$join_swap_words             = _m::$join_swap_words;
$join_text_mixed             = _m::$join_text_mixed;
$join_engine_swap_word       = _m::$join_engine_swap_word;
