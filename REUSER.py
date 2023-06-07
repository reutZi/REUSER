from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Define a function to handle the '/start' command
def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton("לקנות", callback_data="buy"),
            InlineKeyboardButton("למכור", callback_data="sell"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="הי! אני הREUSER, ואני כאן כדי לעזור לך למסור או לקבל חפצים יד שניה. אתה רוצה לקנות או למכור?",
        reply_markup=reply_markup
    )

# Define a function to handle button clicks
def button_click(update: Update, context):
    query = update.callback_query
    query.answer()
    choice = query.data

    keyboard = [
        [
            InlineKeyboardButton("ריהוט בית וגינה", callback_data="category_furniture"),
            InlineKeyboardButton("נדל\"ן", callback_data="category_real_estate"),
        ],
        [
            InlineKeyboardButton("רכבים", callback_data="category_cars"),
            InlineKeyboardButton("מוצרי חשמל", callback_data="category_electronics"),
        ],
        [
            InlineKeyboardButton("ספורט", callback_data="category_sports"),
        ]
    ]

    if choice == "buy":
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="מה אתה רוצה לקנות?", reply_markup=reply_markup)

    elif choice == "sell":
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="מה אתה רוצה למכור?", reply_markup=reply_markup)

    else:
        # Handle other button clicks
        pass


def category_selected(update: Update, context):
    query = update.callback_query
    query.answer()
    category = query.data

    # Handle the selected category
    if category == "category_furniture":
        keyboard = [
            [
                InlineKeyboardButton("ספה", callback_data="subcategory_sofa"),
                InlineKeyboardButton("ארון", callback_data="subcategory_cabinet"),
            ],
            [
                InlineKeyboardButton("כיסאות", callback_data="subcategory_chairs"),
                InlineKeyboardButton("מטבח", callback_data="subcategory_kitchen"),
            ],
            [
                InlineKeyboardButton("שטיח", callback_data="subcategory_rug"),
                InlineKeyboardButton("מזרנים", callback_data="subcategory_mattress"),
            ],
            [
                InlineKeyboardButton("ריהוט גינה", callback_data="subcategory_garden"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="בחר תת-קטגוריה:", reply_markup=reply_markup)
    else:
        response_text = "קטגוריה לא תקינה."
        query.edit_message_text(text=response_text)

def subcategory_selected(update: Update, context):
    query = update.callback_query
    query.answer()
    subcategory = query.data

    # Handle the selected subcategory
    if subcategory == "subcategory_sofa":
        response_text = "בחרת בתת-קטגורית ספה."
    elif subcategory == "subcategory_cabinet":
        response_text = "בחרת בתת-קטגורית ארון."
    elif subcategory == "subcategory_chairs":
        response_text = "בחרת בתת-קטגורית כיסאות."
    elif subcategory == "subcategory_kitchen":
        response_text = "בחרת בתת-קטגורית מטבח."
    elif subcategory == "subcategory_rug":
        response_text = "בחרת בתת-קטגורית שטיח."
    elif subcategory == "subcategory_mattress":
        response_text = "בחרת בתת-קטגורית מזרנים."
    elif subcategory == "subcategory_garden":
        response_text = "בחרת בתת-קטגורית ריהוט גינה."
    else:
        response_text = "תת-קטגוריה לא תקינה."

    query.edit_message_text(text=response_text)


def main():
    # Initialize the bot
    bot = Bot(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM')
    updater = Updater(bot=bot)

    # Register handlers
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    button_click_handler = CallbackQueryHandler(button_click)
    category_selected_handler = CallbackQueryHandler(category_selected, pattern='^category_')
    subcategory_selected_handler = CallbackQueryHandler(subcategory_selected, pattern='^category_')
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(button_click_handler)
    dispatcher.add_handler(category_selected_handler)
    dispatcher.add_handler(subcategory_selected_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


#
# #!/usr/bin/env python
# # pylint: disable=unused-argument, wrong-import-position
# # This program is dedicated to the public domain under the CC0 license.
#
# """
# Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
#  https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
# """
# import logging
#
# from telegram import __version__ as TG_VER
#
# try:
#     from telegram import __version_info__
# except ImportError:
#     __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
#
# if __version_info__ < (20, 0, 0, "alpha", 1):
#     raise RuntimeError(
#         f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#         f"{TG_VER} version of this example, "
#         f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
#     )
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
#
# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Sends a message with three inline buttons attached."""
#     keyboard = [
#         [
#             InlineKeyboardButton("Option 1", callback_data="1"),
#             InlineKeyboardButton("Option 2", callback_data="2"),
#         ],
#         [InlineKeyboardButton("Option 3", callback_data="3")],
#     ]
#
#     reply_markup = InlineKeyboardMarkup(keyboard)
#
#     await update.message.reply_text("Please choose:", reply_markup=reply_markup)
#
#
# async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Parses the CallbackQuery and updates the message text."""
#     query = update.callback_query
#
#     # CallbackQueries need to be answered, even if no notification to the user is needed
#     # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
#     await query.answer()
#
#     await query.edit_message_text(text=f"Selected option: {query.data}")
#
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Displays info on how to use the bot."""
#     await update.message.reply_text("Use /start to test this bot.")
#
#
# def main() -> None:
#     """Run the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token("5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM").build()
#
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CallbackQueryHandler(button))
#     application.add_handler(CommandHandler("help", help_command))
#
#     # Run the bot until the user presses Ctrl-C
#     application.run_polling(allowed_updates=Update.ALL_TYPES)
#
#
# if __name__ == "__main__":
#     main()
#
