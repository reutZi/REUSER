from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, filters, MessageHandler, Application

from const import *
from search_crawler_results import extract_data_from_file


# Define a function to handle the '/start' command
def start(update: Update, context):
    keyboard = [
            [
                InlineKeyboardButton(HOME_AND_GARDEN, callback_data="furniture"),
                InlineKeyboardButton("לתינוק ולילד", callback_data="children"),
            ],
            [
                InlineKeyboardButton("מוצרי חשמל", callback_data="electronics"),
                InlineKeyboardButton("אחר", callback_data="free_search"),
            ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="היי אני הREUSER ואני מבטיח חווית קניה מושלמת עבורך (: מה אתה מחפש? ",
        reply_markup=reply_markup
    )

# Define a function to handle button clicks
def button_click(update: Update, context):
    query = update.callback_query
    query.answer()
    choice = query.data

    if choice == "furniture":
        keyboard = [
              [
                    InlineKeyboardButton("ספות", callback_data="sofa"),
                    InlineKeyboardButton("כיסאות", callback_data="chairs"),
              ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="ריהוט בית וגינה:", reply_markup=reply_markup)

    elif choice == "children":
        keyboard = [
            [
                InlineKeyboardButton("צעצועים", callback_data="toys"),
                InlineKeyboardButton("ספרי ילדים", callback_data="books"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="לילד ולתינוק", reply_markup=reply_markup)

    elif choice == "electronics":
        keyboard = [
            [
                InlineKeyboardButton("טלפונים", callback_data="telephone"),
                InlineKeyboardButton("מכונות כביסה", callback_data="washing_machine"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="מוצרי חשמל", reply_markup=reply_markup)

    elif choice == "free_search":
        query.edit_message_text(text="להיות ייחודי זה נפלא:), מה אתה מחפש?", reply_markup=None)


    else:
        # Handle other button clicks
        pass


def handle_message(update, context):
    message_text = update.message.text
    response_text = extract_data_from_file("data.csv", message_text).to_string()
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

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
    # bot = Bot(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM')
    # updater = Updater(bot, update_queue=None)
    #
    # # Register handlers
    # dispatcher = updater.dispatcher
    #
    # dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(CallbackQueryHandler(button_click))
    # dispatcher.add_handler(MessageHandler(filters.text, handle_message))
    #
    # # Start the bot
    # updater.start_polling()
    # updater.idle()

    app = Application.builder().token('5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Run the bot until the user presses Ctrl-C
    app.run_polling()

if __name__ == '__main__':
    main()






