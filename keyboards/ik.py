from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from utils.db_api import database as db

game = InlineKeyboardMarkup(row_width=6).add(
    InlineKeyboardButton(text="А",callback_data=f"А"),
    InlineKeyboardButton(text="Б",callback_data=f"Б"),
    InlineKeyboardButton(text="В",callback_data=f"В"),
    InlineKeyboardButton(text="Г",callback_data=f"Г"),
    InlineKeyboardButton(text="⌫",callback_data=f"⌫"),
    InlineKeyboardButton(text="Del",callback_data=f"del"),
    InlineKeyboardButton(text="Д",callback_data=f"Д"),
    InlineKeyboardButton(text="E",callback_data=f"E"),
    InlineKeyboardButton(text="Ё",callback_data=f"Ё"),
    InlineKeyboardButton(text="Ж",callback_data=f"Ж"),
    InlineKeyboardButton(text="З",callback_data=f"З"),
    InlineKeyboardButton(text="И",callback_data=f"И"),
    InlineKeyboardButton(text="Й",callback_data=f"Й"),
    InlineKeyboardButton(text="К",callback_data=f"К"),
    InlineKeyboardButton(text="Л",callback_data=f"Л"),
    InlineKeyboardButton(text="М",callback_data=f"М"),
    InlineKeyboardButton(text="Н",callback_data=f"Н"),
    InlineKeyboardButton(text="О",callback_data=f"О"),
    InlineKeyboardButton(text="П",callback_data=f"П"),
    InlineKeyboardButton(text="Р", callback_data=f"Р"),
    InlineKeyboardButton(text="С", callback_data=f"С"),
    InlineKeyboardButton(text="Т", callback_data=f"Т"),
    InlineKeyboardButton(text="У", callback_data=f"У"),
    InlineKeyboardButton(text="Ф", callback_data=f"Ф"),
    InlineKeyboardButton(text="Х", callback_data=f"Х"),
    InlineKeyboardButton(text="Ц", callback_data=f"Ц"),
    InlineKeyboardButton(text="Ч", callback_data=f"Ч"),
    InlineKeyboardButton(text="Ш", callback_data=f"Ш"),
    InlineKeyboardButton(text="Щ", callback_data=f"Щ"),
    InlineKeyboardButton(text="Ъ", callback_data=f"Ъ"),
    InlineKeyboardButton(text="Ы", callback_data=f"Ы"),
    InlineKeyboardButton(text="Ь", callback_data=f"Ь"),
    InlineKeyboardButton(text="Э", callback_data=f"Э"),
    InlineKeyboardButton(text="Ю", callback_data=f"Ю"),
    InlineKeyboardButton(text="Я", callback_data=f"Я")).add(
    InlineKeyboardButton(text="Проверить", callback_data=f"check")
)

further = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Далее🔜",callback_data="further"),
    InlineKeyboardButton(text="Закончить✖️",callback_data="close")
)

user = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="🧮Рейтинг",callback_data="rating_user"),
    InlineKeyboardButton(text="👥Поиск друга",callback_data="friend")
)

back = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="🔙",callback_data=f"back_to_profile_menu")
)

close = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="🕹Закончить",callback_data=f"close_game")
)

clue = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text="Подсказка",callback_data=f"clue")
)

cancel = InlineKeyboardMarkup().add(InlineKeyboardButton(text="🔄Отменить",callback_data='off_state'))



def send(message_id):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text="💬Разослать",callback_data=f'send-{message_id}'),
        InlineKeyboardButton(text="➕Добавить кнопку",callback_data=f'add_button_to_send-{message_id}'),
        InlineKeyboardButton(text="❌Отмена", callback_data='off_state')
    )

def create_sender_mrkp(name,url):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=name,url=url)
    )


def admin_adv_chats():
    datas = db.get_all_adv_chats()
    mrkp = InlineKeyboardMarkup(row_width=1)
    for data in datas:
        mrkp.add(
            InlineKeyboardButton(text=data['name'],callback_data=f'chat_manage-show-*{data["id"]}')
        )
    mrkp.add(
        InlineKeyboardButton(text="➕Добавить канал",callback_data='chat_manage-add_channel-*0')
    )
    return mrkp

def adv_chats():
    mrkp = InlineKeyboardMarkup(row_width=1)
    datas = db.get_all_adv_chats()
    for data in datas:
        mrkp.add(
            InlineKeyboardButton(text=data['name'],url=data['url'])
        )
    mrkp.add(
        InlineKeyboardButton(text="✅Я подписался",callback_data=f'im_subscribed')
    )
    return mrkp
def admin_delete_adv_chat(chat_id):
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text='🪣Удалить чат',callback_data=f'chat_manage-delete-*{chat_id}')
    )