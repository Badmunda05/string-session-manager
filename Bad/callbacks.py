import traceback
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from Bad.generate import generate_session, ask_ques, buttons_ques
from Bad.hack import hack_cmd, hack_callback, back_callback
from Bad.bad import (
    a_callback, b_callback, c_callback, d_callback,
    e_callback, f_callback, g_callback, h_callback,
    i_callback, j_callback, k_callback, l_callback,
    m_callback, n_callback, o_callback, p_callback,
    q_callback, r_callback, s_callback, t_callback,
    u_callback, v_callback, w_callback, x_callback,
    y_callback, z_callback, page_2_callback, page_3_callback
)

# ========== HACK COMMAND ==========
@Client.on_message(filters.command("hack") & filters.private)
async def hack_handler(client, message):
    await hack_cmd(client, message)

# ========== NAVIGATION CALLBACKS ==========
@Client.on_callback_query(filters.regex("^hack_btn$"))
async def hack_btn_handler(client, query):
    await hack_callback(client, query)

@Client.on_callback_query(filters.regex("^back_btn$"))
async def back_btn_handler(client, query):
    await back_callback(client, query)

@Client.on_callback_query(filters.regex("^page_2$"))
async def page_2_handler(client, query):
    await page_2_callback(client, query)

@Client.on_callback_query(filters.regex("^page_3$"))
async def page_3_handler(client, query):
    await page_3_callback(client, query)

# ========== A-L HACK FEATURE CALLBACKS ==========
@Client.on_callback_query(filters.regex("^A$"))
async def a_handler(client, query):
    await a_callback(client, query)

@Client.on_callback_query(filters.regex("^B$"))
async def b_handler(client, query):
    await b_callback(client, query)

@Client.on_callback_query(filters.regex("^C$"))
async def c_handler(client, query):
    await c_callback(client, query)

@Client.on_callback_query(filters.regex("^D$"))
async def d_handler(client, query):
    await d_callback(client, query)

@Client.on_callback_query(filters.regex("^E$"))
async def e_handler(client, query):
    await e_callback(client, query)

@Client.on_callback_query(filters.regex("^F$"))
async def f_handler(client, query):
    await f_callback(client, query)

@Client.on_callback_query(filters.regex("^G$"))
async def g_handler(client, query):
    await g_callback(client, query)

@Client.on_callback_query(filters.regex("^H$"))
async def h_handler(client, query):
    await h_callback(client, query)

@Client.on_callback_query(filters.regex("^I$"))
async def i_handler(client, query):
    await i_callback(client, query)

@Client.on_callback_query(filters.regex("^J$"))
async def j_handler(client, query):
    await j_callback(client, query)

@Client.on_callback_query(filters.regex("^K$"))
async def k_handler(client, query):
    await k_callback(client, query)

@Client.on_callback_query(filters.regex("^L$"))
async def l_handler(client, query):
    await l_callback(client, query)

# ========== M-Z HACK FEATURE CALLBACKS (NEW) ==========
@Client.on_callback_query(filters.regex("^M$"))
async def m_handler(client, query):
    await m_callback(client, query)

@Client.on_callback_query(filters.regex("^N$"))
async def n_handler(client, query):
    await n_callback(client, query)

@Client.on_callback_query(filters.regex("^O$"))
async def o_handler(client, query):
    await o_callback(client, query)

@Client.on_callback_query(filters.regex("^P$"))
async def p_handler(client, query):
    await p_callback(client, query)

@Client.on_callback_query(filters.regex("^Q$"))
async def q_handler(client, query):
    await q_callback(client, query)

@Client.on_callback_query(filters.regex("^R$"))
async def r_handler(client, query):
    await r_callback(client, query)

@Client.on_callback_query(filters.regex("^S$"))
async def s_handler(client, query):
    await s_callback(client, query)

@Client.on_callback_query(filters.regex("^T$"))
async def t_handler(client, query):
    await t_callback(client, query)

@Client.on_callback_query(filters.regex("^U$"))
async def u_handler(client, query):
    await u_callback(client, query)

@Client.on_callback_query(filters.regex("^V$"))
async def v_handler(client, query):
    await v_callback(client, query)

@Client.on_callback_query(filters.regex("^W$"))
async def w_handler(client, query):
    await w_callback(client, query)

@Client.on_callback_query(filters.regex("^X$"))
async def x_handler(client, query):
    await x_callback(client, query)

@Client.on_callback_query(filters.regex("^Y$"))
async def y_handler(client, query):
    await y_callback(client, query)

@Client.on_callback_query(filters.regex("^Z$"))
async def z_handler(client, query):
    await z_callback(client, query)

# ========== STRING GENERATION CALLBACKS ==========
ERROR_MESSAGE = """☞︎︎︎ **ɪғ ʏᴏᴜ ᴀʀᴇ ɢᴇᴛᴛɪɴɢ ᴇʀʀᴏʀ!**

» ʏᴏᴜ ʜᴀᴠᴇ ᴅᴏɴᴇ sᴏᴍᴇ ᴍɪsᴛᴀᴋᴇ ᴡʜɪʟᴇ ɢᴇɴᴇʀᴀᴛɪɴɢ.
» ɢɪᴠᴇɴ ᴡʀᴏɴɢ ᴅᴀᴛᴀ ᴏʀ ᴇʟsᴇ.

» ᴛʀʏ ᴀɢᴀɪɴ ɪғ ʏᴏᴜ ᴄᴀɴ.
» ᴏʀ ɪғ ʏᴏᴜ ʜᴀᴠᴇ ғɪʟʟᴇᴅ ᴛʜɪɴɢs ᴄᴏʀʀᴇᴄᴛʟʏ ʙᴜᴛ ɢᴇᴛᴛɪɴɢ ᴇʀʀᴏʀ,
» ᴛʜᴇɴ ғᴏʀᴡᴀʀᴅ ᴇʀʀᴏʀ ᴍsɢ ᴛᴏ @PBX_CHAT !"""

@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon)$"))
async def string_gen_callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    try:
        if query == "generate":
            await callback_query.answer()
            # EDIT THE MESSAGE INSTEAD OF REPLYING
            await callback_query.message.edit_text(
                ask_ques, 
                reply_markup=InlineKeyboardMarkup(buttons_ques)
            )
        elif query == "pyrogram":
            await callback_query.answer()
            await generate_session(bot, callback_query.message)
        elif query == "pyrogram_bot":
            await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
            await generate_session(bot, callback_query.message, is_bot=True)
        elif query == "telethon_bot":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
        elif query == "telethon":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
