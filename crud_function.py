import sqlite3


connection = sqlite3.connect('crud_db.db')
cursor = connection.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Ускорин', 'Теряй калории быстро', 100))
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Ресторин', 'Восстановись после тренировки', 200))
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Смертин', 'Убей в себе лень', 300))
cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
               ('Влюбин', 'Полюби заниматься спортом', 400))
connection.commit()
def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    prod_list = cursor.fetchall()
    connection.commit()
    connection.close()
    return prod_list