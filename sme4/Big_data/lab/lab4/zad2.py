import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from scipy.interpolate import splrep, splev

df = pd.read_csv('weather_data.csv')

print(df.head())
print()
print(df.info())
print()

df['Station_1'] = df['Station_1'].fillna(df['Station_1'].mean())
df['Station_2'] = df['Station_2'].fillna(df['Station_2'].mean())
df['Station_3'] = df['Station_3'].fillna(df['Station_3'].mean())
df['Station_4'] = df['Station_4'].fillna(df['Station_4'].mean())
df['Station_5'] = df['Station_5'].fillna(df['Station_5'].mean())

print(df.head(df.shape[0]))

x = np.array(np.arange(df.shape[0]))

fig, axes = plt.subplots(ncols=3, figsize=(14, 5))
axes[0].scatter(x, df['Station_1'], color='black')
axes[0].set_title('station 1 data')
axes[0].set_ylabel('temperature')

axes[1].scatter(x, df['Station_2'], color='black')
axes[1].set_title('station 2 data')
axes[1].set_ylabel('temperature')

axes[2].scatter(x, df['Station_3'], color='black')
axes[2].set_title('station 3 data')
axes[2].set_ylabel('temperature')

plt.show()

tck0 = splrep(x, df['Station_1'], k=3)
x_interpolated0 = np.linspace(min(x), max(x), 100)
y_interpolated0 = splev(x_interpolated0, tck0)

tck1 = splrep(x, df['Station_2'], k=2)
x_interpolated1 = np.linspace(min(x), max(x), 100)
y_interpolated1 = splev(x_interpolated1, tck1)

tck2 = splrep(x, df['Station_3'], k=1)
x_interpolated2 = np.linspace(min(x), max(x), 100)
y_interpolated2 = splev(x_interpolated2, tck2)

fig, axes = plt.subplots(ncols=3, figsize=(14, 5))

axes[0].plot(x_interpolated0, y_interpolated0, color='orange', zorder=0, label='interpolation, k = 3')
axes[0].scatter(x, df['Station_1'], color='black', zorder=1, label='data')
axes[0].set_title('station 1 data')
axes[0].set_ylabel('temperatures')
axes[0].legend(loc='upper right')

axes[1].plot(x_interpolated1, y_interpolated1, color='orange', zorder=0, label='interpolation, k = 2')
axes[1].scatter(x, df['Station_2'], color='black', zorder=1, label='data')
axes[1].set_title('station 2 data')
axes[1].set_ylabel('temperatures')
axes[1].legend(loc='upper right')

axes[2].plot(x_interpolated2, y_interpolated2, color='orange', zorder=0, label='interpolation, k = 1')
axes[2].scatter(x, df['Station_3'], color='black', zorder=1, label='data')
axes[2].set_title('station 3 data')
axes[2].set_ylabel('temperatures')
axes[2].legend(loc='upper right')

plt.show()