<?php
/**
 * Mansooj JoinEngine — Initialization Unit Test
 * ---------------------------------------------
 */

require_once __DIR__ . '/../../mansooj_join/mansooj_join.php';

echo "\nRunning Mansooj JoinEngine init test\n";

try {
    $cfg = create_default_join_config();
    if (!$cfg) throw new Exception("JoinConfig creation failed");
    echo "→ Config created (encoding={$cfg->encoding})\n";

    $eng = create_join_engine($cfg);
    if (!$eng) throw new Exception("JoinEngine creation failed");
    echo "→ Engine created\n";

    init_join_engine($eng, $cfg);
    echo "→ Engine initialized\n";

    if (!property_exists($cfg, "encoding"))
        throw new Exception("Missing encoding field");
    if (!property_exists($eng, "cfg"))
        throw new Exception("Engine missing cfg link");

    echo "JoinEngine init verification passed\n";
} catch (Exception $e) {
    echo "Error: {$e->getMessage()}\n";
    exit(1);
}
