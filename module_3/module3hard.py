def total_amount(data_structure):
    total = 0
    if isinstance(data_structure, (list, set, tuple)):
        for item in data_structure:
            total += total_amount(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total += total_amount(key)
            total += total_amount(value)
    elif isinstance(data_structure, int):
        total += data_structure
    elif isinstance(data_structure, str):
        total += len(data_structure)

    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = total_amount(data_structure)
print(result)



