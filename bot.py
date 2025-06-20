from pyrogram import Client, filters
import random

# ====== BOT CONFIGURATION ======
API_ID = 268507865  # Your API ID
API_HASH = "5d810b47881f0268507865d20f7dcbfe"  # Your API Hash
BOT_TOKEN = "7478488657:AAGxdKe0hGzYptQiQLwHoLPjTiNxlc2wtac"  # Your Bot Token

# ====== INITIALIZE CLIENT ======
app = Client("PosterBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ====== IMAGE SOURCES ======
poster_image = "https://i.imgur.com/3GvwNBf.jpg"  # Static image
local_image_path = "poster.jpg"  # Local image file path (optional)

random_images = [
    "https://i.imgur.com/3GvwNBf.jpg",
    "https://i.imgur.com/9Nz45Vt.jpg",
    "https://i.imgur.com/QrV6HYZ.jpg"
]

# ====== COMMAND HANDLERS ======

@app.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply_photo(
        photo=poster_image,
        caption="👋 Hello! I am your Poster Bot!\n\nCommands:\n/poster - Fixed image\n/randompic - Random image\n/localpic - Local image"
    )

@app.on_message(filters.command("poster"))
async def send_fixed_image(bot, message):
    await message.reply_photo(
        photo=poster_image,
        caption="🎬 Here's your movie poster!"
    )

@app.on_message(filters.command("randompic"))
async def send_random_image(bot, message):
    image_url = random.choice(random_images)
    await message.reply_photo(
        photo=image_url,
        caption="✨ Here's a random movie poster!"
    )

@app.on_message(filters.command("localpic"))
async def send_local_image(bot, message):
    try:
        await message.reply_photo(
            photo=local_image_path,
            caption="📸 This is a locally stored image."
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

# ====== START BOT ======
print("✅ Bot is running...")
app.run()
