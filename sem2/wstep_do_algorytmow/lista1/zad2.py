import numpy as np
import random

def calcDistance(rows, col):
    matrix1 = np.zeros((rows, col), dtype=int)
    matrix2 = np.zeros((rows, col), dtype=int)
    distance = 0
    choice = 0

    print("Czy uzupelnic macierz liczbami losowymi? <2 - \"scenariusz testowy\", 1 - tak, 0 - nie>")
    choice = int(input())
    if choice == 1:
        for i in range(0, rows):
            for j in range(0, col):
                matrix1[i][j] = random.randint(-10, 10)
                matrix2[i][j] = random.randint(-10, 10)
    elif choice == 2:
        matrix1 = np.array([[2, 3, -2, -3],
                            [3, 2, -3, -2],
                            [3, 0.2, -3, -4]])
        matrix2 = np.array([[3, 2, -2, 3],
                            [3, 0.2, -4, 3],
                            [-4, 1, -0.4, 1]])
    else:
        print("Macierz 1")
        for i in range(0, rows):
            for j in range(0, col):
                matrix1[i][j] = float(input(f"[{i}][{j}] "))

        print("Macierz 2")
        for i in range(0, rows):
            for j in range(0, col):
                matrix2[i][j] = float(input(f"[{i}[{j}]] "))

    print(matrix1)
    print(matrix2)
    for i in range(0, rows):
        for j in range(0, col):
            distance = distance + abs(matrix1[i][j] - matrix2[i][j])

    return distance