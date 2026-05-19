from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)
from pyrogram.errors import (
    ChatAdminRequired,
    UserNotParticipant,
    ChatWriteForbidden,
)

from config import MUST_JOIN


@Client.on_message(filters.private & filters.incoming, group=-1)
async def force_join(bot: Client, msg: Message):
    # If force join is disabled
    if not MUST_JOIN or not msg.from_user:
        return

    try:
        # Check membership
        await bot.get_chat_member(MUST_JOIN, msg.from_user.id)

    except UserNotParticipant:
        # Build join link
        if MUST_JOIN.isalpha():
            link = f"https://t.me/{MUST_JOIN}"
        else:
            chat = await bot.get_chat(MUST_JOIN)
            link = chat.invite_link

        try:
            await msg.reply_photo(
                photo="https://files.catbox.moe/k6jrxc.jpg",
                caption=(
                    "✦ » ғɪʀsᴛʟʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ғᴀᴍɪʟʏ\n"
                    "✦ » ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ.\n\n"
                    f"✦ » [🔸 ᴏғғɪᴄᴇ 🔸]({link})\n\n"
                    "✦ » ᴀғᴛᴇʀ ᴊᴏɪɴ ❖ /start ❖ ᴍᴇ ᴀɢᴀɪɴ 🌹!"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="🔶 ᴊᴏɪɴ ᴏғғɪᴄᴇ 🔶",
                                url=link,
                            )
                        ]
                    ]
                ),
            )

            # Stop other handlers
            await msg.stop_propagation()

        except ChatWriteForbidden:
            pass

    except ChatAdminRequired:
        print(
            f"❌ I need admin rights in MUST_JOIN chat: {MUST_JOIN}"
        )
