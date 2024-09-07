def add_everything_up(a, b):
    try:
        return a + b

    except TypeError:
        return str(a) + str(b)

    finally:
        print('Функция выполняет строго ту обработку, которая написана в задании: ')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



