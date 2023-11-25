from monteCarloIntegration import monteCarloIntegration

def func(x):
    return x*x

a = -2.0
b = 2.0
n = 50000

print(monteCarloIntegration(a, b, n, func))
