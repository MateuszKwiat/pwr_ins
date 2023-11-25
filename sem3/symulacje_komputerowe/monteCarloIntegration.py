import random

def monteCarloIntegration(a, b, n, func):
    integral = 0.0

    for i in range(n):
        integral += func(random.uniform(a, b))

    return (b-a)/float(n)*integral