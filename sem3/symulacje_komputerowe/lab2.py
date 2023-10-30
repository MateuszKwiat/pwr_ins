from generators import Generators
import matplotlib.pyplot as plt
import time

dataSize = 100

# LCG
generator = Generators.linearCongruentialGenerator(int(time.time() % 1000))
data = list(next(generator) for i in range(dataSize))

plt.hist(data)
plt.title("Linear congruential generator")
plt.show()

# MSM
generator2 = Generators.middleSquareMethod(int(time.time() % 10000))
data1 = list(next(generator2) for i in range(dataSize))

plt.hist(data1)
plt.title("Middle square method")
plt.show()

# BMT
data2, data3 = Generators.boxMullerTransform(dataSize)

fig, axs = plt.subplots(2)
fig.suptitle("Box muller transform")
axs[0].hist(data2)
axs[1].hist(data3)
plt.show()

# MPM
data4, data5 = Generators.marsagliaPolarMethod(dataSize)

fig, axs = plt.subplots(2)
fig.suptitle("Marsaglia polar method")
axs[0].hist(data4)
axs[1].hist(data5)
plt.show()
