from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards import ik,kb
from loader import dp
from utils.db_api import database as db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    db.create_user(message.from_user.id,message.from_user.username)
    db.create_game(message.from_user.id)
    image = "https://is4-ssl.mzstatic.com/image/thumb/Purple128/v4/99/b2/83/99b283c3-19d9-de68-0a88-6612e4f17c21/source/512x512bb.jpg"
    text = f"Привет, {message.from_user.full_name}!🤖\n"\
           "Я – бот, готов взяться за увлекательную игру в угадывание слов.\n" \
           "Давай проверим твои лингвистические способности и вместе 🧩 разгадаем загадку!"

    await message.answer_photo(photo=image,caption=text,reply_markup=kb.start)