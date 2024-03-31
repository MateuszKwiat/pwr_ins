from time import time
import numpy as np

# Z1
def list_max(ls):
    max_elem = ls[0]

    for elem in ls:
        if elem > max_elem:
            max_elem = elem

    return max_elem

def list_second_max(ls):
    max_elem = ls[0]
    second_max_elem = ls[0]

    for i in range(len(ls) - 1):
        if ls[i + 1] > max_elem:
            max_elem = ls[i + 1]
        if ls[i] > second_max_elem and ls[i] < max_elem:
            second_max_elem = ls[i]

    if ls[len(ls) - 1] > second_max_elem and ls[len(ls) - 1] < max_elem:
        second_max_elem = ls[len(ls) - 1]

    return second_max_elem

def list_mean(ls):
    sum = 0
    count = 0

    for elem in ls:
        sum += elem
        count += 1

    return sum / count

# z2
def matrix_multiplication(matrix_A, matrix_B):
    size = len(matrix_A)
    result_matrix = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result_matrix

# z3
zero_sum_combinations = []

def calc_combinations(ls, combination='', index=0):
    global zero_sum_combinations

    if np.sum(list(map(int, combination.split()))) == 0:
        zero_sum_combinations.append(combination[1:])

    if index == len(ls):
        return

    for i in range(index, len(ls)):
        calc_combinations(ls, combination + ' ' + str(ls[i]), i + 1)


def find_zero_sums(ls):
    global zero_sum_combinations

    calc_combinations(ls)
    zero_sum_combinations.pop(0)

    return len(zero_sum_combinations) > 0

print('-----------------1-----------------')

n = int(input('n: '))

ls = np.random.rand(n)

start_time = time()
list_max(ls)
end_time = time() - start_time

print(f'list max elem time: {end_time}')

start_time = time()
list_second_max(ls)
end_time = time() - start_time

print(f'list second max elem time: {end_time}')

start_time = time()
list_mean(ls)
end_time = time() - start_time

print(f'list mean value time: {end_time}')

print('\n-----------------2-----------------')

n = int(input('n: '))

matrix_A = np.random.rand(n, n)
matrix_B = np.random.rand(n, n)

start_time = time()
matrix_multiplication(matrix_A, matrix_B)
end_time = time() - start_time

print(f'matrix multiplicaton time: {end_time}')

print('\n-----------------3-----------------')

n = int(input('n: '))

ls = np.random.randint(-10, 10, n)

start_time = time()
find_zero_sums(ls)
end_time = time() - start_time

print(f'zero sum combinations time: {end_time}')

