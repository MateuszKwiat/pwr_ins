import pywt
import numpy as np
import matplotlib.pyplot as plt

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