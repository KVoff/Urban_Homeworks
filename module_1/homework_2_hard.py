# n = int(input('Введите число от 3 до 20: '))
# print(type(n))
#
# for i in range(1, 9):
#     for j in range(1, 9):
#         sum_ = i + j
#         if n % sum_ == 0:
#             print(i, j)


int_ = range(1, 21)
n = int(input("3-21 "))

result = set()

for i in range(len(int_)):
    for j in range(i + 1, len(int_)):
        if n % (int_[i] + int_[j]) == 0:
            result.add((int_[i], int_[j]))
print(result, type(result))

# result = list(result)
# for i in result:
#     print(*i, end=' ')



