

"""
Arabic Table
--------------------
Pure data layer — no logic, no functions.
Defines core joining maps and Unicode directional constants.
"""

# ─── Shape Indexes ────────────────────────────────
Is_isolated = 0b00001  # 1
Is_initial  = 0b00010  # 2
Is_medial   = 0b00100  # 4
Is_final    = 0b01000  # 8
Is_unshaped = 0b10000  # 16 (used to represent unshaped text)

# ─── Special Marks ────────────────────────────────
Tatweel            = '\u0640'   # ــ
Zero_width_joined  = '\uFEFF'   # ZWJ / BOM
Zero_width_nonjoin = '\u200C'   # ZWNJ
Zero_width_space   = '\u200B'   # ZWS

# ─── Directional Marks ────────────────────────────
RLM = "\u200F"   # Right-to-Left Mark
RLE = "\u202B"   # RTL Embedding
PDF = "\u202C"   # Pop Directional Formatting
LRE = "\u202A"   # LTR Embedding
LRM = "\u200E"   # Left-to-Right Mark

# ─── Non-forward connecting letters ───────────────
# Letters that do NOT connect to following letters
No_forward_connect = {
    "ا": "\u0627",  # ALEF
    "د": "\u062F",  # DAL
    "ذ": "\u0630",  # THAL
    "ر": "\u0631",  # REH
    "ز": "\u0632",  # ZAIN
    "و": "\u0648",  # WAW
    "ؤ": "\u0624",  # WAW WITH HAMZA ABOVE
    "ء": "\u0621",  # HAMZA
}
