from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


# Define a function to handle the '/start' command
def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton("לקנות", url="https://t.me/my_REUSER_bot?start=buy"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="הי! אני הREUSER, ואני כאן כדי לעזור לך למסור או לקבל חפצים יד שניה. אתה רוצה לקנות או למכור?",
        reply_markup=reply_markup
    )

# Define a function to handle incoming messages
def echo(update: Update, context):
    message_text = update.message.text

    if message_text.startswith('לקנות'):
        response_text = "?מה תרצה לקנות"
        context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)
    if message_text.startswith('למכור'):
        response_text = "?מה תרצה למכור"
        context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

def main():
    # Initialize the bot
    bot = Bot(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM')
    updater = Updater(bot=bot)

    # Register handlers
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()