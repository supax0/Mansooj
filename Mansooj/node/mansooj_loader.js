// Mansooj Loader — internal
import path from "path";
import fs from "fs";
import os from "os";

export function detectLib() {
  const sys = os.platform().toLowerCase();
  const base = path.join(path.dirname(new URL(import.meta.url).pathname), "../lib");

  let libPath;
  if (sys.includes("darwin")) libPath = path.join(base, "macos", "mansoojlib.dylib");
  else if (sys.includes("linux")) libPath = path.join(base, "linux", "mansoojlib.so");
  else if (sys.includes("win")) libPath = path.join(base, "windows", "mansoojlib.dll");
  else throw new Error(`Unsupported platform: ${sys}`);

  if (!fs.existsSync(libPath))
    throw new Error(`Mansooj library not found at: ${libPath}`);

  return path.resolve(libPath);
}

export const LIB_PATH = detectLib();
