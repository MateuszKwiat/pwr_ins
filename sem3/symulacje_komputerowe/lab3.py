from generators import Generators
from tests import Tests

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.mlab as mlab

sep = "----------"

def normalTestPrint(text, data1, data2, dataSize):
    print(f"{sep} {text}, data sample: {dataSize} {sep}")
    print(Tests.shapiroWilk(data1))
    print(Tests.shapiroWilk(data2))
    print(Tests.wilcoxon(data1, data2))
    print()

def plotData(data1):
    plt.hist(data1, density=True)
    x_axis = np.arange(-2.5, 2.5, 0.001)
    (mu, sigma) = norm.fit(data1)
    y = norm.pdf(x_axis, mu, sigma)
    plt.plot(x_axis, y, 'r--', linewidth=2)
    plt.show()

# Data  sample - 100
dataSize = 100
data1, data2 = Generators.boxMullerTransform(dataSize)
normalTestPrint("Box Muller Transform", data1, data2, dataSize)
plotData(data1)
plotData(data2)

data3, data4 = Generators.marsagliaPolarMethod(dataSize)
normalTestPrint("Marsaglia Polar Method", data3, data4, dataSize)
plotData(data3)
plotData(data4)

# Data sample - 20
dataSize = 20
data1, data2 = Generators.boxMullerTransform(dataSize)
normalTestPrint("Box Muller Transform", data1, data2, dataSize)
plotData(data1)
plotData(data2)


data3, data4 = Generators.marsagliaPolarMethod(dataSize)
normalTestPrint("Marsaglia Polar Method", data3, data4, dataSize)
plotData(data3)
plotData(data4)




#x_axis = np.arange(-4, 4, 0.001)
#plt.plot(x_axis, norm.pdf(x_axis, 0.2))
#plt.show()