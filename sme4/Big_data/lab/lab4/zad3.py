import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('owid-energy-data(1).csv')
print(df.head())
print(df.shape)
print(df.info())
print(df.columns.to_list())
print(sorted(list(set(df['country']))))

df = df[['country', 'year', 'iso_code', 'population', 'gdp', 'energy_per_capita']]
print(df)
print(list(set(df['iso_code'])))

df = df.loc[df['iso_code'] == 'POL']
print(df)

df = df.drop(['gdp'], axis=1)
print(df)

print(list(pd.isna(df['energy_per_capita'])))

df = df.dropna()
print(df.head())

fig, ax = plt.subplots()
ax.scatter(df['year'], df['energy_per_capita'], color='black', s=7, label='energy usage')
ax.set_title('energy usage per capita')
ax.set_xlabel('year')
ax.set_ylabel('KWH')
ax.legend(loc='upper right')
plt.show()

x_values = df['year'][::3]
y_values = df['energy_per_capita'][::3]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color='black', s=7, label='energy usage')
ax.set_title('energy usage per capita')
ax.set_xlabel('year')
ax.set_ylabel('KWH')
ax.legend(loc='upper right')
plt.show()

def polynomial_interpolation(x_values, y_values, x):
    coefficients = np.polyfit(x_values, y_values, len(x_values) - 1)
    y = np.polyval(coefficients, x)
    
    return y

x_interpolated = np.linspace(min(x_values), max(x_values), 1000)
y_interpolated = polynomial_interpolation(x_values, y_values, x_interpolated)

from scipy.interpolate import splrep, splev

tck = splrep(x_values, y_values, k=2)
x_interpolated0 = np.linspace(min(x_values), max(x_values), 100)
y_interpolated0 = splev(x_interpolated0, tck)

fig, ax = plt.subplots(ncols=3, figsize=(14, 6))
ax[0].plot(df['year'], df['energy_per_capita'], color='orange', zorder=0)
ax[0].scatter(df['year'], df['energy_per_capita'], color='black', s=7, zorder=1, label='energy usage')
ax[0].set_title('energy usage per capita')
ax[0].set_xlabel('year')
ax[0].set_ylabel('KWH')
ax[0].legend(loc='upper right')

ax[1].plot(x_interpolated, y_interpolated, color='orange', zorder=0, label='interpolated data')
ax[1].scatter(x_values, y_values, color='black', s=7, zorder=1, label='partial data')
ax[1].set_title('energy usage interpolation - polynomial')
ax[1].set_xlabel('year')
ax[1].set_ylabel('KWH')
ax[1].legend(loc='upper right')

ax[2].plot(x_interpolated0, y_interpolated0, color='orange', zorder=0, label='interpolated data')
ax[2].scatter(x_values, y_values, color='black', s=7, zorder=1, label='partial data')
ax[2].set_title('energy usage interpolation - B splain')
ax[2].set_xlabel('year')
ax[2].set_ylabel('KWH')
ax[2].legend(loc='upper right')

plt.show()