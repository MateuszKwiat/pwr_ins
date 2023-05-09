from numpy import arange

def lorenzSystemEuler(xZero, yZero, zZero, params, t, dt):
    timeList = [round(x, 3) for x in arange(0, t, dt)]
    xPrev = xZero
    yPrev = yZero
    zPrev = zZero
    sigma = params[0]
    beta = params[1]
    rho = params[2]
    xList = [0]*len(timeList)
    yList = [0]*len(timeList)
    zList = [0]*len(timeList)

    for i in range(0, len(xList)):
        dxdt = sigma * (yPrev - xPrev)
        dydt = xPrev * (rho - zPrev) - yPrev
        dzdt = xPrev * yPrev - beta * zPrev

        xList[i] = xPrev + dxdt * dt
        yList[i] = yPrev + dydt * dt
        zList[i] = zPrev + dzdt * dt

        xPrev = xList[i]
        yPrev = yList[i]
        zPrev = zList[i]

    return xList, yList, zList, timeList
