import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('traffic.csv')
df.head()

df.shape

tk = df['Timestamp'][::5]

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(df['Timestamp'], df['Vehicle Count'], color='orange')

ax.set_xlabel('date and time')
ax.set_ylabel('vehicle count')
ax.set_title('amount of vehicles on Main Street in time')

plt.xticks(tk, rotation=45, ha='right')
plt.grid()

plt.show()

sample_rate = 2

x_values = np.array(np.arange(0, 100)[::sample_rate])
y_values = df['Vehicle Count'][::sample_rate]

from scipy.interpolate import CubicHermiteSpline

dydx = np.gradient(y_values)
x_interpolated0 = np.array(np.arange(0, len(df['Timestamp'])))

spline = CubicHermiteSpline(x_values, y_values, dydx)
y_interpolated0 = spline(x_interpolated0)

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(df['Timestamp'], df['Vehicle Count'], color='gray', zorder=0, label='original data')
ax.scatter(x_values, y_values, s=7, color='black', zorder=2, label='data samples')
ax.plot(x_interpolated0, y_interpolated0, color='orange', zorder=1, label='interpolated data')

ax.set_xlabel('date and time')
ax.set_ylabel('vehicle count')
ax.set_title('amount of vehicles on Main Street in time')
ax.legend(loc='upper right')

plt.xticks(tk, rotation=45, ha='right')
plt.grid()

plt.show()

from scipy.interpolate import splrep, splev

tck = splrep(x_values, y_values, k=4)
x_interpolated1 = np.array(np.arange(0, len(df['Timestamp'])))
y_interpolated1 = splev(x_interpolated1, tck)

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(df['Timestamp'], df['Vehicle Count'], color='gray', zorder=0, label='original data')
ax.scatter(x_values, y_values, s=7, color='black', zorder=2, label='data samples')
ax.plot(x_interpolated1, y_interpolated1, color='orange', zorder=1, label='interpolated data')

ax.set_xlabel('date and time')
ax.set_ylabel('vehicle count')
ax.set_title('amount of vehicles on Main Street in time')
ax.legend(loc='upper right')

plt.xticks(tk, rotation=45, ha='right')
plt.grid()

plt.show()

abs_error0 = [abs(data - interp) for data, interp in zip(df['Vehicle Count'], y_interpolated0)]
abs_error1 = [abs(data - interp) for data, interp in zip(df['Vehicle Count'], y_interpolated1)]

fig, axes = plt.subplots(ncols=2, figsize=(14, 7))

axes[0].plot(df['Timestamp'], abs_error0, color='red')
axes[1].plot(df['Timestamp'], abs_error1, color='red')

axes[0].set_ylabel('error')
axes[1].set_ylabel('error')
axes[0].set_xticks([])
axes[1].set_xticks([])

plt.show()