def test(txt, *values, c=True):
    print(txt, *values, c)

test('Int -', 2, 3)

def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n - 1) * n

print(fac(5))
