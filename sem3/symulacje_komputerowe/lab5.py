x = []
y = []
temp = ''
while True:
    temp = input("point x value: ")
    if temp == 'z':
        break
    x.append(int(temp))
    temp = input("point y value: ")
    if temp == 'z':
        break
    y.append(int(temp))

x.append(x[0])
y.append(y[0])

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()