from pprint import pprint

def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        try:
            results[f.__name__] = f(int_list)
        except Exception as e:
            results[f.__name__] = str(e)

    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

pprint(apply_all_func(['6', 20, 15, 9], len, sum, sorted, max, min))
