import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "0"))

# Get this value from @MissRose_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", None))

# Force Join Channel
MUST_JOIN = getenv("MUST_JOIN", "PBX_UPDATE")
