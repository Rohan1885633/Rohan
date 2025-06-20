import os
import sys
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from config import ADMINS
from database import save_file, db

def register(app):

    # Upload Handler – Admin sends file with caption
    @app.on_message(filters.private & filters.document & filters.user(ADMINS))
    async def handle_upload(client, message: Message):
        if not message.caption:
            return await message.reply("❌ Add a caption with keywords using:\n\n**Title | keyword1, keyword2**")

        try:
            title, tags = message.caption.split("|")
            save_file(message.document.file_id, title.strip(), tags.split(","))
            await message.reply("✅ File saved successfully!")
        except Exception as e:
            await message.reply(f"⚠️ Caption format error.\nUse: `Title | keyword1, keyword2`\n\nError: `{e}`")

    # Bot Stats
    @app.on_message(filters.command("stats") & filters.user(ADMINS))
    async def stats_command(client, message: Message):
        try:
            total_files = db.files.count_documents({})
            # Uncomment below if you add user tracking
            # total_users = db.users.count_documents({})
            await message.reply_text(
                f"📊 **Bot Statistics:**\n\n"
                f"📁 Total Files Indexed: `{total_files}`\n"
                f"👤 Total Users: `Not Tracked`\n"
                f"📦 MongoDB DB: `{db.name}`"
            )
        except Exception as e:
            await message.reply_text(f"❌ Error getting stats:\n`{e}`")

    # Restart Command
    @app.on_message(filters.command("restart") & filters.user(ADMINS))
    async def restart_command(client, message: Message):
        await message.reply_text("♻️ Restarting bot...")
        await asyncio.sleep(2)
        os.execv(sys.executable, [sys.executable] + sys.argv)
