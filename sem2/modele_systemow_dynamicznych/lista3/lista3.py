from prey_predator import preyPredatorEuler
from lorenzSystem import lorenzSystemEuler
import matplotlib.pyplot as plt

plotLineWidth = 0.8
#          a    b    c    d
params = [1.2, 0.6, 0.3, 0.8]
dt = float(input("dt> "))
t = 25
xZero = 2
yZero = 1
xList, yList, timeList = preyPredatorEuler(xZero, yZero, params, t, dt)

plt.plot(timeList, xList, 'r', timeList, yList, 'b', lw=plotLineWidth)
plt.show()

params = [10, 8/3, 28]
xZero = yZero = zZero = 1
xList, yList, zList, timeList = lorenzSystemEuler(xZero, yZero, zZero, params, t, dt)

# Z(X)
plt.plot(xList, zList, 'r', lw=plotLineWidth)
plt.show()

# Y(X)
plt.plot(xList, yList, 'r', lw=plotLineWidth)
plt.show()

# Z(Y)
plt.plot(yList, zList, 'r', lw=plotLineWidth)
plt.show()

# 3D
ax = plt.figure().add_subplot(projection='3d')

ax.plot(xList, yList, zList, 'r', lw=plotLineWidth)
#ax.set_xlabel("X Axis")
#ax.set_ylabel("Y Axis")
#ax.set_zlabel("Z Axis")
#ax.set_title("Lorenz Attractor")

plt.show()