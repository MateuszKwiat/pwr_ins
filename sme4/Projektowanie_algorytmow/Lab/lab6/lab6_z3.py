import matplotlib.pyplot as plt
from time import time
import numpy as np

def PFGCD(a, b):
    a_divs = []
    b_divs = []
    i = 2
    gcd = 1

    while a > 1:
        if a % i == 0:
            a_divs.append(i)
            a //= i
        else:
            i += 1

    i = 2
    while b > 1:
        if b % i == 0:
            b_divs.append(i)
            b //= i
        else:
            i += 1

    for i in range(len(a_divs)):
        for j in range(len(b_divs)):
            if a_divs[i] == b_divs[j] and a_divs[i] != 0 and b_divs[j] != 0:
                gcd *= a_divs[i]
                a_divs[i] = b_divs[j] = 0

    return gcd

def EGCD(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a    

print(PFGCD(108, 36))
print(EGCD(108, 36))

n = int(input('n: '))
m = int(input('m: '))

pfgcd_times = []
egcd_times = []

for q in range(1, m+1):
    start = time()
    PFGCD(n, q)
    pfgcd_times.append(time() - start)

    start = time()
    EGCD(n, q)
    egcd_times.append(time() - start)
    
fig, ax = plt.subplots()

ax.scatter(np.arange(len(pfgcd_times)), pfgcd_times, color='red',s=7, label='PFGCD')
ax.scatter(np.arange(len(egcd_times)), egcd_times, color='green',s=7, label='EGCD')

ax.set_xlabel('q value')
ax.set_ylabel('time')
ax.legend(loc='upper right')

plt.show()
