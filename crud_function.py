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
    )
    ''')


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    prod_list = cursor.fetchone()
    return prod_list

get_all_products()
connection.commit()
connection.close()