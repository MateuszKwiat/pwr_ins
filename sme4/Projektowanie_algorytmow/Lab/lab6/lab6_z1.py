from math import floor, sqrt

ls = []

def divisors(n, div=1):
    global ls

    if div == floor(sqrt(n)):
        return ls
    
    if n % div == 0:
        ls += [div]

    divisors(n, div + 1)

divisors(n=144)
print(ls)