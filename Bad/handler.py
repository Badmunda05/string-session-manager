from pyrogram import Client, filters
from pyrogram.types import Message
from Bad.Database.users import add_served_chat, remove_served_chat

# ══════════════════════════════════════
# AUTO ADD GROUP TO DATABASE
# ══════════════════════════════════════

@Client.on_message(filters.group, group=10)
async def group_tracker(client: Client, message: Message):
    """Track when bot is added to groups"""
    await add_served_chat(message.chat.id)


# ══════════════════════════════════════
# REMOVE GROUP WHEN BOT LEAVES
# ══════════════════════════════════════

@Client.on_message(filters.left_chat_member)
async def left_chat_handler(client: Client, message: Message):
    """Remove group from database when bot is kicked"""
    if message.left_chat_member.id == (await client.get_me()).id:
        await remove_served_chat(message.chat.id)
