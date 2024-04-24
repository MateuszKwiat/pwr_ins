import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from scipy.interpolate import splrep, splev
from matplotlib.widgets import Slider

# [ZAD_1]
def sine_sig(t, sig):
    axes[0].plot(t, sig, color='gray', zorder=0, label='sine wave')
    axes[1].plot(t, sig, color='gray', zorder=0, label='sine wave')    

def samples(t, sig, val):
    axes[0].scatter(t[::val], sig[::val], s=s, color='black', zorder=2, label='sine samples')
    axes[1].scatter(t[::val], sig[::val], s=s, color='black', zorder=2, label='sine samples')
# [ZAD_2]
def interpolate(t, sig, val):
    axes[0].plot(t, splev(t, splrep(t[::val], sig[::val], k=2)), color='orange', zorder=1, label='sine samples\ninterpolation')
    axes[1].plot(t, whittaker_shannon_interpolation(t, sig[::val], val), color='orange', zorder=1, label='sine samples\ninterpolation')
# [ZAD_3]
def whittaker_shannon_interpolation(t, sig, val):
    interpolated_signal = []
    T = val * 0.02

    for tim in t:
        sum = 0
        for n in range(len(sig)):
            sum += sig[n] * np.sinc((tim - n * T) / T)
        
        interpolated_signal.append(sum)

    return interpolated_signal

def axes_info(axes):
    axes[0].set_ylim((-1.1, 1.1))
    axes[1].set_ylim((-1.1, 1.1))
    axes[0].legend(loc='upper right')
    axes[1].legend(loc='upper right')
    axes[0].set_title('scipy interpolation\nfor sine wave samples')
    axes[1].set_title('Whittaker-Shannon interpolation\nfor sine wave samples')


s = 10
t = np.linspace(0, 20, 1000)
sig = np.sin(t)
freq = 1.0
samp = 20

fig, axes = plt.subplots(nrows=1, ncols=2)
sine_sig(t, sig)
samples(t, sig, 1)

axes_info(axes)

ax_samp = fig.add_axes([0.12, 0.01, 0.55, 0.025])
ax_samp_slider = Slider(ax=ax_samp, label='sample', valmin=1, valmax=100, valinit=samp, valstep=1, orientation='horizontal')

ax_freq = fig.add_axes([0.12, 0.05, 0.55, 0.025])
ax_freq_slider = Slider(ax=ax_freq, label='frequnecy', valmin=0.001, valmax=10, valinit=freq, orientation='horizontal')

def update_samp(val):
    global samp

    samp = ax_samp_slider.val

    axes[0].clear()
    axes[1].clear()

    sine_sig(t, sig)
    samples(t, sig, samp)
    interpolate(t, sig, samp)

    axes_info(axes)
    fig.canvas.draw_idle()

def update_freq(val):
    global sig

    freq = ax_freq_slider.val
    sig = np.sin(freq * t)

    axes[0].clear()
    axes[1].clear()

    sine_sig(t, sig)
    samples(t, sig, ax_samp_slider.val)
    interpolate(t, sig, ax_samp_slider.val)

    axes_info(axes)
    fig.canvas.draw_idle()

ax_samp_slider.on_changed(update_samp)
ax_freq_slider.on_changed(update_freq)

plt.show()

fig, axes = plt.subplots(ncols=2)

interpolated_signal = splev(t, splrep(t[::samp], sig[::samp]))
ws_interpolated_signal = whittaker_shannon_interpolation(t, sig[::samp], samp)

abs_error = [abs(interp_val - sig_val) for interp_val, sig_val in zip(interpolated_signal, sig)]
ws_abs_error = [abs(interp_val - sig_val) for interp_val, sig_val in zip(ws_interpolated_signal, sig)]

axes[0].plot(t, abs_error, color='red')
axes[1].plot(t, ws_abs_error, color='red')

axes[0].set_title('absolute error for scipy\ninterpolation and sine wave')
axes[1].set_title('absolute error for Whittaker Shannon\ninterpolation and sine wave')
axes[0].set_xlabel('time')
axes[1].set_xlabel('time')
axes[0].set_ylabel('error value')
axes[1].set_ylabel('error value')

plt.show()  