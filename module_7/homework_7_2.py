def custom_write(file_name, strings):
    book = {}

    file = open(file_name, 'w', encoding='utf-8')
    line_number = 1
    for line in strings:
        line_position = file.tell()
        file.write(line + '\n')
        book[(line_number, line_position)] = line
        line_number += 1
    file.close()
    return book


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# у вас в решении задачи ответы:

# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

# у меня получается:

# ((1, 0), 'Text for tell.')
# ((2, 15), 'Используйте кодировку utf-8.')
# ((3, 64), 'Because there are 2 languages!')
# ((4, 95), 'Спасибо!')

# возможно в вашем решении символ переноса строки идет с пробелом? '\n '
# потому что если считать символы вручную из файла, то у меня все сошлось)