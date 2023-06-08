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

from telegram import ForceReply, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

from consts import *
from search_crawler_results import extract_data_from_file

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    userText = update.message.text
    if isCity(userText):
        keyboard = [
            [
                InlineKeyboardButton("מוצרי חשמל", callback_data="category1"),
                InlineKeyboardButton("ריהוט לבית ולגינה", callback_data="category2"),
            ],
            [
                InlineKeyboardButton("מחשבים וציוד נלווה", callback_data="category3"),
                InlineKeyboardButton("לתינוק ולילד", callback_data="category4"),
            ],
            [
                InlineKeyboardButton("אחר", callback_data="other"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text("מקום נפלא לגור בו! 🏡🌸\nבחר את סוג המוצר שאתה מחפש:", reply_markup=reply_markup)
        return

    keyword = update.message.text
    products = extract_data_from_file("data.csv", keyword)
    products_length = len(products)

    if products.empty:
        await update.message.reply_text("לא נמצאו פריטים שתואמים לבקשה שלך, נסה שנית.")
    else:
        if len(products) > 1:
            await update.message.reply_text(f"נמצאו {products_length} תוצאות מתאימות. אלו התוצאות הרלוונטיות ביותר עבורך: ")
        else:
            await update.message.reply_text("התוצאה הרלוונטית ביותר עבורך:")

    for _, product in products.iterrows():
        photo_url = product['image URL']
        caption_text = f"{product['name']}\n{LINK_URL} {product['link URL']}\n{DATE} {product['date']}\n{OWNER_ADDRESS} {product['owner address']}\n{OWNER_PHONE} {product['owner phone']}"

        #Send the photo with the caption to the user
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption_text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"שלום {user.mention_html()}!",
        #reply_markup=ForceReply(selective=True),
    )

    message_text = "ברוך הבא לREUSER!♻️\n\nביחד נשמור על הסביבה❤️\n\nשלב ראשון הכנס את מקום מגוריך\nכדי שאוכל להביא לך את התוצאות\nהטובות ביותר עבורך!"
    await update.message.reply_text(message_text)

    reply = await context.bot.await_reply(update, timeout=None)


def isCity(city_name):
    with open('cities.txt', 'r', encoding='utf-8') as file:
        cities = file.read().splitlines()
        if city_name in cities:
            return True
        else:
            return False


# async def getOptions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     keyboard = [
#         [
#             InlineKeyboardButton("מוצרי חשמל", callback_data="category1"),
#             InlineKeyboardButton("ריהוט לבית ולגינה", callback_data="category2"),
#         ],
#         [
#             InlineKeyboardButton("מחשבים וציוד נלווה", callback_data="category3"),
#             InlineKeyboardButton("לתינוק ולילד", callback_data="category4"),
#         ],
#         [
#             InlineKeyboardButton("אחר", callback_data="other"),
#         ],
#     ]
#
#     reply_markup = InlineKeyboardMarkup(keyboard)
#
#     await update.message.reply_text("מקום נפלא לגור בו! 🏡🌸\nבחר את סוג המוצר שאתה מחפש:", reply_markup=reply_markup)


async def handle_button_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = query.from_user

    option_selected = query.data

    #keyboard = [[]]

    # Handle different options
    if option_selected == "category2":
        keyboard = [
            [
                InlineKeyboardButton("ספות", callback_data="option1"),
                InlineKeyboardButton("שולחנות", callback_data="option2"),
                InlineKeyboardButton("ארונות", callback_data="option3"),
                InlineKeyboardButton("כיסאות", callback_data="option4")
            ],
        ]
    elif option_selected == "category1":
        keyboard = [
            [
                InlineKeyboardButton("תנורים", callback_data="option3"),
                InlineKeyboardButton("מיקרוגל", callback_data="option5"),
                InlineKeyboardButton("בלנדרים", callback_data="option6"),
                InlineKeyboardButton("מקררים", callback_data="option7"),
            ],
        ]
    elif option_selected == "category3":
        keyboard = [
            [
                InlineKeyboardButton("מחשבים", callback_data="option8"),
                InlineKeyboardButton("מדפסות", callback_data="option9"),
                InlineKeyboardButton("מדפסות", callback_data="option10"),
                InlineKeyboardButton("סוללות", callback_data="option11"),
            ],
        ]
    elif option_selected == "category4":
        keyboard = [
            [
                InlineKeyboardButton("אפשרות 7", callback_data="option7"),
                InlineKeyboardButton("אפשרות 8", callback_data="option8"),
            ],
        ]
    elif option_selected == "category5":
        await query.message.reply_text("נפלא להיות ייחודי!\nאיזה מוצר אתה מחפש?")
        return

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_html(
        rf"בחר את המוצר אותו אתה מחפש:",
        reply_markup=reply_markup,
    )

    await handle_additional_buttons(update,context)



async def handle_additional_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = query.from_user

    option_selected = query.data

    # Handle different options
    if option_selected == "option1":
        # Handle Option 1
        await query.message.reply_text("You selected Option 1")
    elif option_selected == "option2":
        # Handle Option 2
        await query.message.reply_text("You selected Option 2")
    elif option_selected == "option3":
        # Handle Option 3
        await query.message.reply_text("You selected Option 3")
    elif option_selected == "option4":
        # Handle Option 4
        await query.message.reply_text("You selected Option 4")
    elif option_selected == "option5":
        # Handle Option 5
        await query.message.reply_text("You selected Option 5")
    elif option_selected == "option6":
        # Handle Option 6
        await query.message.reply_text("You selected Option 6")
    elif option_selected == "option7":
        # Handle Option 7
        await query.message.reply_text("You selected Option 7")
    elif option_selected == "option8":
        # Handle Option 8
        await query.message.reply_text("You selected Option 8")
    elif option_selected == "option9":
        # Handle Option 9
        await query.message.reply_text("You selected Option 9")
    elif option_selected == "option10":
        # Handle Option 10
        await query.message.reply_text("You selected Option 10")
    else:
        # Handle other options
        return




def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token('5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(handle_button_selection))
    #application.add_handler(CallbackQueryHandler(handle_additional_buttons))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
