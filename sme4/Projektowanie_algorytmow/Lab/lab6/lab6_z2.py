from math import sqrt

def sieve(p):
    if p <= 1:
        return []
    
    x = [True for _ in range(p + 1)]

    for i in range(2, int(sqrt(p))):
        if x[i] == True:
            for j in range(i * i, p + 1, i):
                x[j] = False

    return [i for i in range(2, len(x)) if x[i] == True]

p = int(input())

print(sieve(p))