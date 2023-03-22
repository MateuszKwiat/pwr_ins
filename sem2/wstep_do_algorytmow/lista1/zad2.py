import numpy as np
import random

def calcDistance(rows, col):
    matrix1 = np.zeros((rows, col), dtype=int)
    matrix2 = np.zeros((rows, col), dtype=int)
    distance = 0

    for i in range(0, rows):
        for j in range(0, col):
            matrix1[i][j] = random.randint(-10, 10)
            matrix2[i][j] = random.randint(-10, 10)

    for i in range(0, rows):
        for j in range(0, col):
            distance = distance + abs(matrix1[i][j] - matrix2[i][j])

    return distance