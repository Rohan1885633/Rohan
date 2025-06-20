# 🤖 Telegram Auto Filter Bot

A powerful Telegram bot that automatically filters indexed files using keywords.  
Supports inline search, 4GB files, IMDB-style captions, and admin upload commands.

---

## 🚀 Features

✅ Auto File Filtering  
✅ Inline Search Support  
✅ Admin File Upload  
✅ IMDB-style Caption Template  
✅ Index Files up to 4GB  
✅ Welcome Message  
✅ /stats Command (File Count)  
✅ /restart Command (Safe Restart)  
✅ MongoDB-based Storage  
✅ PM File Send Mode  

---

## 🛠️ Installation

pip install -r requirements.txt

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/auto-filter-bot.git
cd auto-filter-bot

#### 2. Fill In Config

API_ID = "268507865"  # from https://my.telegram.org
API_HASH = "5d810b47881f0268507865d20f7dcbfe"
BOT_TOKEN = "7478488657:AAGxdKe0hGzYptQiQLwHoLPjTiNxlc2wtac"
MONGO_URI = "your_mongodb_uri_here"
ADMINS = [8182973519]  # Telegram user IDs of admins
