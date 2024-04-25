from scipy import signal
from scipy.integrate import quad

import numpy as np
import matplotlib.pyplot as plt

# [ZAD_1]
samples = 1000

t = np.linspace(0, 2 * np.pi, samples)
sig = np.sin(200 * t)

sp = abs(np.fft.fft(sig))

fig, ax = plt.subplots()

ax.plot(sp[:(np.isclose(sp, max(sp)).nonzero()[0][0]) * 2], color='orange')
ax.set_xlabel('frequency')
ax.set_ylabel('amplitude')
ax.set_title('amplitude spectrum for sine signal')

plt.show()

# [ZAD_2]
fig, ax = plt.subplots()

ax.plot((10 * np.log10(sp))[:(np.isclose(sp, max(sp)).nonzero()[0][0]) * 2], color='orange')
ax.set_xlabel('frequency')
ax.set_ylabel('amplitude (dB)')
ax.set_title('amplitude spectrum for sine singal in dB scale')

plt.show()

# [ZAD_3]
fig, ax = plt.subplots()
ax.plot(t, signal.sawtooth(4.5 * t))
plt.show()

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

sp = abs(np.fft.fft(np.sin(20 * t)))
ax[0, 0].plot(sp[:len(sp) // 2], color='orange')
ax[0, 0].set_title('amplitude spectrum\nfor sine signal')

sp = abs(np.fft.fft(signal.square(20 * t)))
ax[0, 1].plot(sp[:len(sp) // 2], color='orange')
ax[0, 1].set_title('amplitude spectrum\nfor square signal')

sp = abs(np.fft.fft(signal.sawtooth(4.5 * t)))
ax[0, 2].plot(sp[:len(sp) // 2], color='orange')
ax[0, 2].set_title('amplitude spectrum\nfor sawtooth signal')

sp = abs(np.fft.fft(signal.chirp(t, f0=2, f1=10, t1=t[-1])))
ax[1, 0].plot(sp[:len(sp) // 2], color='orange')
ax[1, 0].set_title('amplitude spectrum\nfor chirp signal')

sp = abs(np.fft.fft(np.sin(20 * t) + np.cos(30 * t)))
ax[1, 1].plot(sp[:len(sp) // 2], color='orange')
ax[1, 1].set_title('amplitude spectrum for super\nposition of sine and cosine signal')

sp = abs(np.fft.fft(signal.unit_impulse(len(t))))
ax[1, 2].plot(sp[:len(sp) // 2], color='orange')
ax[1, 2].set_title('amplitude spectrum for\nunit impulse signal')

plt.show()

# [ZAD_4*]
sig = np.sin(200 * t)
sp = np.fft.fft(sig)

fig, ax = plt.subplots()

ax.plot(np.linspace(0, 1, len(np.angle(sp))), np.angle(sp, deg=True), color='orange')

plt.show()

from scipy.interpolate import splrep, splev

# [ZAD_5]
t = np.linspace(0, 2 * np.pi, 1000)
sig = (signal.chirp(t, f0=2, f1=10, t1=t[-1]) * np.sin(t)) + ((t - np.pi)**2)

fig, ax = plt.subplots(ncols=2)

x = np.abs(signal.argrelmax(sig))

ax[0].plot(t, sig, color='orange')
ax[1].plot(t, sig, color='orange')

ax[0].plot(t, np.abs(signal.hilbert(sig)), color='red')
ax[1].plot(t, splev(t, splrep(*t[x], *sig[x], k=2)), color='green')

plt.show()

