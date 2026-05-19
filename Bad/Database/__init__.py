from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
import sys
import logging

# Setup logger
LOGGER = logging.getLogger("BadStringBot.Database")

try:
    LOGGER.info("Connecting to MongoDB...")
    mongodb = AsyncIOMotorClient(MONGO_DB_URI)
    db = mongodb.BadStringBot
    LOGGER.info("✅ MongoDB connection initialized successfully!")
except Exception as e:
    LOGGER.error(f"❌ Error connecting to MongoDB: {e}")
    LOGGER.error("Please check your MONGO_DB_URI in config.py")
    sys.exit(1)
