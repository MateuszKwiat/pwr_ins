import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class NormalDistributionPlot:
    def __init__(self, loc, sd):
        self.dist = np.random.normal(loc, sd, 100).astype(int)
        self.avg = np.average(self.dist)
        self.median = np.median(self.dist)
        self.expectedValue = loc
        self.mean = loc
        self.sd = sd
        self.skew = 3 * ((self.avg - self.median) / self.sd)
        self.items = sorted(list(set(self.dist)))
        
    def normalize(self, data):
        normalizedData = []
        xMin = min(data)
        xMax = max(data)
        for i in data:
            normalizedData.append((i - xMin)/(xMax - xMin))
        
        return normalizedData

    def cdf(self):
        res = []
        for i in self.items:
            res.append(np.count_nonzero(self.dist <= i)/100)

        return res
    
    def expectedCdf(self):
        res = []
        temp = []
        denominator = 1/self.sd * np.sqrt(2 * np.pi)
        for i in self.items:
            for j in range(-1000, i):
                temp.append(pow(np.e, -1/2 * pow((j - self.mean)/self.sd, 2)))
            res.append(denominator * np.trapz(temp))
            temp.clear()
        res = self.normalize(res)
        
        return res

    def plot(self):
        print(f"Skewness: {self.skew}")
        plt.hist(self.dist)
        plt.axvline(x=self.avg, color='red', linewidth=2, label="Wartosc srednia")
        plt.axvline(x=self.expectedValue, color='green', linewidth=2, label="Wartosc oczekiwana")
        plt.axvline(x=self.median, color='purple', linewidth=2, label="Mediana")
        plt.legend()
        plt.title("Rozklad normalny")
        plt.show()

        plt.plot(self.cdf(), color='red', label="Obserwowana dystrybuanta")
        plt.plot(self.expectedCdf(), color='green', label="Oczekiwana dystrybuanta")
        plt.legend()
        plt.title("Dystrybuanta")
        plt.show()
