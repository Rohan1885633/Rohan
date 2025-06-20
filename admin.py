from pyrogram import filters
from pyrogram.types import Message
from config import ADMINS
from database import save_file

def register(app):

    @app.on_message(filters.private & filters.document & filters.user(ADMINS))
    async def handle_upload(client, message: Message):
        if not message.caption:
            return await message.reply("Please add a caption with keywords.")

        keywords = message.caption.split("|")
        if len(keywords) < 2:
            return await message.reply("Use this format:\n`Movie Title | keyword1, keyword2`")

        caption = keywords[0].strip()
        keyword_list = keywords[1].split(",")

        save_file(message.document.file_id, caption, keyword_list)
        await message.reply("✅ File saved successfully!")
