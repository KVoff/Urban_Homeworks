import sqlite3
import random


connection = sqlite3.connect('module_14/lesson_1.db')
cursor = connection.cursor()

# создаем таблицу с 4 полями:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
 ''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

# создаем пользователя:
# cursor.execute( 'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'ya@ya.ru', '40') )

# создаем много пользователей:
# for i in range(30):
#     cursor.execute( 'INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (f'newuser{i}', f'{i}ya@ya.ru', str(random.randint(20, 60))) )

'''
ОПЕРАТОРЫ в SQL запросах
«SELECT», «UPDATE», «DELETE», «FROM», «WHERE», «GROUP BY», «HAVING», «ORDER BY»
'''

''' UPDATE '''
# изменяем конкретному пользователю возраст:
# cursor.execute( 'UPDATE Users SET age = ? WHERE username = ?', ('29', 'newuser') )

''' DELETE '''
# удаляем пользователя
# cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser', ))

''' запись в переменную '''
# запрашиваем всю таблицу данных и записываем в переменную users, распечатываем всех:
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()

# for user in users:
#     print(user)

# запрашиваем пользователей с возрастом больше 29 и распечатываем:
# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (29, ))
# users = cursor.fetchall()

# for user in users:
#     print(user)

# пытаемся запросить средний возраст для каждого пользователя (получается среднее от 1 числа):
# cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY AGE')
# users = cursor.fetchall()

# for user in users:
#     print(user)


''' GROUP BY'''
# сотрируем всех по возрасту:
# cursor.execute('SELECT username, age FROM Users GROUP BY AGE')
# users = cursor.fetchall()

# for user in users:
#     print(user)


'''
# Функции в SQL запросах
# «COUNT», «SUM», «AVG», «MIN», «MAX»
'''

''' Count '''
#cursor.execute('SELECT COUNT(*) FROM Users')
#total_1 = cursor.fetchone()[0]  # fetchone !!!
# total_1 = cursor.fetchone()  # видим что тут только 1 элемент
# print(total_1)

# cursor.execute('SELECT COUNT(*) FROM Users WHERE age > ?', (29, ))
# total_1 = cursor.fetchone()[0]
# print(total_1)

''' SUM '''
# cursor.execute(' SELECT SUM(age) FROM Users')
# total_1 = cursor.fetchone()[0]
# print(total_1)

# cursor.execute(' SELECT SUM(age) FROM Users')
# total_1 = cursor.fetchone()[0]
# cursor.execute(' SELECT COUNT(*) FROM Users')
# total_2 = cursor.fetchone()[0]
# print(total_1, total_2, total_1/total_2)

''' AVERAGE '''
# cursor.execute('SELECT AVG(age) FROM Users')
# avg_age = cursor.fetchone()[0]
# print(avg_age)

''' MAX '''
# cursor.execute('SELECT MAX(age) FROM Users')
# avg_age = cursor.fetchone()[0]
# print(avg_age)

''' MIN '''
# cursor.execute('SELECT MIN(age) FROM Users')
# avg_age = cursor.fetchone()[0]
# print(avg_age)


# сохраняем таблицу:
connection.commit()
# выходим:
connection.close()


