import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from matplotlib.widgets import Slider

# [ZAD_1]
def sine_sig(t, sig):
    ax.plot(t, sig, color='gray', zorder=0, label='sine wave')    

def samples(t, sig, val):
    ax.scatter(t[::val], sig[::val], s=s, color='black', zorder=2, label='sine samples')
# [ZAD_2]
def interpolate(t, sig, val):
    ax.plot(t, np.interp(t, t[::val], sig[::val]), color='orange', zorder=1, label='sine samples\ninterpolation')

s = 10
t = np.linspace(0, 20, 1000)
sig = np.sin(t)
freq = 1.0

fig, ax = plt.subplots()
sine_sig(t, sig)
samples(t, sig, 1)
ax.legend(loc='upper right')

ax_samp = fig.add_axes([0.12, 0.01, 0.55, 0.025])
ax_samp_slider = Slider(ax=ax_samp, label='sample', valmin=1, valmax=100, valinit=1, valstep=1, orientation='horizontal')

ax_freq = fig.add_axes([0.12, 0.05, 0.55, 0.025])
ax_freq_slider = Slider(ax=ax_freq, label='frequnecy', valmin=0.001, valmax=10, valinit=1, orientation='horizontal')

def update_samp(val):
    ax.clear()
    sine_sig(t, sig)
    samples(t, sig, ax_samp_slider.val)
    interpolate(t, sig, ax_samp_slider.val)

    ax.legend(loc='upper right')
    fig.canvas.draw_idle()

def update_freq(val):
    global sig

    freq = ax_freq_slider.val
    sig = np.sin(freq * t)

    ax.clear()
    sine_sig(t, sig)
    samples(t, sig, ax_samp_slider.val)
    interpolate(t, sig, ax_samp_slider.val)

    ax.legend(loc='upper right')
    fig.canvas.draw_idle()

ax_samp_slider.on_changed(update_samp)
ax_freq_slider.on_changed(update_freq)

plt.show()