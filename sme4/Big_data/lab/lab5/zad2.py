import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pywt

from scipy.signal import find_peaks

ts = pd.read_csv('amz.csv')
ts = ts.set_index('Date')

print(ts.head())

print('mean: {0:.2f}, standard deviation: {1:.2f}, quantile: {2:.2f}'.format(np.mean(ts['Close']), np.std(ts['Close']), np.quantile(ts['Close'], 0.5)))

coeffs = pywt.wavedec(ts['Close'], 'haar', level=1)

dwt_features = []

for i in range(2):
    dwt_features.extend(coeffs[i])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(dwt_features, color='orange')

ax.set_title('DWT coefficinet')
ax.set_xlabel('decomposition level')
ax.set_ylabel('coefficient')

plt.show()

cA, cD = pywt.dwt(ts['Close'], 'haar')

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(cA, color='orange', label='cA')
ax.plot(cD, color='red', label='cD')

ax.set_title('attribiutes values (wavelet analysis)')
ax.set_xlabel('time')
ax.set_ylabel('value')
ax.legend(loc='upper right')

plt.show()

peaks, _ = find_peaks(ts['Close'])
valleys, _ = find_peaks(-ts['Close'])

fig, ax = plt.subplots(figsize=(14, 7))

plt.plot(np.arange(ts.shape[0]), ts['Close'], color='orange', zorder=0)
plt.scatter(peaks, ts['Close'][peaks], s=5, color='green', zorder=1)
plt.scatter(valleys, ts['Close'][valleys], s=5, color='red', zorder=2)

plt.show()