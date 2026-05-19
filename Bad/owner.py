from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from Bad.Database.users import add_served_user, get_served_users

sudo_user_id = 7616808278

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(bot: Client, msg: Message):
    """Add user to database and notify sudo user"""
    user = msg.from_user
    await add_served_user(user.id)

    try:
        await bot.send_message(
            chat_id=sudo_user_id,
            text=(
                "✅ **USER DETECTED**\n\n"
                f"👤 **Name:** {user.mention}\n"
                f"🆔 **User ID:** `{user.id}`"
            )
        )
    except Exception as e:
        print(f"Failed to send notification to sudo user: {e}")

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(
        f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs",
        quote=True
    )
