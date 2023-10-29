import numpy as np
import matplotlib.pyplot as plt

class UniformDistributionPlot:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.dist = np.random.randint(low, high, 100)
        self.avg = np.average(self.dist)
        self.median = np.median(self.dist)
        self.expectedValue = (low + high) / 2
        self.sd = np.std(self.dist)
        self.skew = 3 * ((self.avg - self.median) / self.sd)
        self.items = sorted(list(set(self.dist)))

    def cdf(self):
        res = []
        for i in self.items:
            res.append(np.count_nonzero(self.dist <= i)/100)

        return res
    
    def expectedCdf(self):
        res = []
        for i in self.items:
            res.append((i - self.low)/(self.high - self.low))

        return res


    def plot(self):
        print(f"Skewness: {self.skew}")
        plt.hist(self.dist)
        plt.axvline(x=self.avg, color='red', linewidth=2, label="Wartosc srednia")
        plt.axvline(x=self.expectedValue, color='green', linewidth=2, label="Wartosc oczekiwana")
        plt.axvline(x=self.median, color='purple', linewidth=2, label="Mediana")
        plt.legend()
        plt.title("Rozklad rownomierny")
        plt.show()

        plt.plot(self.cdf(), color='red', label="Obserwowana dystrybuanta")
        plt.plot(self.expectedCdf(), color='green', label="Oczekiwana dystrybuanta")
        plt.legend()
        plt.title("Dystrybuanta")
        plt.show()
