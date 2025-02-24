from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🎲Играть"),
    KeyboardButton("👤Профиль"),
    KeyboardButton("ℹ️INFO"))

close = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("Закончить"))


admin = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True).add(
    KeyboardButton("📊Статистика"),
    KeyboardButton("💬Рассылка"),
    KeyboardButton("🔃Выгрузить дб")).add(
    KeyboardButton("👥ОП"),
    KeyboardButton("🗑Удалить мертвых"),
)