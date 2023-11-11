from generators import Generators
from tests import Tests

import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.stats import norm
from scipy.stats import uniform

sep = "----------"

def normalTestPrint(text, data1, data2, dataSize):
    print(f"{sep} {text}, data sample: {dataSize} {sep}")
    print(Tests.shapiroWilk(data1))
    print(Tests.shapiroWilk(data2))
    print(Tests.wilcoxon(data1, data2))
    print()

    return f"{text}, data sample: {dataSize}"

def uniformTestPrint(text, data, dataSize):
    print(f"{sep} {text}, data sample: {dataSize} {sep}")
    print(Tests.kolmogorovSmirnov(data))
    print(Tests.chiSquare(data))
    print()
    
    return f"{text}, data sample: {dataSize}"

def plotNormalData(data1, data2, text):
    fig, axs = plt.subplots(2)
    fig.suptitle(text)
    
    axs[0].hist(data1, density=True)
    x_axis = np.arange(-2.5, 2.5, 0.001)
    (mu, sigma) = norm.fit(data1)
    y = norm.pdf(x_axis, mu, sigma)
    axs[0].plot(x_axis, y, 'r--', linewidth=2)

    axs[1].hist(data2, density=True)
    x_axis = np.arange(-2.5, 2.5, 0.001)
    (mu, sigma) = norm.fit(data2)
    y = norm.pdf(x_axis, mu, sigma)
    axs[1].plot(x_axis, y, 'r--', linewidth=2)

    plt.show()

def plotUniformData(data, text):
    plt.hist(data, density=True)
    xmin, xmax = plt.xlim()
    x_axis = np.arange(xmin, xmax)
    (mu, sigma) = uniform.fit(data1)
    y = norm.pdf(x_axis, mu, sigma)
    plt.plot(x_axis, y, 'r--', linewidth=2)
    plt.title(text)
    plt.show()

# Normal distribution
# Data  sample - 100
dataSize = 100
data1, data2 = Generators.boxMullerTransform(dataSize)
text = normalTestPrint("Box Muller Transform", data1, data2, dataSize)
plotNormalData(data1, data2, text)

data3, data4 = Generators.marsagliaPolarMethod(dataSize)
text = normalTestPrint("Marsaglia Polar Method", data3, data4, dataSize)
plotNormalData(data3, data4, text)

# Data sample - 20
dataSize = 20
data1, data2 = Generators.boxMullerTransform(dataSize)
text = normalTestPrint("Box Muller Transform", data1, data2, dataSize)
plotNormalData(data1, data2, text)


data3, data4 = Generators.marsagliaPolarMethod(dataSize)
text = normalTestPrint("Marsaglia Polar Method", data3, data4, dataSize)
plotNormalData(data3, data4, text)

# Uniform distribution
# Data sample - 100
dataSize = 100
generator = Generators.linearCongruentialGenerator(int(time.time() % 1000))
data1 = list(next(generator) for i in range(dataSize))
text = uniformTestPrint("Linear Congruential Generator", data1, dataSize)
plotUniformData(data1, text)

generator2 = Generators.middleSquareMethod(int(time.time() % 10000))
data2 = list(next(generator2) for i in range(dataSize))
text = uniformTestPrint("Middle Square Method", data1, dataSize)
plotUniformData(data2, text)


# Data sample - 20
dataSize = 20
generator = Generators.linearCongruentialGenerator(int(time.time() % 1000))
data1 = list(next(generator) for i in range(dataSize))
text = uniformTestPrint("Linear Congruential Generator", data1, dataSize)
plotUniformData(data1, text)

generator2 = Generators.middleSquareMethod(int(time.time() % 10000))
data2 = list(next(generator2) for i in range(dataSize))
text = uniformTestPrint("Middle Square Method", data1, dataSize)
plotUniformData(data2, text)