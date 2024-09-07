from colorama import Fore
from math import inf

def test_function():
    def inner_function():
        print(Fore.RED + 'Im inside test_function')
    inner_function()

test_function()
print(Fore.GREEN + 'hello')

# inner_function()  при вызове функции inner_function() вне test_funtion()
# появляется ошибка, что функция не определена

print(inf)
def inf_(a, b):
    if a / b == inf:
        return inf

inf_(3, 0)
