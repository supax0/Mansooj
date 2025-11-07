
import unittest
import ctypes as C


import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))


from mansooj_decoder.mansooj_coder import coder_engine_create, coder_decode, coder_encode
from mansooj_decoder.coderconfig import CoderConfig, ENC_UTF8
ENC_ARABIZI = 14  # from your enum

class TestArabiziFromArabic(unittest.TestCase):
    def test_arabic_to_arabizi(self):
        # Engine A: input Arabic bytes -> codepoints (UTF-8)
        cfg_in = CoderConfig(); cfg_in.encoding = ENC_UTF8
        cfg_in.is_multibyte = True; cfg_in.reversible = True; cfg_in.auto_free = True
        eng_in = coder_engine_create(C.byref(cfg_in))

        # Engine B: codepoints -> Arabizi bytes (Arabizi)
        cfg_out = CoderConfig(); cfg_out.encoding = ENC_ARABIZI
        cfg_out.is_multibyte = True; cfg_out.reversible = True; cfg_out.auto_free = True
        eng_out = coder_engine_create(C.byref(cfg_out))

        arabic = "مرحبا حبيبي"
        print(f"\n[Arabic] {arabic}")

        # Decode Arabic UTF-8 -> codepoints
        src = arabic.encode("utf-8")
        src_arr = (C.c_ubyte * len(src))(*src)
        codes = (C.c_int * (len(src) * 2))()
        n_codes = coder_decode(eng_in, src_arr, len(src), codes, len(codes))

        # Encode codepoints -> Arabizi ASCII
        out = (C.c_ubyte * (n_codes * 8))()
        n_bytes = coder_encode(eng_out, codes, n_codes, out, len(out))
        arabizi_bytes = bytes(out[:n_bytes])
        arabizi = arabizi_bytes.decode("ascii", errors="replace")

        print(f"[Arabizi] {arabizi}")
        self.assertTrue(len(arabizi) > 0)
        self.assertNotEqual(arabizi, arabic)

if __name__ == "__main__":
    unittest.main()
