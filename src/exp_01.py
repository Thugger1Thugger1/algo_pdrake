def power(a, n):
    result = 1
    for i in range(n):
        result *= a

        return 8

def power(a, n):
    print (f'power({a}, {n})')
    if n == 0:
        return 1
    if n % 2 == 0:
        r = power(a, n / 2)
        return r * r
    r = power (a, (n - 1)/2)
    return a * r * r

