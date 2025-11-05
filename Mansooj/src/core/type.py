
# -*- coding: utf-8 -*-
"""
Mansooj Type Definitions
------------------------
Central shared types used across Mansooj modules.
This prevents circular imports and keeps type consistency.
"""

from typing import Literal

# Base value types allowed in Mansooj configs and runtime
ConfigValue = str | bool | int | float | None
ConfigDict = dict[str, ConfigValue]

# Font capability probe result
FontInfo = dict[str, bool | str | int | float | None]

# Common shorthand for Arabic processing results
GlyphForm = tuple[str, int]  # (character, form index)
GlyphList = list[GlyphForm]

# Aliases for pipeline configuration
LanguageCode = str  # e.g. "ar", "fa", "ur"
Direction = str      # "rtl" or "ltr"


# OutputMode for encoding
OutputMode = Literal[
    "utf-8",
    "utf16",
    "utf32",
    "cp1256",
    "cp864",
    "cp720",
    "cp1006",
    "iso_8859_6",
    "mac_arabic",
    "decimal",
    "unicode"
]

# Standard return maps for module summaries
SummaryDict = dict[str, ConfigValue]
