import random

x = []
randomX = []
randomY = []
y = []
temp = ''
n = 10000
while True:
    temp = float(input("point x value <0, 1>: "))
    if temp > 1 or temp < 0:
        break
    x.append(temp)
    temp = float(input("point y value <0, 1>: "))
    if temp > 1 or temp < 0:
        break
    y.append(temp)

x.append(x[0])
y.append(y[0])

for i in range(n):
    randomX.append(random.random())
    randomY.append(random.random())

insideShape = 0
total = 0

countOfCrossed = 0

for i in range(n): # random points loop
    for j in range(len(x) - 1): # user defined points
        if (randomY[i] >= y[j] and randomY[i] <= y[j + 1]) or (randomY[i] <= y[j] and randomY[i] >= y[j + 1]):
             if randomX[i] < x[j] + ((randomY[i] - y[j])/(y[j + 1] - y[j])) * (x[j + 1] - x[j]):
                  countOfCrossed += 1
    
    if countOfCrossed % 2 != 0:
         insideShape += 1
    total += 1
    countOfCrossed = 0

print(insideShape/total)

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
