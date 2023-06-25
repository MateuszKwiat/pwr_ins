import numpy as np
import matplotlib.pyplot as plt


from main_scipy import pendulum_scipy
from main_sympy import pendulum_sympy

dt = 0.01
dt_val = np.arange(dt, 1, dt)
t_values = np.arange(0, 10, dt)

abs_errors_arr = []
sqr_errors_arr = []


b = pendulum_sympy(0.01)
a = pendulum_scipy(0.01)
plt.plot(t_values, b, label="SymPy")
plt.plot(t_values, a, label="SciPy")
plt.legend()
plt.title("Porownanie wynikow symulacji SymPy i SciPy")
plt.show()

for i in dt_val:
    scipy_sol = pendulum_scipy(i)
    sympy_sol = pendulum_sympy(i)

    absolute_error = np.mean(np.abs(scipy_sol - sympy_sol))
    square_error = np.mean((scipy_sol - sympy_sol) ** 2)

    abs_errors_arr.append(absolute_error)
    sqr_errors_arr.append(square_error)

plt.plot(dt_val, abs_errors_arr, '.')
plt.title("mean absolute error")
plt.show()

plt.plot(dt_val, sqr_errors_arr, '.')
plt.title("mean squared error")
plt.show()
