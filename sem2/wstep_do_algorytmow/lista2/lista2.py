from meanAndMaxTime import meanAndMaxTime
from plotMeanAndMaxTime import plotMeanAndMaxTime
from bubbleSortsComparison import bubbleSortsComparison
from performanceTests import performanceTests

n = int(input("Wielkosc tablicy\n>"))
arr = [0]*n
meanAndMaxTime(arr, n, True)
print()

plotMeanAndMaxTime()
print()

n = int(input("Wielkosc tablicy\n>"))
arr = [0]*n
bubbleSortsComparison(arr, n)
print()

performanceTests()


