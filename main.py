import time
import logging
import asyncio

import config
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.errors import (
    ApiIdInvalid,
    ApiIdPublishedFlood,
    AccessTokenInvalid,
)

# ──────────────────────────────────────
# Logging Configuration
# ──────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

# Reduce Mongo noise
logging.getLogger("pymongo").setLevel(logging.WARNING)

LOGGER = logging.getLogger("BadStringBot")

# ──────────────────────────────────────
# Start Time
# ──────────────────────────────────────
START_TIME = time.time()

# ──────────────────────────────────────
# Pyrogram Client
# ──────────────────────────────────────
app = Client(
    name="BadStringBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="Bad"),  # plugins folder
)

# ──────────────────────────────────────
# Main Runner
# ──────────────────────────────────────
def main():
    LOGGER.info("🚀 Bad String Session Manager starting...")

    try:
        app.start()

    except ApiIdInvalid:
        LOGGER.error("❌ Invalid API_ID")
        raise SystemExit(1)

    except ApiIdPublishedFlood:
        LOGGER.error("❌ API_ID / API_HASH flood banned")
        raise SystemExit(1)

    except AccessTokenInvalid:
        LOGGER.error("❌ Invalid BOT_TOKEN")
        raise SystemExit(1)

    except Exception as e:
        LOGGER.exception(f"❌ Unexpected error while starting bot: {e}")
        raise SystemExit(1)

    # Bot info
    me = app.get_me()
    LOGGER.info(f"✅ Bot started successfully: @{me.username}")
    LOGGER.info("⚙️ Features enabled: String Generation + Session Utilities")

    # Send "I am alive" message to LOGGER_ID
    try:
        app.send_message(
            config.LOGGER_ID,
            f"**✅ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n"
            f"**ʙᴏᴛ :** @{me.username}\n"
            f"**ɴᴀᴍᴇ :** {me.first_name}\n"
            f"**ɪᴅ :** `{me.id}`\n"
            f"**sᴛᴀᴛᴜs :** ɪ ᴀᴍ ᴀʟɪᴠᴇ 🏴‍☠️"
        )
        LOGGER.info(f"✅ Alive message sent to LOGGER_ID: {config.LOGGER_ID}")

    except Exception as e:
        LOGGER.exception("❌ Failed to send alive message")

    # Idle (keep alive)
    idle()

    # Shutdown
    LOGGER.info("🛑 Stopping bot...")
    app.stop()
    LOGGER.info("✅ Bot stopped cleanly")


# ──────────────────────────────────────
# Entry Point
# ──────────────────────────────────────
if __name__ == "__main__":
    main()
