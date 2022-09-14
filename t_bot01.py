import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
print("Initializing the Bot.....")



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):#Text to be sent to user.
    await context.bot.send_message(chat_id=update.effective_chat.id, text="How Can I help You! ☺️")
    #The function name <help> is used here.



if __name__ == '__main__':
    application = ApplicationBuilder().token('5599948853:AAH3DCmj0DFYPS4dAedYLQxyVJHt-Sy8O8w').build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help',help) #'help' is the text send to user.
    # second parameter help is the function made in the beginning .

    application.add_handler(start_handler)
    application.add_handler(help_handler)   #help handler variable is used here

    
    
    application.run_polling()