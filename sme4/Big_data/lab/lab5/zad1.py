import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ts = pd.read_csv('amz.csv')
ts = ts.set_index('Date')

print(ts.head(10))
print(ts.dtypes)
print(ts.isnull().sum().sum())
print(ts.isna().sum().sum())
print(ts.shape)

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(np.arange(2331), ts['Close'], color='orange')
ax.set_title('Amazon closing stock price in time')
ax.grid()

plt.show()

print('mean: {0:.2f}, standard deviation: {1:.2f}, minimum: {2:.2f}, maximum: {3:.2f}'
      .format(np.mean(ts['Close']), np.std(ts['Close']), np.min(ts['Close']), np.max(ts['Close'])))