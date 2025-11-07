// Mansooj CoderEngine — Direct Binding
// ------------------------------------
// Matches the structure of the Python CTypes binding exactly.
// No external dependencies, no FFI. Placeholder stubs only.

import { LIB_PATH } from "../mansooj_loader.js";
import { CoderConfig, CoderEngine, ENC } from "./coderconfig.js";

console.log("Mansooj CoderEngine loaded →", LIB_PATH);

// ─────────────────────────────────────────────
// FUNCTION BINDINGS (declaration only)
// ─────────────────────────────────────────────
export const _m = {
  coder_engine_create: "native:coder_engine_create",
  coder_engine_init: "native:coder_engine_init",
  coder_engine_destroy: "native:coder_engine_destroy",
  coder_decode: "native:coder_decode",
  coder_encode: "native:coder_encode",
  coder_from_utf8: "native:coder_from_utf8",
  coder_to_utf8: "native:coder_to_utf8",
  decode_arabizi_ex: "native:decode_arabizi_ex",
  encode_arabizi_ex: "native:encode_arabizi_ex",
  coder_is_multibyte: "native:coder_is_multibyte"
};

// ─────────────────────────────────────────────
// CONFIG HELPERS
// ─────────────────────────────────────────────
export function create_default_coder_config() {
  const cfg = new CoderConfig();
  cfg.encoding = ENC.UTF8;
  cfg.reversible = true;
  cfg.strict = false;
  cfg.auto_free = true;
  cfg.warn_on_invalid = false;
  cfg.normalize_output = false;
  cfg.decode_ex = "DecodeFnEx";
  cfg.encode_ex = "EncodeFnEx";
  return cfg;
}

export function create_custom_coder_config(
  encoding,
  reversible,
  strict,
  warn_on_invalid,
  normalize_output
) {
  const cfg = new CoderConfig();
  cfg.encoding = encoding;
  cfg.reversible = reversible;
  cfg.strict = strict;
  cfg.auto_free = true; // enforced always true
  cfg.warn_on_invalid = warn_on_invalid;
  cfg.normalize_output = normalize_output;
  cfg.decode_ex = "DecodeFnEx";
  cfg.encode_ex = "EncodeFnEx";
  return cfg;
}

// ─────────────────────────────────────────────
// ENGINE HELPERS
// ─────────────────────────────────────────────
export function create_coder_engine(cfg) {
  const eng = new CoderEngine();
  eng.encoding = cfg.encoding;
  eng.is_multibyte = cfg.is_multibyte;
  eng.reversible = cfg.reversible;
  eng.initialized = true;
  return eng;
}

export function init_coder_engine(engine, cfg) {
  engine.cfg = cfg;
}

// ─────────────────────────────────────────────
// PUBLIC EXPORTS
// ─────────────────────────────────────────────
export const coder_engine_create = _m.coder_engine_create;
export const coder_engine_init = _m.coder_engine_init;
export const coder_engine_destroy = _m.coder_engine_destroy;
export const coder_decode = _m.coder_decode;
export const coder_encode = _m.coder_encode;
export const coder_from_utf8 = _m.coder_from_utf8;
export const coder_to_utf8 = _m.coder_to_utf8;
export const decode_arabizi_ex = _m.decode_arabizi_ex;
export const encode_arabizi_ex = _m.encode_arabizi_ex;
export const coder_is_multibyte = _m.coder_is_multibyte;

export const __all__ = [
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
  "coder_is_multibyte"
];
