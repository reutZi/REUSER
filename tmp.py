#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from urllib.error import URLError

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from search_crawler_results import extract_data_from_file

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf" אני הREUSER. אשמח לעזור לך למצוא את המוצר שאתה צריך וביחד לשמור על העולם. מה אתה מחפש? {user.mention_html()} היי ",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyword = update.message.text
    products = extract_data_from_file("data.csv", keyword)

    if products.empty:
        await update.message.reply_text("No matching results were found for your request")
    else:
        for _, product in products.iterrows():
            photo_url = product['image URL']
            caption_text = f"Name: {product['name']}\nURL link: {product['URL link']}\nDate: {product['date']}\nOwner address: {product['owner address']}"

            try:
                # Send the photo with the caption to the user
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption_text)
            except URLError as e:
                logger.error(f"Failed to send photo for '{product['name']}': {e}")
            except Exception as e:
                logger.error(f"An error occurred while sending photo: {e}")



def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token('5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()