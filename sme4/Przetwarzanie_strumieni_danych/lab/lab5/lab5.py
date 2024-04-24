from scipy import signal

import numpy as np
import matplotlib.pyplot as plt

samples = 1000

t = np.linspace(0, 2 * np.pi, samples)
sig = np.sin(50 * t)

sp = abs(np.fft.fft(sig))

fig, ax = plt.subplots()

ax.plot(sp[:(np.isclose(sp, max(sp)).nonzero()[0][0]) * 2], color='orange')
ax.set_xlabel('frequency')
ax.set_ylabel('amplitude')
ax.set_title('amplitude spectrum for sine signal')

plt.show()