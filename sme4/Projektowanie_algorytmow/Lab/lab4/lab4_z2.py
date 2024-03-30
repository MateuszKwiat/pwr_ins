import numpy as np

def matrix_multiplication(matrix_A, matrix_B):
    size = len(matrix_A)
    result_matrix = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result_matrix[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result_matrix

matrix_A = np.array(([1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]))

matrix_B = np.array(([9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]))

print(matrix_A)
print()

size = int(input())
matrix_A = [[int(input()) for x in range(size)] for y in range(size)]
matrix_B = [[int(input()) for x in range(size)] for y in range(size)]

print()
print(matrix_multiplication(matrix_A, matrix_B))
