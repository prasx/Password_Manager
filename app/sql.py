import sqlite3
import json

# Глобальное соединение
conn = sqlite3.connect('app/users.db')

# Функция для создания таблицы в базе данных
def create_table():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, 
                 user_id TEXT UNIQUE,
                 pos TEXT,
                 data_reg TEXT,
                 last_password TEXT,
                 history_password TEXT)''')
    print("Таблица 'users' успешно создана или обновлена.")
    conn.commit()


# Функция для добавления нового пользователя
def add_user(user_id, pos, data_reg):
    c = conn.cursor()
    c.execute("INSERT INTO users (user_id, pos, data_reg, last_password, history_password) VALUES (?, ?, ?, ?, ?)",
              (user_id, pos, data_reg, '{}', '[]'))
    conn.commit()


# Функция для получения информации о пользователе
def get_user(user_id):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    return user


# Функция для обновления информации о последнем пароле пользователя
def update_last_password(user_id, last_password):
    c = conn.cursor()
    c.execute("UPDATE users SET last_password=? WHERE user_id=?", (last_password, user_id))
    conn.commit()


# Функция для добавления нового пароля в историю пользователя
def add_password_to_history(user_id, password_info):
    c = conn.cursor()
    c.execute("SELECT history_password FROM users WHERE user_id=?", (user_id,))
    history_password = json.loads(c.fetchone()[0])
    history_password.append(password_info)
    c.execute("UPDATE users SET history_password=? WHERE user_id=?", (json.dumps(history_password), user_id))
    conn.commit() 


# Функция для обновления позиции пользователя
def update_user_pos(user_id, new_position):
    c = conn.cursor()
    c.execute("UPDATE users SET pos=? WHERE user_id=?", (new_position, user_id))
    conn.commit() 



def close_connection():
    conn.close()
