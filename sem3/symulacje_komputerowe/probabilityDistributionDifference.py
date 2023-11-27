import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

def probaiblityDistributionDifference(mu1, sd1, mu2, sd2, n):
    nor1 = scipy.stats.norm(mu1, sd1)
    nor2 = scipy.stats.norm(mu2, sd2)

    valuesNor1 = np.linspace(-(sd1*3), sd1*3, n)
    valuesNor2 = np.linspace(-(sd2*3), sd2*3, n)

    diff = 0

    for i in range(n):
        diff += nor1.pdf(valuesNor1[i]) * np.log(nor1.pdf(valuesNor1[i]) / nor2.pdf(valuesNor2[i]))

    return diff