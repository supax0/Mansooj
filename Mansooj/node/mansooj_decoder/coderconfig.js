// Mansooj CoderEngine Config
// --------------------------


// ENCODING ENUM
export const ENC = {
  RAW_BYTE: 0,
  CP1256: 1,
  ISO_8859_6: 2,
  CP864: 3,
  CP720: 4,
  CP1006: 5,
  MAC_ARABIC: 6,
  PRES_FORMS_DECIMAL: 7,
  ASCII: 8,
  UTF8: 9,
  UTF16_LE: 10,
  UTF16_BE: 11,
  UTF32_LE: 12,
  UTF32_BE: 13,
  ARABIZI: 14,
  MANSOOJ_INTERNAL: 15,
  HEX_STREAM: 16,
  BINARY_RAW: 17
};

// STRUCTS (mock equivalents)
export class CoderEngine {
  constructor() {
    this.encoding = 0;
    this.decode_ex = null;
    this.encode_ex = null;
    this.is_multibyte = false;
    this.reversible = false;
  }
}

export class CoderConfig {
  constructor() {
    this.encoding = ENC.UTF8;
    this.decode_ex = null;
    this.encode_ex = null;
    this.is_multibyte = true;
    this.reversible = true;
    this.strict = false;
    this.auto_free = true;
    this.warn_on_invalid = false;
    this.normalize_output = false;
    this.custom_filter = null;
  }
}
