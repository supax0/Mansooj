<?php
# Mansooj Test — Decoder Init


require_once __DIR__ . '/../../mansoojdecoder/coderconfig.php';
require_once __DIR__ . '/../../mansoojdecoder/mansooj_coder.php';

echo "Running Mansooj CoderEngine init test\n";

try {
    $cfg = create_default_coder_config();
    echo "→ Config created (encoding={$cfg['encoding']})\n";

    $engine = create_coder_engine($cfg);
    echo "→ Engine created successfully\n";

    init_coder_engine($engine, $cfg);
    echo "→ Engine initialized successfully\n";

    if ($engine["config"]["encoding"] === $cfg["encoding"]) {
        echo " Init verification passed\n";
    } else {
        echo "❌ Init verification failed\n";
    }

} catch (Throwable $e) {
    echo " Error: {$e->getMessage()}\n";
}
?>
