# -*- coding: utf-8 -*-
import unittest
import ctypes as C
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
from mansooj_decoder.mansooj_coder import coder_engine_create, coder_from_utf8
from mansooj_decoder.coderconfig import CoderConfig, ENC_UTF8

class TestFromUtf8(unittest.TestCase):
    def test_from_utf8(self):
        cfg = CoderConfig()
        cfg.encoding = ENC_UTF8
        cfg.is_multibyte = True
        cfg.reversible = True
        cfg.auto_free = True
        eng = coder_engine_create(C.byref(cfg))

        text = "مرحبا"
        print(f"\n[Input UTF-8] → {text!r}")

        p_bytes = coder_from_utf8(eng, C.c_char_p(text.encode("utf-8")))
        self.assertIsNotNone(p_bytes)

        # Read raw bytes returned from C (until null terminator)
        i = 0
        raw = bytearray()
        while True:
            b = p_bytes[i]
            if b == 0:
                break
            raw.append(b)
            i += 1

        print(f"[Decoded Raw Bytes] → {raw}")
        try:
            print(f"[Decoded Text] → {raw.decode('utf-8', errors='replace')}")
        except Exception as e:
            print(f"[Decode Error] {e}")

if __name__ == "__main__":
    unittest.main()
