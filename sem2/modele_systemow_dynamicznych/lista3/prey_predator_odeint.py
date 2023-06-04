from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

plotLineWidth = 0.8 

def derivative(variables, t, params):
    x = variables[0]
    y = variables[1]
    
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    dxdt = (a - b * y) * x
    dydt = (c * x - d) * y

    return ([dxdt, dydt])


def prey_predator_odeint(xZero, yZero, params):

    t1 = np.linspace(0, 25, 20000)
    y0 = np.asarray([xZero,yZero])
    y = odeint(derivative, y0, t1, args=(params,))

    plt.plot(t1, y[:,0], 'r', t1, y[:,1], 'b', lw=plotLineWidth)
    plt.legend(['X', 'Y'])
    plt.show()