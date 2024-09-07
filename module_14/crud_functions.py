import sqlite3


def initiate_db():
    connection = sqlite3.connect('module_14/products.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('module_14/products.db')
    cursor = connection.cursor()

    # Получение всех продуктов
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products


# Пополнение продуктов, запускаем один раз:
def populate_products():
    connection = sqlite3.connect('module_14/products.db')
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
