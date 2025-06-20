from pyrogram import filters
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, Message
from database import search_files

def register(app):

    @app.on_message(filters.private & filters.command("start"))
    async def start_handler(client, message: Message):
        await message.reply_text(
            "👋 Welcome to the Auto Filter Bot!\n\n"
            "✨ Features:\n"
            "✅ 𝐼𝑀𝐷𝐵 𝑇𝑒𝑚𝑝𝑙𝑎𝑡𝑒 𝑆𝑒𝑡\n"
            "✅ 𝐼𝑛𝑑𝑒𝑥𝑒𝑠 𝐹𝑖𝑙𝑒𝑠 𝑎𝑏𝑜𝑣𝑒 4𝐺𝐵\n"
            "✅ 𝑃𝑟𝑒𝐷𝑉𝐷 𝑎𝑛𝑑 𝐶𝑎𝑚𝑅𝑖𝑝 𝐷𝑒𝑙𝑒𝑡𝑒 𝑀𝑜𝑑𝑒\n"
            "✅ 𝐹𝑜𝑟𝑐𝑒 𝑆𝑢𝑏𝑠𝑐𝑟𝑖𝑝𝑡𝑖𝑜𝑛, 𝑆𝑒𝑡𝑡𝑖𝑛𝑔𝑠, 𝑆𝑡𝑎𝑡𝑠\n"
            "✅ 𝐴𝑢𝑡𝑜 𝐹𝑖𝑙𝑡𝑒𝑟, 𝐵𝑟𝑜𝑎𝑑𝑐𝑎𝑠𝑡, 𝐵𝑎𝑛, 𝐼𝑛𝑙𝑖𝑛𝑒 𝑆𝑒𝑎𝑟𝑐ℎ, 𝐹𝑖𝑙𝑒 𝑆𝑡𝑜𝑟𝑒\n\n"
            "📥 Send a keyword like `ironman` to get matching files.\n"
            "🔎 Try inline: `@YourBotUsername ironman`",
            disable_web_page_preview=True
        )

    @app.on_message(filters.private & filters.text)
    async def text_search(client, message: Message):
        results = search_files(message.text)
        if not results:
            return await message.reply("❌ No matches found.")

        for result in results:
            await message.reply_document(result["file_id"], caption=result["caption"])

    @app.on_inline_query()
    async def inline_search(client, inline_query: InlineQuery):
        query = inline_query.query
        results = search_files(query)
        answers = []

        for r in results:
            answers.append(
                InlineQueryResultArticle(
                    title=r["caption"],
                    input_message_content=InputTextMessageContent(r["caption"]),
                    description=", ".join(r["keywords"])
                )
            )

        await inline_query.answer(answers[:50])
