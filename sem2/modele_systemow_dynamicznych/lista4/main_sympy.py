import sympy
from sympy.utilities.lambdify import lambdify
import numpy as np

def pendulum_sympy(dt):
    t = sympy.symbols('t')
    x = sympy.Function('x')
    k = 10

    eq = sympy.Eq(x(t).diff(t, 2), -k*x(t))
    sol = sympy.dsolve(eq, ics={x(0): np.pi / 18, x(t).diff(t).subs(t, 0): 0})
    print(sol)
    sympy.plot(sol.rhs, (t, 0, 10), axis_center=(-1, -.2), title='kat odchylenia wahadelka')

    dt = dt
    t_values = np.arange(0, 10, dt)
    func = lambdify(t, sol.rhs, 'numpy')
    np_arr = func(t_values)

    return np_arr

pendulum_sympy(0.001)