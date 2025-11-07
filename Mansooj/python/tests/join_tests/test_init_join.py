# -*- coding: utf-8 -*-
"""
JoinEngine — Initialization Unit Test
-------------------------------------
Verifies creation and initialization of Mansooj JoinEngine via CTypes binding.
"""

import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))


from mansooj_join.mansooj_join import (
    create_default_join_config,
    create_join_engine,
    init_join_engine,
)
class TestJoinEngineInit(unittest.TestCase):
    def test_join_engine_init(self):
        print("\nRunning Mansooj JoinEngine init test")

        cfg = create_default_join_config()
        self.assertIsNotNone(cfg, "JoinConfig creation failed")
        print(f"→ Config created (encoding={cfg.encoding})")

        eng = create_join_engine(cfg)
        self.assertIsNotNone(eng, "JoinEngine creation failed")
        print("→ Engine created")

        init_join_engine(eng, cfg)
        print("→ Engine initialized")

        # Basic validation
        self.assertTrue(hasattr(cfg, "encoding"))
        self.assertTrue(hasattr(eng, "contents") or hasattr(eng, "value"))
        print("✅ JoinEngine init verification passed")

if __name__ == "__main__":
    unittest.main(verbosity=2)
