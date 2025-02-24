import states.st
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import ik,kb
from loader import dp,bot
import random
import os
from utils.db_api import database as db
from handlers.users import lt
from data import text as txt
from states import st
from data import config as cfg
from handlers.users import misc as ms



@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if str(message.from_user.id) in cfg.ADMINS:
        match message.text:
            case 'Админ':
                await message.answer("Админ меню", reply_markup=kb.admin)
                return
            case "📊Статистика":
                await message.answer(lt.admin_stat(), reply_markup=kb.admin)
            case "💬Рассылка":
                await message.answer("Пришлите мне сообщение, которое будет разослано пользователям")
                await st.UserState.sender.set()
                return
            case "🔃Выгрузить дб":
                document = ms.get_ids_files()
                await message.answer_document(document=document,
                                              caption="Файл с ID пользователей")
            case "👥ОП":
                await message.answer("<b>Ваши каналы:</b>", reply_markup=ik.admin_adv_chats())
                return
            case "🗑Удалить мертвых":
                await message.answer('Пришлите .txt файл с ID пользователей, которых нужно удалить из дб',
                                     reply_markup=ik.cancel)
                await st.UserState.delete_users.set()
    sub_status = await ms.check_subscribes(message.from_user.id)
    if sub_status:
        match message.text:
            case "🎲Играть":
                directory = ".\photo"
                all_files_in_directory = os.listdir(directory)
                random_file = random.choice(all_files_in_directory)
                file_name, file_extension = os.path.splitext(random_file)
                db.update_game(message.from_user.id, "photo_name", f"{file_name}")
                data_user_guessed = db.game(message.from_user.id)['guessed']
                with open(f"{directory}/{random_file}", 'rb') as photo:
                    await bot.send_photo(message.chat.id, photo, caption=txt.game,reply_markup=ik.clue)
                    await st.UserState.game.set()

            case "👤Профиль":
                await message.answer(lt.profile(message.from_user.id),reply_markup=ik.user)

            case "ℹ️INFO":
                await message.answer(txt.info,reply_markup=kb.start)

    else:
        await message.answer("Подпишитесь на каналы ниже, чтобы дальше использовать бота.\n"
                         "<b>Это нужно, для того, чтобы бот оставался бесплатным</b>",
                         reply_markup=ik.adv_chats())


