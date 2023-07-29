from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lang_context import context

async def choose_lang_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("UZ", callback_data="lang=uz"),
        InlineKeyboardButton("RU", callback_data="lang=ru"),
        InlineKeyboardButton("EN", callback_data="lang=en"),
    )

    return btn

async def start_menu_btn(lang):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row(f"{context[lang]['my_id']}")
    btn.row(f"{context[lang]['my_username']}", f"{context[lang]['is_premium']}")

    return btn