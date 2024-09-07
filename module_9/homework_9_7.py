
def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        numbers = (2, 3, 5, 7)
        if res < 0 or res == 0 or res == 1:
            return f'{res}: не простое и не составное.'
        if res in numbers:
            return f'{res}: Простое число.'
        elif res % 2 == 0 or res % 3 == 0 or res % 5 == 0 or res % 7 == 0:
            return f'{res}: Составное число.'
        else:
            return f'{res}: Простое число.'
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result_1 = sum_three(1, 3, 1)
print(result_1)


