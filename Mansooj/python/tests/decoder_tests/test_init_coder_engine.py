


import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
from mansooj_decoder.mansooj_coder import create_default_coder_config, create_coder_engine, init_coder_engine

class TestInitCoderEngine(unittest.TestCase):
    def test_init_coder_engine(self):
        cfg = create_default_coder_config()
        eng = create_coder_engine(cfg)
        init_coder_engine(eng, cfg)
        self.assertIsNotNone(eng)

if __name__ == "__main__":
    unittest.main()
