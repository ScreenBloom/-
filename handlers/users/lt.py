from utils.db_api import database as db
from handlers.users import misc as ms

def profile(user_id):
    data = db.get_user(user_id)
    number = data['rating']
    formatted_number = "{:.1f}".format(number)
    text = f"""
    🙍‍♂ Пользователь: @{data['username']}

🆔 ID: <b>{user_id}</b>

🧠Ваш рейтинг: <b>{formatted_number}</b>

📎Количество отгаданных слов: <b>{data['total_words']}</b>"""
    return text


def ratting():
    data = db.get_top_users()
    user_id1 = data[0][1]
    user_id2 = data[1][1]
    user_id3 = data[2][1]
    rating_user1 = db.get_user(user_id1)['rating']
    rating_user2 = db.get_user(user_id2)['rating']
    rating_user3 = db.get_user(user_id3)['rating']
    formatted_number1 = "{:.1f}".format(rating_user1)
    formatted_number2 = "{:.1f}".format(rating_user2)
    formatted_number3 = "{:.1f}".format(rating_user3)
    text = f"""
    <b>Рейтинг</b> объективный инструмент оценки пользователей🌐

В этом месте вы можете отслеживать кто находится в топе!👁‍🗨
На данный момент лидируют:
➖➖➖➖➖➖➖➖
🥇 @{data[0][0]} 
   Его(ее) рейтинг: {formatted_number1} 🧠
➖➖➖➖➖➖➖➖
🥈 @{data[1][0]} 
   Его(ее) рейтинг: {formatted_number2} 🧠
➖➖➖➖➖➖➖➖
🥉 @{data[2][0]} 
   Его(ее) рейтинг: {formatted_number3} 🧠
"""
    return text


def profile_friend(user_id):
    data = db.get_user(user_id)
    number = data['rating']
    formatted_number = "{:.1f}".format(number)
    text = f"""
        🙍‍♂ Пользователь: @{data['username']}

🧠Рейтинг: <b>{formatted_number}</b>

📎Количество отгаданных слов: <b>{data['total_words']}</b>"""
    return text


def admin_stat():
    users = db.get_all_users()
    u_lst = []
    b_lst = []
    for i in [1, 7, 30]:
        u_lst.append(ms.get_count_of_user(i, users))
    text = "<b>📊Статистика</b>\n\n" \
           f"<b>👥Пользователей в боте:</b> {len(users)}\n" \
           f"<b>👤Пользователей за 1 день:</b> {u_lst[0]}\n" \
           f"<b>👤Пользователей за 7 дней:</b> {u_lst[1]}\n" \
           f"<b>👤Пользователей за 30 дней:</b> {u_lst[2]}\n\n"
    return text


def adv_chat_stat(chat_id):
    data = db.get_adv_chat(chat_id)
    return f"Канал: <b>{data['name']}</b>\n" \
           f"ID: <code>{data['id']}</code>\n\n" \
           f"Привидено пользователей: <b>{data['user_count']}</b>"