def all_var(string):
    for length in range(len(string)):
        for index in range(len(string) - length):
            yield string[index:index+length + 1]

a = all_var('abc')
for i in a:
    print(i)
