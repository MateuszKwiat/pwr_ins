from generators import Generators
from tests import Tests

sep = "----------"

def normalTestPrint(text, data1, data2, dataSize):
    print(f"{sep} {text}, data sample: {dataSize} {sep}")
    print(Tests.shapiroWilk(data1))
    print(Tests.shapiroWilk(data2))
    print(Tests.wilcoxon(data1, data2))
    print()

# Data  sample - 100
dataSize = 100
data1, data2 = Generators.boxMullerTransform(dataSize)
normalTestPrint("Box Muller Transform", data1, data2, dataSize)

data3, data4 = Generators.marsagliaPolarMethod(dataSize)
normalTestPrint("Marsaglia Polar Method", data3, data4, dataSize)

# Data sample - 20
dataSize = 20
data1, data2 = Generators.boxMullerTransform(dataSize)
normalTestPrint("Box Muller Transform", data1, data2, dataSize)

data3, data4 = Generators.marsagliaPolarMethod(dataSize)
normalTestPrint("Marsaglia Polar Method", data3, data4, dataSize)

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x_axis = np.arange(-4, 4, 0.001)
plt.plot(x_axis, norm.pdf(x_axis, 0.2))
plt.show()