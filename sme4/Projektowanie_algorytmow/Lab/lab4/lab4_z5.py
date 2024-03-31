from time import time
import numpy as np
import matplotlib.pyplot as plt

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


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 6))

size = 11

n = [*range(1, size)]

max_time_values = []
min_time_values = []
mean_time_values = []
time_values = []

for j in range(1, size):
    for _ in range(11):
        ls = np.random.rand(j)

        start_time = time()
        list_max(ls)
        time_values.append(time() - start_time)
    
    max_time_values.append(max(time_values))
    min_time_values.append(min(time_values))
    mean_time_values.append(np.mean(time_values))

    time_values.clear()

axes[0].plot(n, max_time_values, color='red', label='max time values')
axes[0].plot(n, mean_time_values, color='orange', label='mean time values')
axes[0].plot(n, min_time_values, color='green', label='min time values')

axes[0].set_title('find max value algo')
axes[0].set_xlabel('number of elements')
axes[0].set_ylabel('time')

axes[0].legend(loc='upper left')

max_time_values.clear()
min_time_values.clear()
mean_time_values.clear()

for j in range(1, size):
    for _ in range(11):
        matrix_A = np.random.rand(j, j)
        matrix_B = np.random.rand(j, j)

        start_time = time()
        matrix_multiplication(matrix_A, matrix_B)
        time_values.append(time() - start_time)

    max_time_values.append(max(time_values))
    min_time_values.append(min(time_values))
    mean_time_values.append(np.mean(time_values))

    time_values.clear()

axes[1].plot(n, max_time_values, color='red', label='max time values')
axes[1].plot(n, mean_time_values, color='orange', label='mean time values')
axes[1].plot(n, min_time_values, color='green', label='min time values')

axes[1].set_title('matrix multiplication algo')
axes[1].set_xlabel('matrix size')

axes[1].legend(loc='upper left')

max_time_values.clear()
min_time_values.clear()
mean_time_values.clear()

for j in range(1, size):
    for _ in range(11):
        ls = np.random.randint(-10, 10, j)
        
        start_time = time()
        find_zero_sums(ls)
        time_values.append(time() - start_time)

    max_time_values.append(max(time_values))
    min_time_values.append(min(time_values))
    mean_time_values.append(np.mean(time_values))

    time_values.clear()

axes[2].plot(n, max_time_values, color='red', label='max time values')
axes[2].plot(n, mean_time_values, color='orange', label='mean time values')
axes[2].plot(n, min_time_values, color='green', label='min time values')

axes[2].set_title('find zero sum combinations algo')
axes[2].set_xlabel('number of elements')

axes[2].legend(loc='upper left')

plt.show()