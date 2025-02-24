from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from utils.db_api import database as db
from keyboards import ik,kb
from handlers.users import lt
import os

class UserState(StatesGroup):
    game = State()
    friend = State()
    delete_users = State()
    sender = State()
    add_btn_url = State()
    add_btn_name = State()

class Add_Channel(StatesGroup):
    c_id = State()
    c_name = State()
    c_url = State()

@dp.message_handler(state=UserState.game)
async def main(message: types.Message,state: FSMContext):
    answer = message.text
    photo_name = db.game(message.from_user.id)['photo_name']
    data_user_words = db.get_user(message.from_user.id)['total_words']
    data_user_rating = db.get_user(message.from_user.id)['rating']
    data_user_guessed = db.game(message.from_user.id)['guessed']
    if answer == photo_name:
        db.update_userfield(message.from_user.id, "total_words", data_user_words + 1)
        db.update_userfield(message.from_user.id, "rating", data_user_rating + 0.1)
        #db.add_word_to_database(message.from_user.id, data_user_guessed + ','+photo_name)
        await message.answer("🎉Поздаравляю!\n"
                            "Ты верно отгадал слово,хочешь продолжить?", reply_markup=ik.further)
        await state.finish()
    else:
        await message.answer("Вы неверно отдагали, попробуйте еще раз!💡\n"
                             "Игру всегда можно закончить кнопкой ниже.",reply_markup=ik.close)
        await UserState.game.set()


@dp.message_handler(state=UserState.friend)
async def main(message: types.Message,state: FSMContext):
    try:
        text = message.text
        user_id = db.get_user_for_username(text.replace("@","",1))['id']
        await state.finish()
        await message.answer(lt.profile_friend(user_id),reply_markup=kb.start)
    except Exception as e:
        await state.finish()
        await message.answer("❌Такого пользователя нет",reply_markup=kb.start)


@dp.message_handler(state=UserState.delete_users,content_types=types.ContentType.DOCUMENT)
async def main(message: types.Message,state: FSMContext):
    await state.finish()
    file_path = (await message.document.get_file())['file_path']
    await message.document.download()
    file = open(file_path,'r')
    msg = await message.answer("⏳")
    s = list(map(int, (file.read().split("\n"))[0:-1]))
    await msg.delete()
    file.close()
    db.delete_users_for_ids(s)
    os.remove(file_path)
    await message.answer("✅Мертвые пользователи удалены")


@dp.message_handler(state=UserState.sender,content_types=types.ContentType.ANY)
async def main(message: types.Message,state: FSMContext):
    msg_id = message.message_id
    await bot.copy_message(chat_id=message.from_user.id,from_chat_id=message.from_user.id,
                           message_id=msg_id)
    await message.answer("Рассылаем?",reply_markup=ik.send(msg_id))
    await state.finish()


@dp.message_handler(state=UserState.add_btn_url)
async def main(message: types.Message,state: FSMContext):
    url = message.text
    await state.update_data(url=url)
    await message.answer("Введите надпись на кнопке")
    await UserState.add_btn_name.set()

@dp.message_handler(state=UserState.add_btn_name)
async def main(message: types.Message,state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    data = await state.get_data()
    mrkp = ik.create_sender_mrkp(name,data['url'])
    message_to_send = await bot.copy_message(chat_id=message.from_user.id, from_chat_id=message.from_user.id,
                           message_id=data['message_id'],reply_markup=mrkp)
    await message.answer('Рассылаем?',reply_markup=ik.send(message_to_send.message_id))


@dp.message_handler(state=Add_Channel.c_id)
async def main(message: types.Message,state: FSMContext):
    try:
        await state.update_data(id=int(message.text))
        await message.answer("Введите имя канала",reply_markup=ik.cancel)
        await Add_Channel.c_name.set()
    except:
        await message.answer("❌Введите число",reply_markup=ik.cancel)

@dp.message_handler(state=Add_Channel.c_name)
async def main(message: types.Message,state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ссылку на вступление",reply_markup=ik.cancel)
    await Add_Channel.c_url.set()

@dp.message_handler(state=Add_Channel.c_url)
async def main(message: types.Message,state: FSMContext):
    data = await state.get_data()
    await state.finish()

    url = message.text
    db.create_adv_chat(data['id'],url,data['name'])
    await message.answer("✅Ваш канал успешно создан")