from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def diff(y, t, g, L):
    return [y[1], -(g / L) * np.sin(y[0])]


def pendulum_scipy(dt):
    y0 = [np.pi / 18, 0.0]
    g = 9.81
    L = 1.0
    dt = dt
    t_values = np.arange(0, 10, dt)

    sol = odeint(diff, y0, t_values, args=(g, L))

    plt.plot(t_values, sol[:,0])
    plt.title("kat odchylenia wahadelka")
    plt.show()

    return sol[:,0]

pendulum_scipy(0.001)