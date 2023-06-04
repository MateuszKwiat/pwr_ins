from prey_predator import preyPredatorEuler
from lorenzSystem import lorenzSystemEuler
from prey_predator_odeint import prey_predator_odeint
from lorenzSystemOdeint import lorenzSystemOdeint

dt = float(input("dt> "))
t = 25

params = [1.2, 0.6, 0.3, 0.8]
xZero = 2
yZero = 1
prey_predator_odeint(xZero, yZero, params)
preyPredatorEuler(xZero, yZero, params, t, dt)

params = [10, 8/3, 28]
xZero = yZero = zZero = 1
lorenzSystemOdeint(xZero, yZero, zZero, params)
lorenzSystemEuler(xZero, yZero, zZero, params, t, dt)
