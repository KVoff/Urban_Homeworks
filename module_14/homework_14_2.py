import sqlite3


connection = sqlite3.connect('not_telegram.db')  # module_14/homework_14_2.db
cursor = connection.cursor()

# Создаем таблицу с 4 полями:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
 ''')

# заполняем базу на 10 пользователей:
for i in range(1, 11):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (f'newuser{i}', f'exemple{i}@ya.ru', i * 10, '1000')
    )

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = ?', (500, 1))

# Удаляем каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('DELETE FROM Users WHERE id % 3 = ?', (1, ))


# запрашиваем пользователей где возраст не равен 60 и распечатываем:
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
# print(type(users))

# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


# Удаление пользователя с id=6:
cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

# Подсчёт кол-ва всех пользователей:
cursor.execute('SELECT COUNT(*) FROM Users')
users_count = cursor.fetchone()[0]

# Подсчёт суммы всех балансов:
cursor.execute(' SELECT SUM(balance) FROM Users')
balance_sum = cursor.fetchone()[0]

print(balance_sum / users_count)

connection.commit()
connection.close()
