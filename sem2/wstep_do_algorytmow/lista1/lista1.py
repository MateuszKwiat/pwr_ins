import zad1
import zad2

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
print("Zadanie 2")
m = int(input("Wiersze macierzy\n>"))
n = int(input("Kolumny macierzy\n>"))
print(zad2.calcDistance(m, n))

# Zad 3