import pywt
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider

# [ZAD_1]
make_wavelet = lambda name, isContinuous=False: pywt.ContinuousWavelet(name).wavefun(10) if isContinuous else pywt.Wavelet(name).wavefun(10)

wavelet_params = [['haar'], ['db4'], ['sym2'], ['coif2'], ['bior2.2'], ['gaus1', True], ['mexh', True], ['morl', True]]
wavelets = [make_wavelet(*name) for name in wavelet_params]

fig, axes = plt.subplots(nrows=2, ncols=4) 
fig.tight_layout()

for wavelet, params, ax in zip(wavelets, wavelet_params, axes.ravel()):
    ax.plot(*(wavelet[::-1] if params[-1] == True else (wavelet[-1], wavelet[1])), color='orange')
    ax.set_title(params[0] + ' wavelet')

plt.show()

# [ZAD_2]
def plot_wavelet(wavelet):
    ax.plot(wavelet[-1], wavelet[1], color='orange')
    ax.set_title('Daubechies wavelet')

def update(*args):
    wavelet = db_wavelet(ax_version_slider.val, ax_level_slider.val)
    
    ax.clear()
    plot_wavelet(wavelet)
    fig.canvas.draw_idle()

fig, ax = plt.subplots()

db_wavelet = lambda version=2, level=2: pywt.Wavelet(f'db{version}').wavefun(level)

ax_version = fig.add_axes([0.12, 0.01, 0.55, 0.025])
ax_version_slider = Slider(ax=ax_version, label='version', valmin=2, valmax=35, valinit=2, valstep=1, orientation='horizontal')

ax_level = fig.add_axes([0.12, 0.05, 0.55, 0.025])
ax_level_slider = Slider(ax=ax_level, label='level', valmin=2, valmax=10, valinit=2, orientation='horizontal')

plot_wavelet(db_wavelet())
ax_version_slider.on_changed(update)
ax_level_slider.on_changed(update)

plt.show()