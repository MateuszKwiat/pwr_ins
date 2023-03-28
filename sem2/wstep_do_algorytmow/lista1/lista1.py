"""
WdA labolatorium
Mateusz Kwiatkowski 264204
grupa 6, TP sr 13:15
L1
"""

import zad1
import zad2
import zad3
import zad4

# Zad 1
print("Zadanie 1")
m = int(input("Wiersze macierzy\n>"))
n = int(input("Kolumny macierzy\n>"))
zad1obj = zad1.StudentGrades(m, n)

num = int(input("Liczba niezaliczonych przedmiotow\n>"))
print(zad1obj.studentsFaliedClassesAmount(num))

zad1obj.highestLowestAverageGrades()

zad1obj.topGradesStudent()

zad1obj.classesHistogram()

temp_list = zad1obj.studentsList()
print(temp_list)

# Zad 2
print("\nZadanie 2")
m = int(input("Wiersze macierzy\n>"))
n = int(input("Kolumny macierzy\n>"))
print(zad2.calcDistance(m, n))

# Zad 3
print("\nZadanie 3")
n = int(input("Rozmiar macierzy nxn+1\n>"))
matrix = zad3.Matrix(n)
matrix.uppperTriangularMatrix()

# Zad 4
print("\nZadanie 4")
n = int(input("Liczba kolumn\n>"))
zad4obj = zad4.ReceiptChecker(n)
zad4obj.checkIfReceiptIsCorrect()