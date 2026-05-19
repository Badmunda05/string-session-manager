from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 
from config import OWNER_ID

# Page 1: A-L Features
HACK_TEXT = """
**𝗔 :~** [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]

**𝗕 :~** [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsʀɴᴀᴍᴇ... ᴇᴛᴄ]

**𝗖 :~** [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ sᴛʀɪɴɢsᴇssɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]

**𝗗 :~** [ᴋɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ **ᴏᴘᴛɪᴏɴ ʙ** ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ ᴀᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]

**𝗘 :~** [ᴊᴏɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

**𝗙 :~** [ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠɪᴀ sᴛʀɪɴɢsᴇssɪᴏɴ]

**𝗚 :~** [ᴅᴇʟᴇᴛᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

**𝗛 :~** [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]

**𝗜 :~** [ᴛᴇʀᴍɪɴᴀᴛᴇ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ ᴜᴏᴜʀ sᴛʀɪɴɢsᴇssɪᴏɴ]

**𝗝 :~** [ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ]

**𝗞 :~** [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]

**𝗟 :~** [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]
"""

# Page 2: M-X Features
HACK_TEXT_2 = """
**𝗠 :~** [ᴇxᴘᴏʀᴛ ᴀʟʟ ᴄʜᴀᴛs ᴅᴀᴛᴀ {ɢᴇᴛ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʀᴏᴜᴘs ᴡɪᴛʜ ᴍᴇᴍʙᴇʀ ᴄᴏᴜɴᴛ}]

**𝗡 :~** [ᴄʜᴀɴɢᴇ ᴘʀᴏғɪʟᴇ {ᴜᴘᴅᴀᴛᴇ ɴᴀᴍᴇ, ʙɪᴏ, ᴜsᴇʀɴᴀᴍᴇ}]

**𝗢 :~** [ɢᴇᴛ ᴀʟʟ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs {sʜᴏᴡ ᴀʟʟ ʟᴏɢɢᴇᴅ ɪɴ ᴅᴇᴠɪᴄᴇs}]

**𝗣 :~** [ғᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇs {ʙᴜʟᴋ ғᴏʀᴡᴀʀᴅ ᴛᴏ ᴍᴜʟᴛɪᴘʟᴇ ᴄʜᴀᴛs}]

**𝗤 :~** [ᴀᴅᴅ ᴍᴇᴍʙᴇʀs {ʙᴜʟᴋ ᴀᴅᴅ ᴜsᴇʀs ᴛᴏ ɢʀᴏᴜᴘ}]

**𝗥 :~** [ᴄʜᴀɴɢᴇ ᴜsᴇʀɴᴀᴍᴇ {ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ}]

**𝗦 :~** [ᴅᴏᴡɴʟᴏᴀᴅ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏs {ɢᴇᴛ ᴀʟʟ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇs}]

**𝗧 :~** [ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ {sᴇɴᴅ ᴛᴏ ᴀʟʟ ᴄᴏɴᴛᴀᴄᴛs}]

**𝗨 :~** [ɢᴇᴛ ᴍᴇᴍʙᴇʀs ʟɪsᴛ {ᴇxᴘᴏʀᴛ ᴀʟʟ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs}]

**𝗩 :~** [ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ {ᴄᴏᴘʏ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ's ᴘʀᴏғɪʟᴇ}]

**𝗪 :~** [ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴄʜᴀᴛs {ᴄʟᴇᴀʀ ᴀʟʟ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴs}]

**𝗫 :~** [ʙʟᴏᴄᴋ ᴀʟʟ ᴄᴏɴᴛᴀᴄᴛs {ʙʟᴏᴄᴋ ᴇᴠᴇʀʏᴏɴᴇ}]
"""

