"""VELOCITY HINDI - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY HINDI"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "HINDI"
HANDLE = "@velocityhindi"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "hi",
    "name": "Hindi",
    "native_name": "हिन्दी",
    "history_key": "hindi",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "hi-IN-SwaraNeural",
    "native_fallback_voice": "hi-IN-MadhurNeural",
    "native_engine": "edge",
    "native_lang_code": "hi",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "हिन्दी",
    "translit_label": "ROMANIZED",
    "greeting": "नमस्ते!",
    "encouragement": "शानदार!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "NotoSansDevanagari-Bold.ttf",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Motivation", "प्रेरणा", "rocket", "#A560E8"),
    ("Love", "प्यार", "heart", "#FF4B4B"),
    ("Success", "सफलता", "trophy", "#F5A700"),
    ("Wisdom", "ज्ञान", "book", "#A560E8"),
    ("Happiness", "खुशी", "smile", "#F5A700"),
    ("Self Improvement", "आत्म सुधार", "leaf", "#58CC02"),
    ("Gratitude", "कृतज्ञता", "heart", "#FF7A00"),
    ("Friendship", "दोस्ती", "users", "#00A889"),
    ("Hope", "उम्मीद", "sun", "#FF7A00"),
    ("Creativity", "रचनात्मकता", "palette", "#E056A0"),
    ("Inner Peace", "आंतरिक शांति", "lotus", "#00A889"),
    ("Confidence", "आत्मविश्वास", "shield", "#1CB0F6"),
    ("Perseverance", "लगन", "mountain", "#FF7A00"),
    ("Inspiration", "प्रेरणा", "sparkles", "#A560E8"),
    ("Positive Life", "सकारात्मक जीवन", "sun", "#58CC02"),
    ("Courage", "साहस", "shield", "#FF4B4B"),
    ("Kindness", "दयालुता", "heart", "#E056A0"),
    ("Patience", "धैर्य", "hourglass", "#00A889"),
    ("Forgiveness", "क्षमा", "hands", "#FF7A00"),
    ("Strength", "ताकत", "dumbbell", "#FF4B4B"),
    ("Joy", "खुशी", "smile", "#F5A700"),
    ("Balance", "संतुलन", "scale", "#00A889"),
    ("Growth", "विकास", "sprout", "#58CC02"),
    ("Purpose", "उद्देश्य", "target", "#A560E8"),
    ("Mindfulness", "सचेतनता", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnhindi",
    "#hindilessons",
    "#hindiforbeginners",
    "#languagelearning",
    "#hindivocabulary",
    "#velocityhindi",
    "#dailyhindi",
    "#hindi",
    "#learnlanguages",
    "#speakhindi",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
