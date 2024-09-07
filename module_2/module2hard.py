int_ = range(1, 21)
n = int(input("Введите значение от 3 до 20: "))

result = set()

for i in range(len(int_)):
    for j in range(i + 1, len(int_)):
        if n % (int_[i] + int_[j]) == 0:
            result.add((int_[i], int_[j]))

print(result, type(result))
result = list(result)
print(result)
result = result(''.join(result))
print(result)
# for i in result:
#     print(*i, end=' ')