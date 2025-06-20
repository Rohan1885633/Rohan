from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS
from database import db

def register(app):

    # Existing admin upload handler here...

    @app.on_message(filters.command("stats") & filters.user(ADMINS))
    async def stats_command(client, message: Message):
        try:
            total_files = db.files.count_documents({})
            # If you track users:
            # total_users = db.users.count_documents({})
            await message.reply_text(
                f"📊 **Bot Statistics:**\n\n"
                f"📁 Total Files Indexed: `{total_files}`\n"
                f"👤 Total Users: `Not Tracked`\n"
                f"📦 MongoDB: `{db.name}`",
                quote=True
            )
        except Exception as e:
            await message.reply_text(f"❌ Error: {e}")
