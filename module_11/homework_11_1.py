print('''
Requests упрощает выполнение HTTP-запросов, предоставляя разработчику
интуитивный интерфейс. Эта библиотека полезна для работы с API и получения данных с сайтов.
''')

import requests

# Пример 1: Выполнение GET-запроса
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print("GET-запрос выполнен, статус:", response.status_code)

# Пример 2: Получение данных в формате JSON
data = response.json()
print("Данные о первом посте:", data[0])

# Пример 3: Выполнение POST-запроса
post_response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "New Post", "body": "Content of the post", "userId": 1}
)
print("POST-запрос выполнен, ответ:", post_response.json())

print('''
GET-запрос позволяет получать данные с удалённых серверов.
Обработка JSON: Requests автоматически парсит JSON, упрощая доступ к данным.
POST-запросы: Легко отправлять данные на сервер.
''')

print('''
Pandas используется для анализа и обработки данных.
Она предоставляет мощные структуры данных (например, DataFrame) и методы для
манипуляции таблицами.
''')

import pandas as pd

# Пример 1: Создание DataFrame из словаря
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print("DataFrame создан:\n", df)

# Пример 2: Фильтрация данных
filtered_df = df[df["Age"] > 28]
print("Фильтрация по возрасту > 28:\n", filtered_df)

# Пример 3: Экспорт в CSV
df.to_csv("employees.csv", index=False)
print("Данные экспортированы в employees.csv")

print('''
Создание DataFrame: Удобно работать с табличными данными.
Фильтрация: Легко применять условия и находить нужные записи.
Экспорт/импорт данных: Поддерживается множество форматов, включая CSV, Excel, SQL.
''')

print('''Выводы:
С помощью Requests я научился эффективно взаимодействовать с API,
а Pandas добавил возможность обработки данных в формате таблиц. 
Эти библиотеки существенно расширяют стандартные возможности Python. 
''')
