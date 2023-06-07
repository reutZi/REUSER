# # from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
# # from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
# # import ExcelTable
# #
# #
# # # Define a function to handle the '/start' command
# # def start(update: Update, context):
# #     keyboard = [
# #         [
# #             InlineKeyboardButton("לקנות", url="https://t.me/my_REUSER_bot?start=buy"),
# #         ]
# #     ]
# #     reply_markup = InlineKeyboardMarkup(keyboard)
# #     context.bot.send_message(
# #         chat_id=update.effective_chat.id,
# #         text="הי! אני הREUSER, ואני כאן כדי לעזור לך למסור או לקבל חפצים יד שניה. אתה רוצה לקנות או למכור?",
# #         reply_markup=reply_markup
# #     )
# #
# # # Define a function to handle incoming messages
# # def echo(update: Update, context):
# #     message_text = update.message.text
# #
# #     if message_text.startswith('לקנות'):
# #         response_text = "?מה תרצה לקנות"
# #         context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)
# #     if message_text.startswith('למכור'):
# #         response_text = "?מה תרצה למכור"
# #         context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)
# #
# #
# # def main():
# #     # Initialize the bot
# #     bot = Bot(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM')
# #     updater = Updater(bot=bot)
# #
# #     # Register handlers
# #     dispatcher = updater.dispatcher
# #     start_handler = CommandHandler('start', start)
# #     echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# #     dispatcher.add_handler(start_handler)
# #     dispatcher.add_handler(echo_handler)
# #
# #
# #     # Start the bot
# #     updater.start_polling()
# #     updater.idle()
# #
# # if __name__ == '__main__':
# #     main()
# #
#
# from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
#
# # Define a function to handle the '/start' command
# def start(update: Update, context):
#     keyboard = [
#         [
#             InlineKeyboardButton("לקנות", url="https://t.me/my_REUSER_bot?start=buy"),
#             InlineKeyboardButton("למכור", url="https://t.me/my_REUSER_bot?start=sell"),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="הי! אני הREUSER, ואני כאן כדי לעזור לך למסור או לקבל חפצים יד שניה. אתה רוצה לקנות או למכור?",
#         reply_markup=reply_markup
#     )
#
# # Define a function to handle incoming messages
# def echo(update: Update, context):
#     message_text = update.message.text
#
#     if message_text.startswith('לקנות'):
#         response_text = "?מה תרצה לקנות"
#         context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)
#     if message_text.startswith('למכור'):
#         response_text = "?מה תרצה למכור"
#         context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)
#
#
# def main():
#     # Initialize the bot
#     bot = Bot(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM')
#     updater = Updater(bot=bot)
#
#     # Register handlers
#     dispatcher = updater.dispatcher
#     start_handler = CommandHandler('start', start)
#     echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#     dispatcher.add_handler(start_handler)
#     dispatcher.add_handler(echo_handler)
#
#     # Start the bot
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()
#

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

# Define a function to handle category selection
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
    subcategory_selected_handler = CallbackQueryHandler(subcategory_selected, pattern='^subcategory_')
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(button_click_handler)
    dispatcher.add_handler(category_selected_handler)
    dispatcher.add_handler(subcategory_selected_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
