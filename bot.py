import logging
from aiogram import Bot, Dispatcher, executor, types
from bot_keyboards import *
from lang_context import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)


BOT_TOKEN = ""

bot = Bot(token=BOT_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

btn_names = [
    "Mening ID", "Mening username", "Premium egasimanmi?",
    "Мой ID", "Мой username", "У меня Premium?",
    "My ID", "My username", "have I Premium?"
    ]


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    btn = await choose_lang_btn()
    await message.answer("Til tanlang:", reply_markup=btn)


@dp.callback_query_handler(text_contains='lang')
async def choose_lang_callback(call: types.CallbackQuery, state: FSMContext):
    lang = call.data.split(":")[1]
    await call.message.delete()
    btn = await start_menu_btn(lang)
    await state.update_data(lang=lang)
    await call.message.answer(context[lang]["start_text"], reply_markup=btn)


@dp.message_handler(content_types=['text'])
async def menu_btns_handler(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    if text in btn_names:
        if "ID" in text:
            await message.answer(context[data['lang']]["your_id"].format(message.from_user.id))
        
        elif "username" in text:
            await message.answer(context[data['lang']]["your_username"].format(message.from_user.username))
        
        elif "premium" in text.lower():
            await message.answer(context[data['lang']]["your_premium"].format(message.from_user.is_premium))


if __name__ == '__main__':
    executor.start_polling(dp)