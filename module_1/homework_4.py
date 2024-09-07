# Кортеж, кортеж с изменяемым списком внутри, преобразование кортежа в список
immutable_var = (1, 2, True, 'tuple')
immutable_var_ = tuple([1, 2, True, 'tuple'])
immutable_var_list = tuple(([1, 2], True, 'tuple'))
print(immutable_var)
print(immutable_var_)
print(immutable_var_list)
immutable_var_list[0][0] = 99
print(immutable_var_list)

# После того как кортеж создан, в него нельзя добавлять элементы, а также изменять их или удалять.
# immutable_var[0] = 100
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment

mutable_list = list(immutable_var)
mutable_list[0] = 100
print(mutable_list)
