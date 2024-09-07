def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print(10)
print_params(20, 'test')
print_params(b=25)  # работает, но подчеркивает желтым, ожидаемый параметр должен быть str
print_params(c=[1, 2, 3])  # работает, но подчеркивает желтым

values_list = [11, 'word', False]
values_dict = {'a': 20, 'b': 'Hello', 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['homework', 11]
print_params(*values_list_2, 42)  # работает



