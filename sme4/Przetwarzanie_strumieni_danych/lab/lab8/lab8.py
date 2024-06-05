import matplotlib.pyplot as plt
import emd
import numpy as np
import pandas as pd

from scipy import signal

def plot_imfs(t, sig):
    imf = emd.sift.sift(sig)

    emd.plotting.plot_imfs(imf)
    plt.show()

    fig, ax = plt.subplots(nrows=imf.shape[1], ncols=2, figsize=(14, 8))

    for i in range(imf.shape[1]):
        ax[i, 0].plot(imf[:, i])
        ax[i, 1].plot(np.abs(np.fft.fft(imf[:, i]))[:200])

    plt.show()


sample_rate = 1000
m = 10
num_samples = sample_rate * m

# [ZAD_2]
t = np.linspace(0, m, num_samples)
sig = signal.chirp(t, f0=2, f1=10, t1=t[-1])

plot_imfs(t, sig)

# [ZAD_3]
t = np.linspace(0, m, num_samples)
sig = np.sin(30 * t) + np.cos(40 * t) + np.sin(70 * t)

plot_imfs(t, sig)

# [ZAD_4]
df = pd.read_csv('Data1.csv')
df = df.loc[df['sensor position'] == 'FP1']

t = np.array(df['time'])
sig = np.array(df['sensor value'])

plot_imfs(t, sig)