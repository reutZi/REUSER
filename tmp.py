
import logging
from urllib.error import URLError

import requests
from telebot.apihelper import send_photo, send_message
from telegram import ForceReply, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

from consts import *
from search_crawler_results import extract_data_from_file

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE, text = None) -> None:
    query = update.callback_query
    if(text == None):
        userText = update.message.text
    else:
        userText = text
    if isCity(userText):
        await getOptions(update, context)
        return

    products = extract_data_from_file("data.csv", userText)
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
        product_url = product['link URL']
        caption_text = f"\n[{LINK_URL}]({product_url})\n{DATE} {product['date']}\n{OWNER_ADDRESS} {product['owner address']}\n{OWNER_PHONE} {product['owner phone']}".replace('.', '\.')
        photo_data = requests.get(photo_url).content
        send_photo(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM', chat_id= query.message.chat_id,
                   photo=photo_data, caption=caption_text, parse_mode='MarkdownV2')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"שלום {user.mention_html()}!",
        reply_markup=None,
    )

    message_text = f"\n{O1}{O2}\n\n{O3}\n\n{O4}\n\n{O5}\n{O6}"
    await update.message.reply_text(message_text)

    reply = await context.bot.await_reply(update, timeout=None)

def isCity(city_name):
    with open('cities.txt', 'r', encoding='utf-8') as file:
        cities = file.read().splitlines()
        if city_name in cities:
            return True
        else:
            return False


async def getOptions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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

    await update.message.reply_text(f"מקום נפלא לגור בו! 🏡🌸\n\nבחר את סוג המוצר שאתה מחפש:{O6}", reply_markup=reply_markup)


async def handle_button_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = query.from_user

    option_selected = query.data

    keyboard = [[]]

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
                InlineKeyboardButton("תנורים", callback_data="option11"),
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
                InlineKeyboardButton("פלאפונים", callback_data="option10"),
            ],
        ]
    elif option_selected == "category4":
        keyboard = [
            [
                InlineKeyboardButton("עריסות", callback_data="option12"),
                InlineKeyboardButton("עגלות וטיולונים", callback_data="option13"),
            ],
        ]
    elif option_selected == "category5":
        await query.message.reply_text(f"נפלא להיות ייחודי!\nאיזה מוצר אתה מחפש?{O6}")
        return
    elif option_selected == "option1":
        send_images("ספה", query)
        return
    elif option_selected == "option2":
        # Handle Option 2
        send_images("שולחן", query)
        return
    elif option_selected == "option3":
        # Handle Option 3
        send_images("ארון", query)
        return
    elif option_selected == "option4":
        # Handle Option 4
        send_images("כסא", query)
        return
    elif option_selected == "option5":
        # Handle Option 5
        send_images("מיקרוגל", query)
        return
    elif option_selected == "option6":
        # Handle Option 6
        send_images("בלנדר", query)
        return
    elif option_selected == "option7":
        # Handle Option 7
        send_images("מקרר", query)
        return
    elif option_selected == "option8":
        # Handle Option 8
        send_images("מחשב", query)
        return
    elif option_selected == "option9":
        # Handle Option 9
        send_images("מדפסת", query)
        return
    elif option_selected == "option10":
        # Handle Option 10
        send_images("פלאפון", query)
        return
    elif option_selected == "option11":
        # Handle Option 10
        send_images("תנור", query)
        return
    elif option_selected == "option12":
        # Handle Option 10
        send_images("עריסה", query)
        return
    elif option_selected == "option13":
        # Handle Option 10
        send_images("עגלה", query)
        return

    else:
        await query.message.reply_text(f"נפלא להיות ייחודי!\nאיזה מוצר אתה מחפש?{O6}")
        return

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_html(
        rf"בחר את המוצר אותו אתה מחפש:",
        reply_markup=reply_markup,
    )

def send_images(text, query):
    products = extract_data_from_file("data.csv", text)
    products_length = len(products)

    if products.empty:
        text_message =  "לא נמצאו פריטים שתואמים לבקשה שלך, נסה שנית."
    else:
       if len(products) > 1:
           text_message = f"נמצאו {products_length} תוצאות מתאימות. זאת התוצאה הרלוונטית ביותר עבורך: "
       else:
           text_message = "התוצאה הרלוונטית ביותר עבורך:"

    send_message(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM', chat_id=query.message.chat_id,
                        text=text_message)


    for _, product in products.iterrows():
        photo_url = product['image URL']
        product_url = product['link URL']
        caption_text = f"\n[{LINK_URL}]({product_url})\n{DATE} {product['date']}\n{OWNER_ADDRESS} {product['owner address']}\n{OWNER_PHONE} {product['owner phone']}".replace(
            '.', '\.')
        photo_data = requests.get(photo_url).content
        send_photo(token='5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM', chat_id=query.message.chat_id,
                   photo=photo_data, caption=caption_text, parse_mode='MarkdownV2')


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token('5980355826:AAFUvJ0oyasgvc6GxChdVjRXHWIqanesQvM').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_button_selection))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()