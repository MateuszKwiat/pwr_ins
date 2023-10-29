import numpy as np
from UniformDistributionPlot import UniformDistributionPlot
from NormalDistributionPlot import NormalDistributionPlot

#uniform distribution
uniformPlot = UniformDistributionPlot(0, 10)
uniformPlot.plot()

#normal distribution
normalPlot = NormalDistributionPlot(0, 3)
normalPlot.plot()
