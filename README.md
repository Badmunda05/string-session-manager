![Bad String Session Manager](https://files.catbox.moe/ookphv.jpg)

# 🧿 BAD STRING SESSION MANAGER 🧿

**A powerful Telegram bot to generate Pyrogram & Telethon string sessions with extra utilities.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Support](https://img.shields.io/badge/Support-Telegram-blue)

---

## ✨ Features

- 🔐 Generate **Pyrogram String Session**
- 🔑 Generate **Telethon String Session**
- 🧠 Clean & modular plugin system
- 🚫 Force subscribe (MUST_JOIN)
- 🧾 MongoDB based user tracking
- 😈 Extra hack / utility menu
- 🛡 Owner-only protected features
- ⚡ Fast, lightweight & stable

---

## 📂 Project Structure

```text
BadStringBot/
│
├── main.py
├── config.py
├── .env
├── requirements.txt
├── runtime.txt
├── Procfile
│
├── Bad/
│   ├── Database/
│   ├── Helpers/
│   ├── Plugins/
│   └── Utils/
```

---

## ⚙️ Environment Variables

Create a `.env` file and fill:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=your_telegram_id
MONGO_DB_URI=your_mongodb_uri
MUST_JOIN=channel_username   # optional
```

---

## 🚀 Deployment

### ▶ Local Run

```bash
pip install -r requirements.txt
python main.py
```

### ▶ Heroku / Render / VPS

- Python version: **3.10.9**
- Start command:

```bash
python main.py
```

<h3 align="center">
 ──「 🚀 ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 🚀 」──
</h3>

<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https://github.com/PbxBad/string-session-manager">
    <img
      src="https://img.shields.io/badge/Deploy%20On%20Heroku-7952B3?style=for-the-badge&logo=heroku&logoColor=white"
      width="240"
      height="45"
      alt="Deploy on Heroku"
    />
  </a>
</p>

---

## 🛡 Security Notes

- ❌ Never commit `.env`
- 🔄 Regenerate tokens if leaked
- 🔐 Hack utilities should be **owner-only**
- 📦 Mongo access only via Database module

---

## 🧑‍💻 Owner

**Bad Munda**  
[Telegram](https://t.me/BadMundaXD)

---

## ❤️ Support & Updates

- [💬 Support](https://t.me/PBX_CHAT)
- [📢 Updates](https://t.me/PBX_UPDATE) 

---

## 📜 License

Open-source project.  
Use, modify & share responsibly.

---

🔥 **Built with Python & Pyrogram** 🔥
