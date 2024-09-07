x = -38

print('hello')
if x < 0:
    print('x is less than zero')
print('goodbye')

# примеры
a, b = 10, 5

if a > b:
    print('a > b')
if a > b and a > 0:
    print('success')
if (a > b) and (a > 0 or b < 1000):
    print('success')
if 5 < b < 10:
    print('success')
else:
    print('wrong')

# можно сравнивать числа, строки, списки, вообще - все

if '34' > '123':
    print('success')
else:
    print('wrong')
if '123' > '12':
    print('success')
else:
    print('wrong')
if [1, 2] > [1, 1]:
    print('success')
else:
    print('wrong')

# что нельзя сравнивать разные типы

# if '6' > 5:
#     print('success') # Type Error
# if [5, 6] > 5:
#     print('success') # Type Error

# но

if [1, 2] != 5:
    print('success')
