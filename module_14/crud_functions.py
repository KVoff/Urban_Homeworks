import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')  # module_14/products.db (products.db)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users, если она еще не создана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')  # module_14/products.db (products.db)
    cursor = connection.cursor()

    # Получение всех продуктов
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('products.db')  # module_14/products.db (products.db)
    cursor = connection.cursor()

    # Добавление нового пользователя с начальными данными
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('products.db')  # module_14/products.db (products.db)
    cursor = connection.cursor()

    # Проверка наличия пользователя с таким именем
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    connection.close()
    return user is not None


# Пополнение продуктов, запускаем один раз:
def populate_products():
    connection = sqlite3.connect('products.db')  # module_14/products.db (products.db)
    cursor = connection.cursor()

    for i in range(1, 5):
        cursor.execute(
            'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
            (f'Продукт {i}', f'Описание {i}', i * 100)
        )

    connection.commit()
    connection.close()


if __name__ == '__main__':
    initiate_db()
    populate_products()
