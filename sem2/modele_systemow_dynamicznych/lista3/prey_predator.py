from numpy import arange
import matplotlib.pyplot as plt

plotLineWidth = 0.8

def preyPredatorEuler(xZero, yZero, params, t, dt):
    timeList = [round(x, 3) for x in arange(0, t, dt)]
    xPrev = xZero
    yPrev = yZero
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    xList = [0]*len(timeList)
    yList = [0]*len(timeList)

    for i in range(0, len(xList)):
        dxdt = (a - b * yPrev) * xPrev
        dydt = (c * xPrev - d) * yPrev

        xList[i] = xPrev + dxdt * dt
        yList[i] = yPrev + dydt * dt

        xPrev = xList[i]
        yPrev = yList[i]

    

    plt.plot(timeList, xList, 'r', timeList, yList, 'b', lw=plotLineWidth)
    plt.legend(['X', 'Y'])
    plt.show()
