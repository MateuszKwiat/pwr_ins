import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plotLineWidth = 0.8 

def derivative(variables, t, params):
    x = variables[0]
    y = variables[1]
    z = variables[2]

    sigma = params[0]
    beta = params[1]
    rho = params[2]

    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return ([dxdt, dydt, dzdt])


def lorenzSystemOdeint(xZero, yZero, zZero, params):
    t1 = np.linspace(0, 20, 20000)
    y0 = np.asarray([xZero, yZero, zZero])
    y = odeint(derivative, y0, t1, args=(params,))

    # Z(X)
    plt.plot(y[:,0], y[:,2], 'r', lw=plotLineWidth, label='Z(X)')
    plt.legend()
    plt.show()

    # Y(X)
    plt.plot(y[:,0], y[:,1], 'r', lw=plotLineWidth, label='Y(X)')
    plt.legend()  
    plt.show()

    # Z(Y)
    plt.plot(y[:,1], y[:,2], 'r', lw=plotLineWidth, label='Z(Y)')
    plt.legend() 
    plt.show()

    # 3D
    ax = plt.figure().add_subplot(projection='3d')

    ax.plot(y[:,0], y[:,1], y[:,2], 'r', lw=plotLineWidth)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Lorenz System")

    plt.show()