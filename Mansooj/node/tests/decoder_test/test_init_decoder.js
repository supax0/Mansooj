// Mansooj JS Test — Decoder Init
const path = require("path");
const {
  create_default_coder_config,
  create_coder_engine,
  init_coder_engine
} = require(path.resolve(__dirname, "../../mansooj_decoder/mansooj_coder.js"));

console.log(" Running Mansooj CoderEngine Init Test (JS)");

try {
  const cfg = create_default_coder_config();
  console.log(`→ Config created (encoding=${cfg.encoding})`);

  const engine = create_coder_engine(cfg);
  console.log("→ Engine created");

  init_coder_engine(engine, cfg);
  console.log("→ Engine initialized");

  if (engine.cfg.encoding === cfg.encoding)
    console.log("Init verification passed");
  else
    console.log("❌ Init verification failed");
} catch (e) {
  console.error(" Error:", e.message);
}
