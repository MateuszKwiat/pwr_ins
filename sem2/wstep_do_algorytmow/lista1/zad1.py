import numpy as np
import matplotlib.pyplot as plt
import random

class StudentGrades:
    def __init__(self, m, n):
        self.grades_array = np.array([2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5], dtype=float)
        self.rows = m
        self.col = n
        self.matrix = np.zeros((m, n), dtype=float)
        self.average = np.zeros((m, 1), dtype=float)

        for i in range(0, self.rows):
            for j in range(0, self.col):
                self.matrix[i][j] = self.grades_array[random.randrange(0, 7)]
        
        self.calcAverage()
        print(self.matrix)


    def calcAverage(self):
        for i in range(0, self.rows):
            self.average[i] = sum(self.matrix[i])/self.col


    def studentsFaliedClassesAmount(self, num):
        count_students = 0
        failed_classes_array = np.zeros((self.rows, 1))
        
        for i in range(0, self.rows):
            for j in range(0, self.col):
                if self.matrix[i][j] == 2.0:
                    failed_classes_array[i] = failed_classes_array[i] + 1
            
            if failed_classes_array[i] >= num:
                count_students = count_students + 1

        return count_students
        
    
    def highestLowestAverageGrades(self):
        temp_ar = np.sort(self.average, axis=None)
        
        index = np.where(self.average == temp_ar[0])
        print(f"Najnizsza srednia {temp_ar[0]}, oceny:")
        for i in range(0, self.col):
            print(self.matrix[index[0][0]][i], end=" ")

        index = np.where(self.average == temp_ar[self.rows-1])
        print(f"\nNajwyzsza srednia {temp_ar[self.rows-1]}, oceny:")
        for i in range(0, self.col):
            print(self.matrix[index[0][0]][i], end=" ")

        print()

    
    def topGradesStudent(self):
        top_grade = self.grades_array[6]
        count_grades = 0
        top_student = self.matrix[0]
        temp_grades = 0

        for i in reversed(range(0, 7)):
            if self.grades_array[i] in self.matrix:
                top_grade = self.grades_array[i]
                break

        for i in range(0, self.rows):
            temp_student = self.matrix[i]
            temp_grades = np.count_nonzero(temp_student == top_grade)
            if temp_grades > count_grades:
                top_student = temp_student
        
        print(f"Student z najwieksza iloscia oceny {top_grade}:")
        print(top_student)
    
    
    def classesHistogram(self):
        transposed_matrix = np.transpose(self.matrix)
        for i in range(0, self.col):
            plt.hist(transposed_matrix[i], bins=self.grades_array)
            plt.title(f"Histogram z przedmiotu no.{i}")
            plt.show()
#            plt.subplot(int(self.col / 2), int(self.col / int(self.col / 2)), i + 1)
#        plt.show()


    def studentsList(self):
        list_of_students = []
        
        for i in range(0, self.rows):
            if self.average[i] >= 4.5:
                list_of_students.append(self.matrix[i])

        return list_of_students