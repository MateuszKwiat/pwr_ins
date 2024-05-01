import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import find_peaks

ts = pd.read_csv('amz.csv')
ts = ts.set_index('Date')

print(ts.head())

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(np.arange(ts.shape[0]), ts['Close'], color='orange')

ax.set_title('Amazon closing stock price')
ax.set_xlabel('date')
ax.set_ylabel('closing stock price')
ax.grid()

plt.show()

ts_freq = np.fft.fft(ts['Close']).real
peaks, _ = find_peaks(ts_freq[:300])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(np.arange(len(ts_freq[:300])), ts_freq[:300], color='orange')
ax.plot(peaks, ts_freq[peaks], 'x', color='green')

ax.set_title('fft of Amazon closing stock price')
ax.set_xlabel('freq')
ax.set_ylabel('amplitude')
ax.grid()

plt.show()

ts_PSD = np.abs(np.fft.fft(ts['Close']).real)**2
peaks, _ = find_peaks(ts_PSD[:300])

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(np.arange(len(ts_PSD[:300])), ts_PSD[:300], color='orange')
ax.plot(peaks, ts_PSD[peaks], 'x', color='green')

ax.set_title('PSD of Amazon closing stock price')
ax.set_xlabel('freq')
ax.set_ylabel('amplitude')
ax.grid()

plt.show()