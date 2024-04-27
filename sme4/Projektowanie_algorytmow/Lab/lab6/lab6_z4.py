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
            return 'composite'
        
        k -= 1

    return 'probably prime'

def find_s_and_d(n):
    s = 1
    d = 0

    while True:
        temp = n / (2**s)
        if not (temp).is_integer():
            return s - 1, d
        
        s += 1
        d = temp

def miller_rabin(n, k):
    for _ in range(k):
        a = np.random.randint(2, n - 2)
        s, d = find_s_and_d(n - 1)
        x = mod_exp(a, d, n)

        for _ in range(s):
            y = mod_exp(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return 'composite'
            
            x = y

        if y != 1:
            return 'composite'
        
    return 'probably prime'


number = 7911
iterations = 1000

print(fermat(number, iterations))
print(miller_rabin(number, iterations))