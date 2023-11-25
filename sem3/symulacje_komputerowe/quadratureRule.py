def quadratureRule(a, b, n, func):
    sum = 0

    for k in range(1, n):
        sum += func(a + k * ((b-a)/n))

    return ((b-a)/n) * ((func(a)/2) + sum + (func(b)/2))