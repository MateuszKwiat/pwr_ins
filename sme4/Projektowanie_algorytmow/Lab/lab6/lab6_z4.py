import numpy as np

def mod_exp(a, n, m):
    result = 1
    
    while n > 0:
        if n % 2 == 1:
            result *= a

        n //= 2
        a *= a

    return result % m


def fermat(n, k):
    if n == 3 or n == 2:
        return True
    
    if n < 2:
        return False

    while k > 0:
        a = np.random.randint(2, n - 2)
        if mod_exp(a, n - 1, n) != 1:
            return False
        
        k -= 1

    return True

print(fermat(7919, 100))