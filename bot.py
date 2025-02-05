import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import os
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def change(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id_ = update.message.audio.file_id
    file = await context.bot.get_file(file_id=id_)
    await file.download_to_drive('/dev/shm/hello')
    chat_id = update.message.chat_id
    f = open("/dev/shm/hello", "rb")
    print("->>>>>>>>>>>>>>1")
    await context.bot.send_audio(chat_id, f, title="adnannnn", caption="karriiim")
    print("->>>>>>>>>>>>>>2")
    



if __name__ == '__main__':
    application = ApplicationBuilder().token('7730403782:AAGukUBxnqxbtAfsLdcHqw7NQ16T8cCI584').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    change_handler = MessageHandler(filters.AUDIO, change)
    application.add_handler(change_handler)
    
    application.run_polling()


