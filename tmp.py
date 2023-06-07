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
from telegram import ForceReply, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     await update.message.reply_html(
#         rf"Hi {user.mention_html()}!",
#         reply_markup=ForceReply(selective=True),
#     )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user = update.effective_user
    await update.message.reply_html(
               rf"שלום {user.mention_html()}!",
               reply_markup=ForceReply(selective=True),)



    keyboard = [
        [
            InlineKeyboardButton("ספות", callback_data="category1"),
            InlineKeyboardButton("שולחנות", callback_data="category2"),
        ],
        [
            InlineKeyboardButton("ארונות", callback_data="category3"),
            InlineKeyboardButton("כסאות", callback_data="category4"),
        ],
        [
            InlineKeyboardButton("אחר", callback_data="category5"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    emoji_recycle = "♻️"
    emoji_heart = "❤️"
    message_text = "ברוך הבא לREUSER! " + emoji_recycle + "\n\nאשמח לעזור לך למצוא את המוצר הכי טוב עבורך!\n" + " " + emoji_heart + "ביחד נשמור על הסביבה\n\nתבחר את הקטגוריה המתאימה עבורך:"

    await update.message.reply_html(message_text,reply_markup=reply_markup,)


    # await update.message.reply_html(
    #     "שלום משתמש, תבחר קטגוריה:",
    #     reply_markup=reply_markup,
    # )


async def handle_button_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = query.from_user

    option_selected = query.data

    # Handle different options
    if option_selected == "category1":
        keyboard = [
            [
                InlineKeyboardButton("אפשרות 1", callback_data="option1"),
                InlineKeyboardButton("אפשרות 2", callback_data="option2"),
            ],
        ]
    elif option_selected == "category2":
        keyboard = [
            [
                InlineKeyboardButton("אפשרות 3", callback_data="option3"),
                InlineKeyboardButton("אפשרות 4", callback_data="option4"),
            ],
        ]
    elif option_selected == "category3":
        keyboard = [
            [
                InlineKeyboardButton("אפשרות 5", callback_data="option5"),
                InlineKeyboardButton("אפשרות 6", callback_data="option6"),
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
        # נחכה לתשובה של המשתמש
        context.bot.register_next_step_handler(query.message, handle_user_response)

    else:
        # Handle other options
        return

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_html(
        rf"Option '{option_selected}' selected by {user.mention_html()}",
        reply_markup=reply_markup,
    )


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

async def handle_user_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    await update.message.reply_text(f"תודה על תשובתך: {user_response}")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token('5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(handle_button_selection))
    application.add_handler(CallbackQueryHandler(handle_additional_buttons))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_response))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()