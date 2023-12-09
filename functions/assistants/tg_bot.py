from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from functions.tools import audio as audio


def telegram_bot():

    TOKEN = "BOT_TOKEN"
    BOT_USERNAME = "BOT_NAME"

    # Commands
    async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hallo!\n"
                                        "Ich bin ein, sich in der Entwicklung befindender, Bot,\n"
                                        "der irgendwann mal auf alle möglichen Befehle antworten kann")

    async def receive_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        voice_file = await context.bot.get_file(update.message.voice.file_id)
        await audio.convert_ogg_to_mp3(voice_file.download('voice_note.ogg'))
        await update.message.reply_text('Sprachmemo empfangen und gespeichert!')

    # Response
    def handle_response(text: str) -> str:
        processed: str = text.lower()

        if "hello" in processed:
            return "moin"

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type
        text: str = update.message.text

        print(f"{update.message.chat.id} in {message_type}: '{text}'")

        if message_type == "group":
            if BOT_USERNAME in text:
                new_text: str = text.replace(BOT_USERNAME, "").strip()
                response: str = handle_response(new_text)
            else:
                return
        else:
            response: str = handle_response(text)

        print("Bot:", response)
        await update.message.reply_text(response)

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(receive_voice)

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=5)


telegram_bot()
