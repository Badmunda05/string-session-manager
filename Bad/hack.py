from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram.errors import (
    UserIsBlocked,
    InputUserDeactivated,
)

from config import OWNER_ID
from Bad.Helper.data import (
    HACK_TEXT,
    HACK_MODS,
    BAD_MODS,
)
from Bad.Database.users import (
    add_served_user,
    remove_served_user,
)


# ──────────────────────────────────────
# /hack Command (Private)
# ──────────────────────────────────────
async def hack_cmd(client: Client, message: Message):
    try:
        if message.from_user:
            await add_served_user(message.from_user.id)

        await message.reply_text(
            text=HACK_TEXT,
            reply_markup=HACK_MODS,
        )

    except (UserIsBlocked, InputUserDeactivated):
        if message.from_user:
            await remove_served_user(message.from_user.id)

    except Exception:
        pass


# ──────────────────────────────────────
# Hack Button Callback
# ──────────────────────────────────────
@Client.on_callback_query(filters.regex("^hack_btn$"))
async def hack_callback(client: Client, query: CallbackQuery):
    try:
        await query.message.edit_text(
            text=HACK_TEXT,
            reply_markup=BAD_MODS,
        )
        await query.answer()

    except Exception:
        pass


# ──────────────────────────────────────
# Back Button Callback
# ──────────────────────────────────────
@Client.on_callback_query(filters.regex("^back_btn$"))
async def back_callback(client: Client, query: CallbackQuery):
    try:
        user = query.from_user
        me = await client.get_me()

        pm_text = f"""
✦ » ʜᴇʏ {user.mention} ✤,
✦ » ɪ ᴀᴍ {me.mention},

✦ » Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ,
✦ » ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

✦ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴩʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ
✦ » ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

✦ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴩ,
✦ » ᴅᴍ ᴍʏ ᴏᴡɴᴇʀ:
[⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α ⎯꯭̽🌸꯭](tg://user?id={OWNER_ID})
"""

        pm_buttons = InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton(
                    text="⌜ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ⌟",
                    callback_data="generate",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⌜ ʜᴀᴄᴋ ғᴇᴀᴛᴜʀᴇs ⌟",
                    callback_data="hack_btn",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⌜ sᴜᴘᴘᴏʀᴛ ⌟",
                    url="https://t.me/PBX_CHAT",
                ),
                InlineKeyboardButton(
                    text="⌜ ᴜᴘᴅᴀᴛᴇs ⌟",
                    url="https://t.me/PBX_UPDATE",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⌜ sᴏᴜʀᴄᴇ ⌟",
                    url="https://github.com/Badmunda05/string-session-manager/fork",
                )
            ],
        ]
    )

        await query.message.edit_text(
            text=pm_text,
            reply_markup=pm_buttons,
        )
        await query.answer()

    except Exception:
        pass
