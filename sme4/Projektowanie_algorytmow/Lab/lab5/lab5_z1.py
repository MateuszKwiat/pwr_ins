from math import sqrt

# 1)
def seq1(n):
    return 1 if n == 0 else 3**n + seq1(n - 1)

def seq1_analytical(n):
    return 3**(n + 1) // 2 

# 2)
def seq2(n):
    return 0 if n == -1 or n == 0 else n + seq2(n - 2)

def seq2_analytical(n):
    return (n // 2)**2 + (n if n % 2 != 0 else n // 2)

# 3)
def seq3(n):
    return 0 if n == 0 else (1 if n == 1 else seq3(n - 1) + seq3(n - 2))

def seq3_analytical(n):
    Phi = (1 + sqrt(5)) / 2
    phi = (1 - sqrt(5)) / 2

    return int((Phi**n - phi**n) / sqrt(5))

def check_for_N_elems(n):
    print('-----------------------sequence 1-----------------------')
    for i in range(n):
        print("{: <} {: <10} {: <} {: <10} {: <} {: <10}".
              format('numeric:', f'{seq1(i)}', 'analytical:', f'{seq1_analytical(i)}', 'difference:', f'{abs(seq1(i) - seq1_analytical(i))}'))

    print('\n-----------------------sequence 2-----------------------')
    for i in range(n):
        print("{: <} {: <10} {: <} {: <10} {: <} {: <10}".
              format('numeric:', f'{seq2(i)}', 'analytical:', f'{seq2_analytical(i)}', 'difference:', f'{abs(seq2(i) - seq2_analytical(i))}'))
        
    print('\n-----------------------sequence 3-----------------------')
    for i in range(n):
        print("{: <} {: <10} {: <} {: <10} {: <} {: <10}".
              format('numeric:', f'{seq3(i)}', 'analytical:', f'{seq3_analytical(i)}', 'difference:', f'{abs(seq3(i) - seq3_analytical(i))}'))
check_for_N_elems(15)