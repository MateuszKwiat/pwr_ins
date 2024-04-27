from math import pow

def EGCD(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a    

def mod_exp(a, n, m):
    result = 1
    
    while n > 0:
        if n % 2 == 1:
            result *= a

        n //= 2
        a *= a

    return result % m

def RSA(s, decypher=False):
    p = 191
    q = 193

    n = p * q

    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if EGCD(e, phi) == 1:
            break
        else:
            e += 1

    # d = 2
    # while True:
    #     if mod_exp(d, e, phi) == 1:
    #         break
    #     else:
    #         d += 1

    k = 2
    d = ((k * phi) + 1) / e

    if decypher:
        s = mod_exp(s, d, n)

    else:
        s = mod_exp(s, e, n)

    return s#, [e, n], [d, n]

def encoder(s):
    return [str(RSA(ord(l))) for l in s]

def decoder(s):
    return ''.join([chr(RSA(int(num), True)) for num in s])

enc = encoder('Test Message')
print(''.join(enc))

print(decoder(enc))
