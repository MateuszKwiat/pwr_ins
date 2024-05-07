import numpy as np
import matplotlib.pyplot as plt

from scipy import signal, fft

# [ZAD_1]
def hamming_window(n, N, a0):
    return a0 - (1 - a0) * np.cos((2 * np.pi * n) / N)

def hann_window(n, N):
    return np.sin((np.pi * n) / N)**2

def blackman_window(n, N, alpha):
    a0 = (1 - alpha) / 2
    a1 = 1 / 2
    a2 = alpha / 2

    return a0 - a1 * np.cos((2 * np.pi * n) / N) + a2 * np.cos((4 * np.pi * n) / N) 

def dirchlet_window(n, N):
    return 1

def plot_window(window_function, params):
    N = 1000
    samples = np.linspace(0, params[0], N)
    window = [window_function(n, *params) for n in samples]
    transform = fft.fft(window)[:N // 2]
    freq = fft.fftfreq(N, max(samples))[:N // 2]

    fig, ax = plt.subplots(ncols=2, figsize=(12, 6))
    fig.tight_layout()
    
    ax[0].fill_between(x=samples, y1=window, where=(0 < samples) & (samples < params[0]), color='b', alpha=0.5)
    ax[0].set_xlabel('samples')
    ax[0].set_ylabel('amplitude')
    ax[0].set_title(f'{((str(window_function).split()[1]).split("_")[0]).title()} window function')

    ax[1].plot(freq, 2.0 / N * np.abs(transform), color='orange')
    ax[1].set_title(f'Fourier transform of {((str(window_function).split()[1]).split("_")[0]).title()} window function')
    ax[1].grid()

    plt.show()

N = 200 * np.pi
plot_window(hamming_window, [N, 0.54])
plot_window(hann_window, [N])
plot_window(blackman_window, [N, 0.16])
plot_window(dirchlet_window, [N])

# [ZAD_2]
def plot_window_view(window_function, sig, params):
    samp_size = 10_000
    
    window_size = 200 * np.pi
    window_view = [window_function(n, *params) * s for n, s in zip(np.linspace(0, window_size, samp_size), sig)]
    
    fig, ax = plt.subplots()
    
    ax.plot(np.linspace(0, window_size, samp_size), window_view, color='orange')

    ax.set_xlabel('samples')
    ax.set_ylabel('amplitude')
    ax.set_title(f'{((str(window_function).split()[1]).split("_")[0]).title()} window view')
    
    plt.show()

t = np.linspace(0, 200 * np.pi, 10_000)
sig = np.sin(2000 * t) + np.sin(300 * t) + np.sin(4000 * t)

plot_window_view(hamming_window, sig, [N, 0.54])
plot_window_view(hann_window, sig, [N])
plot_window_view(blackman_window, sig, [N, 0.16])
plot_window_view(dirchlet_window, sig, [N])
