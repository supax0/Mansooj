
"""

Mansooj Enhanced Configuration Layer with Harfbuzz and NLP Engine
---------------------------------------------------------
Advanced runtime configuration, font capability detection, optional Harfbuzz integration, and NLP capabilities.

This is the goal, hopefully.
"""


import os
import logging
from configparser import ConfigParser
from .type import ConfigDict, FontInfo, ConfigValue



# Optional Imports for JSON, YAML, Harfbuzz, and NLP tools (only if the specified has installed them)
try:
    import json
    Has_json = True
except ImportError:
    Has_json = False

try:
    import yaml
    Has_yaml = True
except ImportError:
    Has_yaml = False

try:
    import harfbuzz as hb
    Has_harfbuzz = True
except ImportError:
    Has_harfbuzz = False

# NLP Imports (Optional for lemmatization and tokenization)
try:
    from nlpengine import NLPEngine  # custom NLP engine ;)
    Has_nlp_engine = True
except ImportError:
    Has_nlp_engine = False

try:
    from fontTools.ttLib import TTFont
    Has_fonts_tools = True
except ImportError:
    Has_fonts_tools = False



# Configuration logging setup
logger = logging.getLogger("MansoojConfig")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)



# Predefined bit flags (using bitwise flags)
ENABLE_NONE = 0b0000        # No features enabled
ENABLE_SENTENCES = 0b0001   # Enable sentence-based functionality
ENABLE_WORDS = 0b0010       # Enable word-based functionality
ENABLE_LETTERS = 0b0100     # Enable letter-based functionality
ENABLE_ALL = 0b1111         # Enable all functionality (sentences + words + letters)


# Default configuration (type-safe)
Default: ConfigDict = {
    "language": "ar",                           # Default language is Arabic
    "enable": True,                             # Enable core functionality
    "ligatures": True,                          # Enable ligatures for Arabic characters
    "isolated": True,                           # Use isolated forms for characters
    "direction": "rtl",                         # Right-to-left text direction
    "support_zero_width_joined": True,          # Support zero-width joins (e.g., in Arabic ligatures)
    "remove_harket_joined": True,               # Remove Harakat (diacritics) when joined


}




# ---------------------------------------------------------------------
# Font capability detection with enhanced error handling
# ---------------------------------------------------------------------
def __Is_true_type__(font_path: str, enable_ligatures: bool = True) -> FontInfo:
    """
    Probe a TrueType/OpenType font for Arabic presentation forms.
    Returns: {"valid": bool, "ligatures": bool, "isolated": bool, "error": str?}
    """
    if not Has_fonts_tools:
        logger.error("fontTools not installed. Font detection will not work.")
        return {
            "valid": False,
            "error": "fontTools not installed",
            "ligatures": False,
            "isolated": False,
        }

    if not font_path or not os.path.exists(font_path):
        logger.error(f"Invalid font path: {font_path}")
        return {
            "valid": False,
            "error": f"invalid font path: {font_path}",
            "ligatures": False,
            "isolated": False,
        }

    try:
        ttfont = TTFont(font_path)
        cmap_tables = [t.cmap for t in ttfont["cmap"].tables]
        isolated_found = any(0xFE8D in cmap for cmap in cmap_tables)

        result: FontInfo = {"valid": True, "ligatures": False, "isolated": isolated_found}

        if enable_ligatures:
            lig_codepoints = [0xFEFB, 0xFEFC]  # “لا” ligatures
            result["ligatures"] = any(
                cp in cmap for cp in lig_codepoints for cmap in cmap_tables
            )

        ttfont.close()
        logger.info(f"Font '{font_path}' is valid for ligatures: {result['ligatures']}, isolated forms: {result['isolated']}")
        return result

    except Exception as e:
        logger.error(f"Error while processing font '{font_path}': {e}")
        return {"valid": False, "error": str(e), "ligatures": False, "isolated": False}

# ---------------------------------------------------------------------
# Enhanced Configuration Loader with Harfbuzz
# ---------------------------------------------------------------------
def auto_config(
    user_config: ConfigDict | None = None,
    config_file: str | None = None,
    section: str = "ArabicReshaper",
) -> ConfigDict:
    """
    Merge built-in defaults + optional file + user overrides into one ConfigDict.
    Ensures all values are type-safe and ConfigParser-compatible.
    """
    from Mansooj.src.core.config import Default

    cfg = ConfigParser()

    # --- 1. Normalize default values to strings (ConfigParser requires str)
    str_defaults = {k: "" if v is None else str(v) for k, v in Default.items()}
    cfg.read_dict({section: str_defaults})

    # --- 2. Optional external config (.ini or env)
    env_path = os.getenv("MANSOOJ_ARABIC_CONFIG_FILE")
    config_path = config_file or env_path

    if config_path and os.path.exists(config_path):
        logger.info(f"Loading configuration from file: {config_path}")
        cfg.read(config_path, encoding="utf-8")
    elif config_path:
        raise FileNotFoundError(f"Config file not found: {config_path}")

    # --- 3. User overrides (dict)
    if user_config:
        user_str = {k: "" if v is None else str(v) for k, v in user_config.items()}
        cfg.read_dict({section: user_str})

    if section not in cfg:
        raise ValueError(f"Missing [{section}] section in configuration")

    merged: ConfigDict = {}

    # --- 4. Type restoration: re-cast strings to original Default types
    for key, def_val in Default.items():
        raw = cfg[section].get(key, "")
        if raw == "" and def_val is None:
            merged[key] = None
        elif isinstance(def_val, bool):
            merged[key] = raw.lower() in ("1", "true", "yes", "on")
        elif isinstance(def_val, int):
            try:
                merged[key] = int(raw)
            except ValueError:
                merged[key] = def_val
        elif isinstance(def_val, bool) and key == "use_harfbuzz":
            # Enable Harfbuzz only if specified in the configuration
            merged[key] = raw.lower() in ("1", "true", "yes", "on")
        else:
            merged[key] = raw

    logger.info(f"Configuration loaded successfully. Values: {merged}")
    return merged
