from monteCarloIntegration import monteCarloIntegration
from quadratureRule import quadratureRule
from probabilityDistributionDifference import probaiblityDistributionDifference

# 1)
mu1, mu2 = 0, 0
sd1 = 2
sd2 = 3
n = 1000

print(probaiblityDistributionDifference(mu1, sd1, mu2, sd2, n))

# 2) & 3)
def func(x):
    return x*x

a = -2.0
b = 2.0
n = 50000

print(monteCarloIntegration(a, b, n, func))
print(quadratureRule(a, b, n, func))