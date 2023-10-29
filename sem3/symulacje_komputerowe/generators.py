import numpy as np
import matplotlib.pyplot as plt

class Generators:
    def __init__(self):
        pass

    def linearCongruentialGenerator(x, m = 13462, a = 1255, c = 8574):
        while True:
            x = (a * x + c) % m
            yield x

    def middleSquareMethod(n):
        #...
        #...
        #...
        #...
        #...
        return 

    def boxMullerTransform(n):
        u1 = np.random.uniform(size=n)
        u2 = np.random.uniform(size=n)

        r = np.sqrt(-2 * np.log(u1))
        theta = 2 * np.pi * u2

        z0 = r * np.cos(theta)
        z1 = r * np.sin(theta)

        return z0, z1

    def marsagliaPolarMethod(n):
        def randomUniformPair():
            return np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        
        n1 = []
        n2 = []
        x = 0
        y = 0

        for i in range(0, n):
            x, y = randomUniformPair()
            while x*x + y*y >=1 or x*x + y*y <= 0:
                x, y = randomUniformPair()

            s = x*x + y*y
            const = np.sqrt((-2 * np.log(s))/s)
            n1.append(x * const)
            n2.append(y * const)

        return n1, n2
            
