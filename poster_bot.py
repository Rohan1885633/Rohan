from pyrogram import Client, filters
import random

# ========== BOT CONFIG ==========
API_ID = 268507865  # ✅ Your API ID
API_HASH = "5d810b47881f0268507865d20f7dcbfe"  # ✅ Your API Hash
BOT_TOKEN = "7478488657:AAGxdKe0hGzYptQiQLwHoLPjTiNxlc2wtac"  # ✅ Your Bot Token

app = Client("PosterBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ========== IMAGE LINKS ==========
random_images = [
    "https://i.imgur.com/3GvwNBf.jpg",
    "https://i.imgur.com/9Nz45Vt.jpg",
    "https://i.imgur.com/QrV6HYZ.jpg"
]

poster_image = "https://i.imgur.com/3GvwNBf.jpg"
local_image_path = "poster.jpg"  # Optional local image (must exist in same folder)

# ========== COMMAND HANDLERS ==========

@app.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_photo(
        photo=poster_image,
        caption="👋 Hello! I am your Poster Bot.\nUse /poster or /randompic to get images."
    )

@app.on_message(filters.command("poster"))
async def send_fixed_image(bot, message):
    await message.reply_photo(
        photo=poster_image,
        caption="🎬 This is a fixed movie poster."
    )

@app.on_message(filters.command("randompic"))
async def send_random_image(bot, message):
    await message.reply_photo(
        photo=random.choice(random_images),
        caption="✨ Here's a random movie poster!"
    )

# Optional local image sender
@app.on_message(filters.command("localpic"))
async def send_local_image(bot, message):
    try:
        await message.reply_photo(
            photo=local_image_path,
            caption="🖼️ This is a locally saved poster."
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

# ========== START BOT ==========
app.run()
