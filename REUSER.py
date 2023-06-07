from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, filters


# Define a function to handle the '/start' command
def start(update: Update, context):
    keyboard = [
        [
            InlineKeyboardButton("ריהוט בית וגינה", callback_data="furniture"),
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
        query.edit_message_text(text="בחר את סוג הספה הרצויה:", reply_markup=reply_markup)

        # הוסף את הפונקציה handle_furniture_choice כפונקציה טפלנית לבחירת הרהוט
        context.dispatcher.add_handler(CallbackQueryHandler(handle_furniture_choice))


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
        query.edit_message_text(text="הכנס את שם המוצר שאתה מחפש:")


    else:
        # Handle other button clicks
        pass


def handle_furniture_choice(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    choice = query.data

    if choice == "3sofa":
        text = "בחרת ב-3 מושבים"
        context.bot.send_message(chat_id=query.message.chat_id, text=text)

    elif choice == "2chairs":
        text = "בחרת ב-2 מושבים"
        context.bot.send_message(chat_id=query.message.chat_id, text=text)

    elif choice == "armchairs":
        text = "בחרת בכורסאות"
        context.bot.send_message(chat_id=query.message.chat_id, text=text)

    # הוסיפי תנאים ופעולות נוספות עבור הבחירות הנוספות ב







def main():
    # Initialize the bot
    bot = Bot(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM')
    updater = Updater(bot=bot)

    # Register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button_click))
    # query.edit_message_text(text="הכנס את שם המוצר שאתה מחפש:")

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
