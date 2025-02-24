import sqlite3
from data import config as cfg
from loader import bot
from datetime import datetime
conn = sqlite3.connect(r"utils\db_api\database.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id PRIMARY KEY,
    username TEXT,
    rating INT,
    total_words INT,
    date TEXT,
    ban INT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS game(
    id PRIMARY KEY,
    word TEXT,
    photo_name TEXT,
    guessed TEXT)
""")

cur.execute("""CREATE TABLE IF NOT EXISTS adv_chats(
    id INT PRIMARY KEY,
    user_count INT,
    url TEXT,
    name TEXT
)""")


cur.execute("""CREATE TABLE IF NOT EXISTS chanel(
    url TEXT,
    name TEXT,
    text TEXT,
    id INT
)""")
def get_all_users():
    result = []
    cortejs = cur.execute("SELECT * FROM users")
    for crtj in cortejs:
        result.append(parse_user_data(crtj))
    return result
def get_user_for_username(username):
    try:
        data = cur.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        return parse_user_data(data)
    except:
        pass
def get_top_users():
    result = []
    cur.execute("SELECT username,id FROM users ORDER BY rating DESC LIMIT 3")
    rows = cur.fetchall()# получение результатов запроса
    for row in rows:
        result.append(row)
    return result
def parse_user_data(data):
    return {'id':data[0],'username':data[1],'rating':data[2],'total_words':data[3],'date': data[4],'ban':data[5]}

def get_user(userId):
    try:
        data = cur.execute("SELECT * FROM users WHERE id = ?",(userId,)).fetchone()
        return parse_user_data(data)
    except:
        pass
#Users
def create_user(userId,username):
    try:
        date = str(datetime.now())[:19]
        cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",(userId,username,0,0,date,0))
        conn.commit()
    except Exception as e:
        pass

def add_word_to_database(user_id,update):
    cur.execute(f"UPDATE game SET guessed = ? WHERE id = ?", (update, user_id))
    conn.commit()

def create_game(userId):
    try:
        cur.execute("INSERT INTO game VALUES(?,?,?,?)",(userId,"none","none","Гуд"))
        conn.commit()
    except Exception as e:
        pass

def game(user_id):
    x = cur.execute("SELECT * FROM game WHERE id = ?", (user_id,)).fetchone()
    return parse_calculator(x)
def parse_calculator(data):
    return {'id': data[0], 'word': data[1], 'photo_name': data[2],'guessed': data[3]}


def update_calculator(user_id, word):
    try:
        cur.execute("UPDATE game SET word = word || ? WHERE id = ?", (word, user_id))
        conn.commit()
    except Exception as e:
        print(e)

def update_game(user_id,field,update):
    cur.execute(f"UPDATE game SET {field} = ? WHERE id = ?",(update,user_id))
    conn.commit()
def delete_game(user_id):
    try:
        cur.execute("DELETE FROM game WHERE id = ?", (user_id,))
        conn.commit()
    except Exception as e:
        print(e)

def delete_one(user_id):
    try:
        # Получаем текущее значение из базы данных
        cur.execute("SELECT word FROM game WHERE id = ?", (user_id,))
        current_decide = cur.fetchone()[0]

        # Удаляем последний символ из строки
        new_decide = current_decide[:-1]

        # Обновляем базу данных с новым значением
        cur.execute("UPDATE game SET word = ? WHERE id = ?", (new_decide, user_id))
        conn.commit()
    except Exception as e:
        print(e)

def delete_users_for_ids(ids: list):
    for id in ids:
        cur.execute(f"DELETE FROM users WHERE id = ?", (id,))
        conn.commit()

def get_user_ids():
    result = []
    cortejs = cur.execute("SELECT * FROM users")
    for crtj in cortejs:
        result.append(int(crtj[0]))
    return result

def update_userfield(user_id,field,update):
    cur.execute(f"UPDATE users SET {field} = ? WHERE id = ?",(update,user_id))
    conn.commit()

def plus_userfield(user_id,field,plus_value):
    old = cur.execute(f"SELECT {field} FROM users WHERE id = ?", (user_id,)).fetchone()[0]
    if old == None:
        old = ""
    new = old + plus_value
    update_userfield(user_id,field,new)


#adv_chat
def create_adv_chat(id,url,name):
    try:
        cur.execute("INSERT INTO adv_chats VALUES(?,?,?,?)",(id,0,url,name))
        conn.commit()
    except:
        pass
def get_adv_chat(id):
    x = cur.execute("SELECT * FROM adv_chats WHERE id = ?",(id,)).fetchone()
    return parse_adv_chat_data(x)
def get_all_adv_chats():
    res = []
    datas = cur.execute("SELECT * FROM adv_chats").fetchall()
    for data in datas:
        res.append(parse_adv_chat_data(data))
    return res
def get_all_adv_chats_id():
    res = []
    datas = cur.execute("SELECT * FROM adv_chats").fetchall()
    for data in datas:
        res.append(data[0])
    return res
def parse_adv_chat_data(data):
    return {'id':data[0],'user_count':data[1],'url':data[2],'name':data[3]}

def delete_adv_chat(id):
    cur.execute("DELETE FROM adv_chats WHERE id = ?",(id,))
    conn.commit()

def update_adv_chat_field(chat_id,field,update):
    cur.execute(f"UPDATE adv_chats SET {field} = ? WHERE id = ?",(update,chat_id))
    conn.commit()

def plus_adv_chat_field(chat_id,field,plus_value):
    old = cur.execute(f"SELECT {field} FROM adv_chats WHERE id = ?", (chat_id,)).fetchone()[0]
    if old == None:
        old = ""
    new = old + plus_value
    update_adv_chat_field(chat_id,field,new)

def plus_user_count_to_all():
    ids = get_all_adv_chats_id()
    for id in ids:
        plus_adv_chat_field(id,'user_count',1)