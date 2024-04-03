import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


t = np.linspace(0, 20, 1000)

sine_signal = np.sin(2 * np.pi * t)
square_signal = signal.square(2 * np.pi * t)
sawtooth_signal = signal.sawtooth(2 * np.pi * t)
chirp_signal = signal.chirp(t, f0=1, f1=0.5, t1=3)
superposition_signal = np.sin(2 * np.pi * t) + np.cos(2 * np.pi * t)
unit_impulse_signal = signal.unit_impulse(len(t))

# [ZAD_1]
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 8))
axes[0, 0].plot(*signal.periodogram(sine_signal), color='orange')
axes[0, 1].plot(*signal.periodogram(square_signal), color='orange')
axes[0, 2].plot(*signal.periodogram(sawtooth_signal), color='orange')

axes[1, 0].plot(*signal.welch(sine_signal), color='orange')
axes[1, 1].plot(*signal.welch(square_signal), color='orange')
axes[1, 2].plot(*signal.welch(sawtooth_signal), color='orange')

axes[0, 0].set_title('periodogram\nsine PSD')
axes[0, 1].set_title('periodogram\nsquare PSD')
axes[0, 2].set_title('periodogram\nsawtooth PSD')
axes[1, 0].set_title('welch\nsine PSD')
axes[1, 1].set_title('welch\nsquare PSD')
axes[1, 2].set_title('welch\nsawtooth PSD')

plt.show()

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 8))
axes[0, 0].plot(*signal.periodogram(chirp_signal), color='orange')
axes[0, 1].plot(*signal.periodogram(superposition_signal), color='orange')
axes[0, 2].plot(*signal.periodogram(unit_impulse_signal), color='orange')

axes[1, 0].plot(*signal.welch(chirp_signal), color='orange')
axes[1, 1].plot(*signal.welch(superposition_signal), color='orange')
axes[1, 2].plot(*signal.welch(unit_impulse_signal), color='orange')

axes[0, 0].set_title('periodogram\nchirp PSD')
axes[0, 1].set_title('periodogram\nsuppos PSD')
axes[0, 2].set_title('periodogram\nunit imp PSD')
axes[1, 0].set_title('welch\nchirp PSD')
axes[1, 1].set_title('welch\nsuppos PSD')
axes[1, 2].set_title('welch\nunit imp PSD')

plt.show()

# [ZAD_2]
def rxx(n, r, sig):
    sum = 0

    for x1, x2 in zip(sig, sig[r:]):
        sum += x1 * x2

    return sum / (n - r)

def psd(sig):
    result = []

    for r in range(len(sig)):
        result.append(rxx(len(sig), r, sig[:len(sig) - r]))
    
    return np.linspace(0, 0.5, len(sig)//2), np.fft.fft(result)[:len(sig)//2].real

# [ZAD_3]
fig, axes = plt.subplots(ncols=3)

signals = [np.sin(2 * np.pi * t), signal.square(2 * np.pi * t), 
           signal.sawtooth(2 * np.pi * t), signal.chirp(t, f0=1, f1=0.5, t1=3), 
           np.sin(2 * np.pi * t) + np.cos(2 * np.pi * t), signal.unit_impulse(len(t))]

i = 2

axes[0].plot(*signal.periodogram(signals[i]), color='red')
axes[1].plot(*signal.welch(signals[i]), color='orange')
axes[2].plot(*psd(signals[i]), color='green')

axes[0].set_title('periodogram\nsignal PSD')
axes[1].set_title('welch\nsignal PSD')
axes[2].set_title('definition\nsignal PSD')

plt.show()