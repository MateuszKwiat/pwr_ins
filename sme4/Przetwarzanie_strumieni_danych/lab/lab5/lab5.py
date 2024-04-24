from scipy import signal

import numpy as np
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots()

ax.plot((10 * np.log10(sp))[:(np.isclose(sp, max(sp)).nonzero()[0][0]) * 2], color='orange')
ax.set_xlabel('frequency')
ax.set_ylabel('amplitude (dB)')
ax.set_title('amplitude spectrum for sine singal in dB scale')

plt.show()

# -------------------------------------------------------------------------------------------
# fig, ax = plt.subplots(nrows=2, ncols=3)

# ax[0, 0].plot(abs(np.fft.fft(np.sin(t))))
# ax[0, 1].plot(abs(np.fft.fft(signal.square(t))))
# ax[0, 2].plot(abs(np.fft.fft(signal.sawtooth(t))))
# ax[1, 0].plot(abs(np.fft.fft(signal.chirp(t, f0=1, f1=0.5, t1=3))))
# ax[1, 1].plot(abs(np.fft.fft(np.sin(t * np.e) + np.cos(t * np.pi))))
# ax[1, 2].plot(abs(np.fft.fft(signal.unit_impulse(len(t)))))

# plt.plot(abs(np.fft.fft(np.sin(t * 20) + np.cos(t * 40)))[:samples // 20])

# plt.show()

# sine_signal = np.sin(t)
# square_signal = signal.square(t)
# sawtooth_signal = signal.sawtooth(t)
# chirp_signal = signal.chirp(t, f0=1, f1=0.5, t1=3)
# sup_pos_signal = np.sin(t * np.e) + np.cos(t * np.pi)
# unit_impulse_signal = signal.unit_impulse(len(t))