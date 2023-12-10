from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="desatuak")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="XV_SUPPORT")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="LocalMemo")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = "Spamxmoan_bot"
    BOT_ID = "6654681821"
    BOT_NAME = "SpamxMoan"
    owner_username = "xexenid"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6654681821:AAEW1l-PsFFYctn0Ruh8Srd8zcCXa0956tg"
    API_ID = 27125828  # Your APP_ID from Telegram
    API_HASH = "0220766f8c8ca1a28b12a9356ada0925"  # Your APP_HASH from Telegram
    OWNER_ID = 1563707058 # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001683506649 # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://desatuak:bimakeren321@cluster0.od1yy2z.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "desatuak"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "XV_SUPPORT"
    SUPPORT_CHANNEL = "LocalMemo"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
