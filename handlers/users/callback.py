from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from handlers.users import misc as ms
from loader import dp
from keyboards import ik,kb
from aiogram.dispatcher import FSMContext
from utils.db_api import database as db
import random
import os
from handlers.users import lt
from data import text as txt
from states import st

@dp.callback_query_handler(state="*")
async def main(call: types.CallbackQuery, state: FSMContext):
    params = call.data.split("-")
    match params[0]:
        case "А":
            db.update_calculator(call.from_user.id, "А")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}",reply_markup=ik.game)
        case "Б":
            db.update_calculator(call.from_user.id, "Б")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "В":
            db.update_calculator(call.from_user.id, "В")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Г":
            db.update_calculator(call.from_user.id, "Г")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Д":
            db.update_calculator(call.from_user.id, "Д")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "E":
            db.update_calculator(call.from_user.id, "E")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ё":
            db.update_calculator(call.from_user.id, "Ё")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ж":
            db.update_calculator(call.from_user.id, "Ж")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "З":
            db.update_calculator(call.from_user.id, "З")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "И":
            db.update_calculator(call.from_user.id, "И")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Й":
            db.update_calculator(call.from_user.id, "Й")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "К":
            db.update_calculator(call.from_user.id, "К")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Л":
            db.update_calculator(call.from_user.id, "Л")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "М":
            db.update_calculator(call.from_user.id, "М")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Н":
            db.update_calculator(call.from_user.id, "Н")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "О":
            db.update_calculator(call.from_user.id, "О")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "П":
            db.update_calculator(call.from_user.id, "П")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Р":
            db.update_calculator(call.from_user.id, "Р")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "С":
            db.update_calculator(call.from_user.id, "С")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Т":
            db.update_calculator(call.from_user.id, "Т")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "У":
            db.update_calculator(call.from_user.id, "У")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ф":
            db.update_calculator(call.from_user.id, "Ф")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Х":
            db.update_calculator(call.from_user.id, "Х")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ц":
            db.update_calculator(call.from_user.id, "Ц")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ч":
            db.update_calculator(call.from_user.id, "Ч")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ш":
            db.update_calculator(call.from_user.id, "Ш")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Щ":
            db.update_calculator(call.from_user.id, "Щ")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ъ":
            db.update_calculator(call.from_user.id, "Ъ")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ы":
            db.update_calculator(call.from_user.id, "Ы")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ь":
            db.update_calculator(call.from_user.id, "Ь")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Э":
            db.update_calculator(call.from_user.id, "Э")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Ю":
            db.update_calculator(call.from_user.id, "Ю")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)
        case "Я":
            db.update_calculator(call.from_user.id, "Я")
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)

        case "del":
            db.update_game(call.from_user.id,"word","Ваш вариант: ")
            #db.create_game(call.from_user.id)
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}",reply_markup=ik.game)

        case "⌫":
            db.delete_one(call.from_user.id)
            data = db.game(call.from_user.id)
            await call.message.edit_caption(f"{data['word']}", reply_markup=ik.game)

        case "check":
            data = db.game(call.from_user.id)['photo_name']
            text = db.game(call.from_user.id)['word']
            split_text = text.split(":")
            words_after_colon = split_text[1].strip().split()
            word = words_after_colon[0]
            if data == word:
                data_user_words = db.get_user(call.from_user.id)['total_words']
                data_user_rating = db.get_user(call.from_user.id)['rating']
                data_user_guessed_words = db.game(call.from_user.id)['guessed_words']
                db.update_userfield(call.from_user.id,"total_words",data_user_words+1)
                db.update_userfield(call.from_user.id,"rating",data_user_rating+0.1)
                await call.message.delete()
                await call.message.answer("🎉Поздаравляю!\n"
                                          "Ты верно отгадал слово,хочешь продолжить?",reply_markup=ik.further)
            else:
                await call.answer("Не верно,попробуй еще раз!😊")

        case "close":
            await call.message.delete()
            await call.message.answer("😔Жаль что ты закончил игру, буду ждать тебя снова!\n\n"
                                      "Пользуйся клавиатурой ниже👇",reply_markup=kb.start)

        case "further":
            await call.message.delete()
            directory = ".\photo"
            all_files_in_directory = os.listdir(directory)
            random_file = random.choice(all_files_in_directory)
            file_name, file_extension = os.path.splitext(random_file)
            db.update_game(call.from_user.id, "photo_name", f"{file_name}")
            data_user_guessed = db.game(call.from_user.id)['guessed']
            with open(f"{directory}/{random_file}", 'rb') as photo:
                await call.bot.send_photo(call.message.chat.id, photo, caption=txt.game,reply_markup=ik.clue)
                await st.UserState.game.set()

        case "rating_user":
            await call.message.edit_text(lt.ratting(),reply_markup=ik.back)

        case "back_to_profile_menu":
            await call.message.edit_text(lt.profile(call.from_user.id),reply_markup=ik.user)

        case "close_game":
            await call.message.delete()
            await state.finish()
            await call.message.answer("Главное меню📕", reply_markup=kb.start)

        case "friend":
            await call.message.delete()
            await call.message.answer("Здесь вы сможете найти своего друга(подругу) и узнать его(ее) рейтинг!➰\n"
                                      "✏️Введите Username пользователя\n"
                                      "При поиске используйте \"@\" (@username)")
            await st.UserState.friend.set()

        case "clue":
            await call.message.delete()
            data_word = db.game(call.from_user.id)['photo_name']
            first_letter = data_word[:2]
            count = len(data_word)
            directory = ".\photo"
            photo_name = db.game(call.from_user.id)['photo_name']
            with open(f"{directory}/{photo_name}.webp", 'rb') as photo:
                await call.bot.send_photo(call.message.chat.id,photo)
                await call.message.answer(f"📌Первые две буквы вашего слова: <b>{first_letter}</b>\n"
                                          f"Cлово состоит из <b>{count}</b> букв.\n"
                                          f"Больше на это слово у вас нет подсказок!")
                await st.UserState.game.set()

        case "off_state":
            await call.message.delete()
            await call.message.answer("Действие отменено❎")
            await state.finish()

        case "send":
            await call.message.delete()
            message_id = int(params[1])
            data = await state.get_data()
            await state.finish()
            if len(data) != 0:
                name = data['name']
                url = data['url']
            else:
                name = "0"
                url = "0"
            from_chat_id = call.from_user.id
            await call.message.answer("Рассылка запущена")
            await ms.sender(message_id, from_chat_id, name, url)

        case 'add_button_to_send':
            message_id = int(params[1])
            await call.message.answer("Введите ссылку кнопки", reply_markup=ik.cancel)
            await st.UserState.add_btn_url.set()
            await state.update_data(message_id=message_id)

        case "chat_manage":
            chat_id = int(call.data.split("*")[1])
            match params[1]:
                case 'add_channel':
                    await call.message.delete()
                    await call.message.answer("Введите ID канала", reply_markup=ik.cancel)
                    await st.Add_Channel.c_id.set()
                case 'show':
                    await call.message.delete()
                    await call.message.answer(lt.adv_chat_stat(chat_id), reply_markup=ik.admin_delete_adv_chat(chat_id))
                case 'delete':
                    db.delete_adv_chat(chat_id)
                    await call.message.delete()
                    await call.message.answer("✅Чат удален")
        case "im_subscribed":
            sub_status = await ms.check_subscribes(call.from_user.id)
            if sub_status:
                await call.message.edit_text("Спасибо за поддержку нашего бота.\n"
                                             "<b>Благодаря Вам он остаётся полностью бесплатным.</b>\n"
                                             "")
            else:
                await call.answer("☹️Вы не подписаны на один из каналов")



