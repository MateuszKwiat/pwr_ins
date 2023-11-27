from monteCarloIntegration import monteCarloIntegration
from quadratureRule import quadratureRule
from probabilityDistributionDifference import probaiblityDistributionDifference
from statisticalTestForIntegrals import statisticalTestForIntegrals

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

mtCar = monteCarloIntegration(a, b, n, func)
numeric = quadratureRule(a, b, n, func)

print(f"Monte Carlo integration: {mtCar},\nQuadrature rule method: {numeric},\nApproximations difference: {abs(mtCar - numeric)}")

# 4)
print(statisticalTestForIntegrals(mtCar, numeric))