# Page 3: Y-Z Features
HACK_TEXT_3 = """
**𝗬 :~** [ᴄʜᴀɴɢᴇ ᴘʀɪᴠᴀᴄʏ sᴇᴛᴛɪɴɢs {ʟᴀsᴛ sᴇᴇɴ, ᴘʜᴏɴᴇ, ᴘʀᴏғɪʟᴇ}]

**𝗭 :~** [ᴍᴀɴᴀɢᴇ 𝟸ғᴀ {ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴛᴡᴏ-ғᴀᴄᴛᴏʀ ᴀᴜᴛʜ}]

**ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴄᴏᴍɪɴɢ sᴏᴏɴ...**
"""

info = """
❥︎ ɴᴀᴍᴇ : {}
❥︎ ɪᴅ : {}
❥︎ ᴘʜᴏɴᴇ ɴᴏ : +{}
❥︎ ᴜsᴇʀɴᴀᴍᴇ : @{}
"""

# Page 1 Buttons (A-L)
HACK_MODS = IKM(
    [
        [
            IKB("𝗔", callback_data="A"),
            IKB("𝗕", callback_data="B"),
            IKB("𝗖", callback_data="C"),
            IKB("𝗗", callback_data="D"),
        ],
        [
            IKB("𝗘", callback_data="E"),
            IKB("𝗙", callback_data="F"),
            IKB("𝗚", callback_data="G"),
            IKB("𝗛", callback_data="H"),
        ],
        [
            IKB("𝗜", callback_data="I"),
            IKB("𝗝", callback_data="J"),
            IKB("𝗞", callback_data="K"),
            IKB("𝗟", callback_data="L"),
        ],
        [
            IKB("➡️ ɴᴇxᴛ ᴘᴀɢᴇ", callback_data="page_2"),
        ],
    ]
)

# Page 2 Buttons (M-X)
HACK_MODS_2 = IKM(
    [
        [
            IKB("𝗠", callback_data="M"),
            IKB("𝗡", callback_data="N"),
            IKB("𝗢", callback_data="O"),
            IKB("𝗣", callback_data="P"),
        ],
        [
            IKB("𝗤", callback_data="Q"),
            IKB("𝗥", callback_data="R"),
            IKB("𝗦", callback_data="S"),
            IKB("𝗧", callback_data="T"),
        ],
        [
            IKB("𝗨", callback_data="U"),
            IKB("𝗩", callback_data="V"),
            IKB("𝗪", callback_data="W"),
            IKB("𝗫", callback_data="X"),
        ],
        [
            IKB("⬅️ ᴘʀᴇᴠ", callback_data="hack_btn"),
            IKB("➡️ ɴᴇxᴛ", callback_data="page_3"),
        ],
    ]
)

# Page 3 Buttons (Y-Z)
HACK_MODS_3 = IKM(
    [
        [
            IKB("𝗬", callback_data="Y"),
            IKB("𝗭", callback_data="Z"),
        ],
        [
            IKB("⬅️ ᴘʀᴇᴠɪᴏᴜs ᴘᴀɢᴇ", callback_data="page_2"),
        ],
    ]
)

# Main menu with back button
BAD_MODS = IKM(
    [
        [
            IKB("𝗔", callback_data="A"),
            IKB("𝗕", callback_data="B"),
            IKB("𝗖", callback_data="C"),
            IKB("𝗗", callback_data="D"),
        ],
        [
            IKB("𝗘", callback_data="E"),
            IKB("𝗙", callback_data="F"),
            IKB("𝗚", callback_data="G"),
            IKB("𝗛", callback_data="H"),
        ],
        [
            IKB("𝗜", callback_data="I"),
            IKB("𝗝", callback_data="J"),
            IKB("𝗞", callback_data="K"),
            IKB("𝗟", callback_data="L"),
        ],
        [
            IKB("➡️ ᴍᴏʀᴇ", callback_data="page_2"),
        ],
        [
            IKB("⬅️ ʙᴀᴄᴋ", callback_data="back_btn"),
        ],
    ]
)
