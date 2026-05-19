from Bad.Database import db

# Collections
usersdb = db.tgusersdb
chatsdb = db.tgchatsdb

# ═══════════════════════════════════════
# USERS DATABASE
# ═══════════════════════════════════════

async def is_served_user(user_id: int) -> bool:
    """Check if user exists in database"""
    return bool(await usersdb.find_one({"user_id": user_id}))


async def get_served_users() -> list:
    """Get all users from database"""
    return [user async for user in usersdb.find({"user_id": {"$gt": 0}})]


async def add_served_user(user_id: int):
    """Add user to database"""
    if await is_served_user(user_id):
        return
    await usersdb.insert_one({"user_id": user_id})


async def remove_served_user(user_id: int):
    """Remove user from database"""
    await usersdb.delete_one({"user_id": user_id})


async def get_served_users_count() -> int:
    """Get total users count"""
    return await usersdb.count_documents({"user_id": {"$gt": 0}})

# ═══════════════════════════════════════
# CHATS/GROUPS DATABASE
# ═══════════════════════════════════════

async def is_served_chat(chat_id: int) -> bool:
    """Check if chat exists in database"""
    return bool(await chatsdb.find_one({"chat_id": chat_id}))


async def get_served_chats() -> list:
    """Get all chats from database"""
    return [chat async for chat in chatsdb.find({"chat_id": {"$lt": 0}})]


async def add_served_chat(chat_id: int):
    """Add chat to database"""
    if await is_served_chat(chat_id):
        return
    await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    """Remove chat from database"""
    await chatsdb.delete_one({"chat_id": chat_id})


async def get_served_chats_count() -> int:
    """Get total chats count"""
    return await chatsdb.count_documents({"chat_id": {"$lt": 0}})
