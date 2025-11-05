
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

}
