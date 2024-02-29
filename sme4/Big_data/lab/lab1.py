# haslo mnbd2024
from math import sqrt

# zad 2
def z2():
    for i in range(1, 30):
        if i % 2 == 0:
            print(i)
        else:
            continue

# zad 3
def z3(x):
    i = 1
    sum = 0 

    while i < x:
        sum += i
        i += 1

    return sum

# zad 4
def z4(x):
    sum = 0
    for i in range(1, x):
        if i % 2 == 0:
            sum += i

    return sum

# zad 5
def z5():
    for i in range(100, -101, -1):
        if i % 2 == 0 and i % 3 != 0 and i % 8 != 0:
            print(i, end=" ")
        else:
            continue
    
    print()

# zad 6
def z6(n):
    sq_ls = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i, n):
            sq_ls[i][j] = i + 1
            sq_ls[j][i] = i + 1
            
        

    for i in range(n):
        print(sq_ls[i])

# zad 7
def z7(ls):
    sq_ls = [[0 for i in range(int(sqrt(len(ls))))] for j in range(int(sqrt(len(ls))))]
    k = 0
    for i in range(len(sq_ls)):
        for j in range(len(sq_ls)):
            sq_ls[j][i] = ls[k]
            k += 1
    
    for i in range(len(sq_ls)):
        print(sq_ls[i])

# zad 8
def z8(res, app):
    return res[:len(res) - 1] + app

# zad 9
def z9(ls, s):
    for i in range(len(ls)):
        ls[i] = s + ' ' + ls[i]

    return ls

# zad 10 
def z10(tps_ls):
    for i in range(len(tps_ls)):
        tps_ls[i] = tps_ls[i][:len(tps_ls[i])-1] + (0,)

    for i in range(len(tps_ls)):
        print(tps_ls[i])

# zad 11
def z11(tps_ls):
    res = []
    for tp in tps_ls:
        if tp:
            res.append(tp)

    return res
        
# zad 12
def z12(dict):
    res = 1
    for i in range(1, len(dict) + 1):
        res *= dict[f"f{i}"]
    
    return res

# zad 13
def z13(n):
    dict = {}
    for i in range(1, n + 1):
        dict[i] = pow(i, 4)

    return dict

# zad 14
def z14(dict):
    print(set(dict.values()))

z2()
print()
print(z3(5))
print()
print(z4(5))
print()
z5()
print()
z6(5)
print()
z7(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P'])
print()
print(z8([100, 90, 80, 70, 60, 50], [49, 39, 29, 19]))
print()
print(z9(['A', 'B', 'C', 'D'], 'Exit'))
print()
z10([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print()
print(z11([(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')]))
print()
print(z12({'f1': 4.8, 'f2': 2.4, 'f3': 1.2, 'f4': 0.6}))
print()
print(z13(6))
print()
z14({1: 'A201', 2: 'B218', 3:'H018', 4:'B218', 5:'H018', 6: 'G123', 7: 'A007', 8: 'G230'})