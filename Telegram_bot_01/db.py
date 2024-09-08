import sqlite3


connection = sqlite3.connect('Telegram_bot_01/database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT,
username TEXT,
first_name TEXT,
block INT
);
''')


def add_users(user_id, username, first_name):
    check_user = cursor.execute('SELECT * FROM Users WHERE id=?', (user_id,))

    if check_user.fetchone() is None:
        cursor.execute(f'''
INSERT INTO Users VALUES('{user_id}', '{username}', '{first_name}', 0)
''')
    connection.commit()


def show_users():
    user_list = cursor.execute('SELECT * FROM Users')
    message = ''
    for user in user_list:
        user_id, username, first_name = user
        message += (f'{user_id} @{username} {first_name} \n')
    connection.commit()
    return message


def show_stat():
    count_users = cursor.execute('SELECT COUNT(*) FROM Users').fetchone()
    connection.commit()
    return count_users[0]


def add_to_block(input_id):
    cursor.execute = (f'UPDATE Users SET block=? WHERE id=?', (1, input_id))
    connection.commit()


def remove_block(input_id):
    cursor.execute = (f'UPDATE Users SET block=? WHERE id=?', (0, input_id))
    connection.commit()


def check_block(user_id):
    users = cursor.execute(f'SELECT block FROM Users WHERE id={user_id}').fetchone()
    connection.commit()
    return users


connection.commit()
connection.close()
