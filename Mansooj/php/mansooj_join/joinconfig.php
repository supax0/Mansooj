<?php
/**
 * Mansooj JoinEngine Config
 * -------------------------

 */

require_once __DIR__ . '/../mansoojdecoder/coderconfig.php';

/**
 * Callback type placeholders
 */
class CustomPolicyFn {
    public function __invoke($prev, $curr, $next) {}
}

class CustomOutputFilterFn {
    public function __invoke(&$joined, &$length) {}
}

/**
 * JoinConfig structure (matches C layout)
 */
class JoinConfig {
    public $coder_config;           // CoderConfig
    public int $encoding;           // int
    public $decode_ex;              // DecodeFnEx
    public $encode_ex;              // EncodeFnEx
    public bool $is_multibyte;
    public bool $reversible;
    public bool $allow_tatweel;
    public bool $skip_non_letters;
    public bool $include_glyphs;
    public bool $auto_free;
    public $custom_policy;          // CustomPolicyFn
    public $custom_output_filter;   // CustomOutputFilterFn
}

/**
 * JoinEngine structure (matches C layout)
 */
class JoinEngine {
    public $coder;                  // CoderEngine
    public bool $allow_tatweel;
    public bool $skip_non_letters;
    public bool $include_glyphs;
    public bool $auto_free;
    public $custom_policy;          // CustomPolicyFn
    public $custom_output_filter;   // CustomOutputFilterFn
}
?>
