import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from config import OWNER_ID
from Bad.Database.users import get_served_users, get_served_chats

logger = logging.getLogger(__name__)

# Global broadcast lock
IS_BROADCASTING = False
broadcast_lock = asyncio.Lock()

# ═══════════════════════════════════════
# BROADCAST COMMAND
# ═══════════════════════════════════════

@Client.on_message(
    filters.command(["broadcast", "gcast", "gcat"], prefixes=["/", "!", "."]) 
    & filters.user(OWNER_ID)
)
async def broadcast_message(client: Client, message: Message):
    """
    Broadcast messages to all users and groups
    
    Usage:
    /broadcast <text> - Broadcast text to groups
    /broadcast -user <text> - Broadcast to users only
    /broadcast -nogroup <text> - Skip groups
    /broadcast -pin <text> - Broadcast and pin (silent)
    /broadcast -pinloud <text> - Broadcast and pin (with notification)
    
    Or reply to a message with /broadcast
    """
    global IS_BROADCASTING
    
    async with broadcast_lock:
        if IS_BROADCASTING:
            return await message.reply_text(
                "**⚠️ ᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴘʀᴏɢʀᴇss.**\n\n"
                "» ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ ɪᴛ ᴛᴏ ᴄᴏᴍᴘʟᴇᴛᴇ."
            )

        IS_BROADCASTING = True
        
        try:
            # Parse command and flags
            try:
                query = message.text.split(None, 1)[1].strip()
            except IndexError:
                query = ""
            except Exception as eff:
                IS_BROADCASTING = False
                return await message.reply_text(f"**❌ ᴇʀʀᴏʀ:** {eff}")
            
            # Check if replying to a message
            if message.reply_to_message:
                broadcast_content = message.reply_to_message
                broadcast_type = "reply"
                flags = {
                    "-pin": "-pin" in query,
                    "-pinloud": "-pinloud" in query,
                    "-nogroup": "-nogroup" in query,
                    "-user": "-user" in query,
                }
            else:
                if len(message.command) < 2:
                    IS_BROADCASTING = False
                    return await message.reply_text(
                        "**☞︎︎︎ ᴜsᴀɢᴇ:**\n\n"
                        "» `/broadcast <text>` - ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴏ ɢʀᴏᴜᴘs\n"
                        "» `/broadcast -user <text>` - ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴏ ᴜsᴇʀs\n"
                        "» `/broadcast -pin <text>` - ʙʀᴏᴀᴅᴄᴀsᴛ & ᴘɪɴ (sɪʟᴇɴᴛ)\n"
                        "» `/broadcast -pinloud <text>` - ʙʀᴏᴀᴅᴄᴀsᴛ & ᴘɪɴ (ʟᴏᴜᴅ)\n"
                        "» `/broadcast -nogroup <text>` - sᴋɪᴘ ɢʀᴏᴜᴘs\n\n"
                        "**ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ** `/broadcast`"
                    )
                
                # Parse flags
                flags = {
                    "-pin": "-pin" in query,
                    "-pinloud": "-pinloud" in query,
                    "-nogroup": "-nogroup" in query,
                    "-user": "-user" in query,
                }

                # Remove flags from query
                for flag in flags:
                    query = query.replace(flag, "").strip()

                if not query:
                    IS_BROADCASTING = False
                    return await message.reply_text(
                        "**❌ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ**"
                    )

                broadcast_content = query
                broadcast_type = "text"
            
            # Start broadcasting
            await message.reply_text("**✦ sᴛᴀʀᴛᴇᴅ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...**")

            # ══════════════════════════════════
            # BROADCAST TO GROUPS
            # ══════════════════════════════════
            if not flags.get("-nogroup", False):
                sent = 0
                pin_count = 0
                failed = 0
                chats = await get_served_chats()

                for chat in chats:
                    chat_id = int(chat["chat_id"])
                    if chat_id == message.chat.id:
                        continue
                    
                    try:
                        if broadcast_type == "reply":
                            m = await client.forward_messages(
                                chat_id, 
                                message.chat.id, 
                                [broadcast_content.id]
                            )
                        else:
                            m = await client.send_message(
                                chat_id, 
                                text=broadcast_content
                            )
                        sent += 1

                        # Pin if flag is set
                        if flags.get("-pin", False) or flags.get("-pinloud", False):
                            try:
                                await m.pin(
                                    disable_notification=flags.get("-pin", False)
                                )
                                pin_count += 1
                            except Exception as e:
                                logger.warning(f"Failed to pin in {chat_id}: {e}")
                                continue

                    except FloodWait as e:
                        flood_time = int(e.value)
                        logger.warning(
                            f"FloodWait of {flood_time}s for chat {chat_id}"
                        )
                        if flood_time > 200:
                            logger.info(f"Skipping chat {chat_id} - FloodWait too long")
                            failed += 1
                            continue
                        await asyncio.sleep(flood_time)
                    
                    except Exception as e:
                        logger.error(f"Error broadcasting to {chat_id}: {e}")
                        failed += 1
                        continue

                await message.reply_text(
                    f"**✅ ɢʀᴏᴜᴘ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!**\n\n"
                    f"**sᴇɴᴛ :** {sent}\n"
                    f"**ᴘɪɴɴᴇᴅ :** {pin_count}\n"
                    f"**ғᴀɪʟᴇᴅ :** {failed}"
                )

            # ══════════════════════════════════
            # BROADCAST TO USERS
            # ══════════════════════════════════
            if flags.get("-user", False):
                susr = 0
                failed_users = 0
                users = await get_served_users()

                for user in users:
                    user_id = int(user["user_id"])
                    
                    try:
                        if broadcast_type == "reply":
                            await client.forward_messages(
                                user_id, 
                                message.chat.id, 
                                [broadcast_content.id]
                            )
                        else:
                            await client.send_message(
                                user_id, 
                                text=broadcast_content
                            )
                        susr += 1

                    except FloodWait as e:
                        flood_time = int(e.value)
                        logger.warning(
                            f"FloodWait of {flood_time}s for user {user_id}"
                        )
                        if flood_time > 200:
                            logger.info(f"Skipping user {user_id} - FloodWait too long")
                            failed_users += 1
                            continue
                        await asyncio.sleep(flood_time)
                    
                    except Exception as e:
                        logger.error(f"Error broadcasting to user {user_id}: {e}")
                        failed_users += 1
                        continue

                await message.reply_text(
                    f"**✅ ᴜsᴇʀ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!**\n\n"
                    f"**sᴇɴᴛ :** {susr}\n"
                    f"**ғᴀɪʟᴇᴅ :** {failed_users}"
                )

        finally:
            IS_BROADCASTING = False


# ═══════════════════════════════════════
# STATS COMMAND
# ═══════════════════════════════════════

@Client.on_message(
    filters.command(["stats", "gstats"], prefixes=["/", "!", "."]) 
    & filters.user(OWNER_ID)
)
async def stats_command(client: Client, message: Message):
    """Get bot statistics"""
    from Bad.Database.users import get_served_users_count, get_served_chats_count
    
    users = await get_served_users_count()
    chats = await get_served_chats_count()
    
    await message.reply_text(
        f"**📊 ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs**\n\n"
        f"**ᴜsᴇʀs :** {users}\n"
        f"**ɢʀᴏᴜᴘs :** {chats}\n"
        f"**ᴛᴏᴛᴀʟ :** {users + chats}"
              )
