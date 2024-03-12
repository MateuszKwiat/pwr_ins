import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


# [ZAD_1]
def add_to_plot(axes, t, signal, signal_title, row, col):
    axes[row, col].plot(t, signal, color='orange')

    if row == 1:
        axes[row, col].set_xlabel('t')
    
    if col == 0:
        axes[row, col].set_ylabel('Amplitude')

    axes[row, col].set_title(signal_title)


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

t = np.linspace(0, 20, 1000)


sine_signal = np.sin(t)
add_to_plot(axes, t, sine_signal, 'Sine Signal', 0, 0)

square_signal = signal.square(t)
add_to_plot(axes, t, square_signal, 'Square Signal', 0, 1)

sawtooth_signal = signal.sawtooth(t)
add_to_plot(axes, t, sawtooth_signal, 'Sawtooth Signal', 0, 2)

chirp_signal = signal.chirp(t, f0=1, f1=0.5, t1=3)
add_to_plot(axes, t, chirp_signal, 'Chirp Signal', 1, 0)

sine_signal = np.sin(t * np.e)
cosine_signal = np.cos(t * np.pi)
add_to_plot(axes, t, sine_signal + cosine_signal, 'Sine + Cosine Signal', 1, 1)

unit_impulse_signal = signal.unit_impulse(len(t))
add_to_plot(axes, t, unit_impulse_signal, 'Unit Impulse Signal', 1, 2)

plt.show()

# [ZAD_2]
df = pd.read_csv('Lista1_zad2.csv')

fig, ax = plt.subplots()
ax.plot(df['Time'], df['Signal'], color='orange')

ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Custom signal of trigonometric functions')

plt.show()

# [ZAD_3]
t = np.linspace(0, 20, 10000)
sig = np.sin(t * 4) + signal.square(t + np.pi) * signal.sawtooth(t * np.e)

fig, ax = plt.subplots()
ax.plot(t, sig, color='orange')

ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Custom signal of trigonometric functions')

plt.show()

data = {'Time' : t, 'Signal' : sig}
df = pd.DataFrame(data)
df.to_csv('Lista1_zad3.csv', index=False)