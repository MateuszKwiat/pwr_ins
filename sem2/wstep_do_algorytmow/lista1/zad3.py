import numpy as np
import random

class Matrix:
    def __init__(self, n):
        self.matrix_size = n
        self.matrix = np.zeros((self.matrix_size, self.matrix_size + 1), dtype=float)
        print("Czy uzupelnic macierz liczbami losowymi? <2 - \"scenariusz testowy\", 1 - tak, 0 - nie>")
        choice = int(input())
        self.fillMatrix(choice)
        print(self.matrix)
   
    def fillMatrix(self, choice):
        if choice == 1:
            for i in range(0, self.matrix_size):
                for j in range(0, self.matrix_size + 1):
                    self.matrix[i][j] = random.randint(-10, 10)
                    self.matrix[i][j] = random.randint(-10, 10)
        elif choice == 2:
            self.matrix = np.array([[2, 3, -2, -3, 2, -4], 
                                   [3, 2, -3, -2, 3, -31], 
                                   [3, 0.2, -3, -4, 3, -30], 
                                   [-4, 1, -3, -0.4, 1, -9], 
                                   [-1, 1, -1, -1, 1, -1]])
        else:
            for i in range(0, self.matrix_size):
                for j in range(0, self.matrix_size + 1):
                    self.matrix[i][j] = float(input(f"[{i}][{j}] "))
    

    def uppperTriangularMatrix(self):
        ratio = 0
        for i in range(0, self.matrix_size - 1):
            if self.matrix[i][i] == 0 and i < self.matrix_size:
                for k in range(0, self.matrix_size + 1):
                    temp = self.matrix[i][k]
                    self.matrix[i][k] = self.matrix[i+1][k]
                    self.matrix[i+1][k] = temp

            for j in range(i + 1, self.matrix_size):
                ratio = self.matrix[j][i] / self.matrix[i][i]
                for k in range(0, self.matrix_size + 1):
                    self.matrix[j][k] = round(self.matrix[j][k] - self.matrix[i][k] * ratio, 2)   

        print(self.matrix) 
