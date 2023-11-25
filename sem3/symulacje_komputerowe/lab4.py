from monteCarloIntegration import monteCarloIntegration
from quadratureRule import quadratureRule

def func(x):
    return x*x

a = -2.0
b = 2.0
n = 50000

print(monteCarloIntegration(a, b, n, func))
print(quadratureRule(a, b, n, func))