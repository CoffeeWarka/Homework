import sqlite3


connection = sqlite3.connect('crud_db.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connection.commit()
    connection.close()


def add_user(username, email, age):
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()

def is_included(username):
    check_user = cursor.execute(f'SELECT * FROM Users WHERE username = ?', (username, ))
    if check_user.fetchone() is None:
        return False
    else:
        return True
    




def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    prod_list = cursor.fetchall()
    connection.commit()
    return prod_list

cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Ускорин', 'Теряй калории быстро', 100))
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Ресторин', 'Восстановись после тренировки', 200))
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Смертин', 'Убей в себе лень', 300))
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Влюбин', 'Полюби заниматься спортом', 400))
connection.commit()


