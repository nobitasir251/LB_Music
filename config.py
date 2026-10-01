import os
import re

from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# ============================================================
# REQUIRED CONFIGURATION
# ============================================================

def get_required(name):
    value = getenv(name)

    if value is None or not value.strip():
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )

    return value.strip()


def get_int(name, default=None, required=False):
    value = getenv(name)

    if value is None or not value.strip():
        if required:
            raise RuntimeError(
                f"Missing required environment variable: {name}"
            )

        return default

    try:
        return int(value.strip())
    except ValueError:
        raise RuntimeError(
            f"Environment variable {name} must be a valid integer. "
            f"Got: {value!r}"
        )


def get_bool(name, default=False):
    value = getenv(name)

    if value is None:
        return default

    return value.strip().lower() in (
        "true",
        "1",
        "yes",
        "y",
        "on",
    )


# ============================================================
# TELEGRAM
# ============================================================

# Get these from https://my.telegram.org/apps
API_ID = get_int("API_ID", required=True)
API_HASH = get_required("API_HASH")

# Get this from @BotFather
BOT_TOKEN = get_required("BOT_TOKEN")


# ============================================================
# DATABASE / BOT
# ============================================================

# Get MongoDB URI from your MongoDB provider
MONGO_DB_URI = get_required("MONGO_DB_URI")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Music Bot")

PRIVATE_BOT_MODE = get_bool(
    "PRIVATE_BOT_MODE",
    default=False,
)


# ============================================================
# MUSIC SETTINGS
# ============================================================

DURATION_LIMIT_MIN = get_int(
    "DURATION_LIMIT",
    default=900,
)


# ============================================================
# LOGGING
# ============================================================

# Telegram group/channel IDs
LOGGER_ID = get_int(
    "LOGGER_ID",
    required=True,
)

LOG_GROUP_ID = get_int(
    "LOG_GROUP_ID",
    required=True,
)


# ============================================================
# OWNER
# ============================================================

OWNER_ID = get_int(
    "OWNER_ID",
    required=True,
)


# ============================================================
# HEROKU
# ============================================================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


# ============================================================
# UPSTREAM REPOSITORY
# ============================================================

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nobitasir251/LB_Music",
)

UPSTREAM_BRANCH = getenv(
    "UPSTREAM_BRANCH",
    "main",
)

GIT_TOKEN = getenv("GIT_TOKEN")


# ============================================================
# SUPPORT
# ============================================================

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/learningbots79",
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/learning_bots",
)


# ============================================================
# ASSISTANT / BROADCAST
# ============================================================

AUTO_LEAVING_ASSISTANT = get_bool(
    "AUTO_LEAVING_ASSISTANT",
    default=False,
)

AUTO_GCAST = get_bool(
    "AUTO_GCAST",
    default=False,
)

AUTO_GCAST_MSG = getenv(
    "AUTO_GCAST_MSG",
    "",
)


# ============================================================
# SPOTIFY
# ============================================================

# Prefer setting these in environment variables.
SPOTIFY_CLIENT_ID = get_required(
    "SPOTIFY_CLIENT_ID"
)

SPOTIFY_CLIENT_SECRET = get_required(
    "SPOTIFY_CLIENT_SECRET"
)


# ============================================================
# PLAYLIST LIMITS
# ============================================================

SERVER_PLAYLIST_LIMIT = get_int(
    "SERVER_PLAYLIST_LIMIT",
    default=50,
)

PLAYLIST_FETCH_LIMIT = get_int(
    "PLAYLIST_FETCH_LIMIT",
    default=25,
)


# ============================================================
# DOWNLOAD LIMITS
# ============================================================

SONG_DOWNLOAD_DURATION = get_int(
    "SONG_DOWNLOAD_DURATION_LIMIT",
    default=180,
)

SONG_DOWNLOAD_DURATION_LIMIT = get_int(
    "SONG_DOWNLOAD_DURATION_LIMIT",
    default=2000,
)


# ============================================================
# TELEGRAM FILE SIZE LIMITS
# ============================================================

# Audio: 100 MB
TG_AUDIO_FILESIZE_LIMIT = get_int(
    "TG_AUDIO_FILESIZE_LIMIT",
    default=104857600,
)

# Video: 1 GB
TG_VIDEO_FILESIZE_LIMIT = get_int(
    "TG_VIDEO_FILESIZE_LIMIT",
    default=1073741824,
)


# ============================================================
# PYROGRAM STRING SESSIONS
# ============================================================

STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")


# ============================================================
# RUNTIME DATA
# ============================================================

BANNED_USERS = filters.user()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


# ============================================================
# IMAGES
# ============================================================

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://te.legra.ph/file/62c76ac2095332a0ede75.jpg",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/4f59fb748e1990acfa297.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/14eb59ea7d31229d8d751.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://te.legra.ph/file/4310ea5f523520b2b765b.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://te.legra.ph/file/923c1faac33d8c70335dc.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://te.legra.ph/file/6c66f8b192532fe758e82.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://te.legra.ph/file/ebc4dc6357be06e08a3ed.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://te.legra.ph/file/d339f390ec168c19879c6.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://te.legra.ph/file/ee0cd53ab73f08f4a3627.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://te.legra.ph/file/5f9fb5bba66021c782d96.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://te.legra.ph/file/affe0afec5c7ad63676a4.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://te.legra.ph/file/3c446e8dee78ed0ca62ff.jpg",
)


# ============================================================
# TIME FUNCTIONS
# ============================================================

def time_to_seconds(time):
    stringt = str(time)

    return sum(
        int(x) * 60**i
        for i, x in enumerate(
            reversed(stringt.split(":"))
        )
    )


DURATION_LIMIT = int(
    time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
)


# ============================================================
# URL VALIDATION
# ============================================================

if SUPPORT_CHANNEL:
    if not re.match(
        r"^(?:http|https)://",
        SUPPORT_CHANNEL,
    ):
        raise SystemExit(
            "[ERROR] SUPPORT_CHANNEL URL is invalid. "
            "It must start with https://"
        )


if SUPPORT_CHAT:
    if not re.match(
        r"^(?:http|https)://",
        SUPPORT_CHAT,
    ):
        raise SystemExit(
            "[ERROR] SUPPORT_CHAT URL is invalid. "
            "It must start with https://"
        )
