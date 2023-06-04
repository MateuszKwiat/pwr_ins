from numpy import arange
import matplotlib.pyplot as plt

plotLineWidth = 0.8

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

    # Z(X)
    plt.plot(xList, zList, 'r', lw=plotLineWidth, label='Z(X)')
    plt.legend()
    plt.show()

    # Y(X)
    plt.plot(xList, yList, 'r', lw=plotLineWidth, label='Y(X)')
    plt.legend()  
    plt.show()

    # Z(Y)
    plt.plot(yList, zList, 'r', lw=plotLineWidth, label='Z(Y)')
    plt.legend() 
    plt.show()

    # 3D
    ax = plt.figure().add_subplot(projection='3d')

    ax.plot(xList, yList, zList, 'r', lw=plotLineWidth)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz System")

    plt.show()

