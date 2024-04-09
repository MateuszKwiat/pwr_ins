import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy.interpolate import CubicHermiteSpline

df = pd.read_csv('amz.csv')
print(df.head())

print(df.shape)

tk = df['Date'][::80]

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(df['Date'], df['Close'], color='orange')
ax.set_xlabel('date')
ax.set_ylabel('price')
ax.set_title('Amazon stock prices')

plt.xticks(tk, rotation=45, ha='right')
plt.grid()

plt.show()

sample_rate = 5

x_values = np.array(np.arange(0, 2331)[::sample_rate])
y_values = df['Close'][::sample_rate]

dydx = np.gradient(y_values)
x_interpolated = np.array(np.arange(0, 2331))

spline = CubicHermiteSpline(x_values, y_values, dydx)
y_interpolated = spline(x_interpolated)

fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(df['Date'], df['Close'], color='gray', zorder=0, label='original data')
ax.plot(x_interpolated[:len(y_interpolated)], y_interpolated[:len(y_interpolated)], color='orange', zorder=1, label='interpolation')
# ax.scatter(x_values, y_values, s=5, color='black', zorder=2, label='sampled data points')

ax.set_xlabel('date')
ax.set_ylabel('price')
ax.set_title('Amazon stock prices')
ax.legend(loc='upper right')

plt.xticks(tk, rotation=45, ha='right')
plt.grid()

plt.show()