import matplotlib.pyplot as plt
from scipy.special import erfinv
from time import time
from math import sqrt

a = 214013
c = 2531011
m = 2**32

def current_milliseconds_time():
    return round(time() * 1000)

def generate_random_numbers(seed=current_milliseconds_time()):
    return (a * seed + c) % m

def normalize(n):
    return n / m

def scale(n, low, high):
    return (n * (high - low)) + low if high > low else n

def mean(x):
    return sum(x) / len(x)

def variance(x):
    return sum([(xi - mean(x))**2 for xi in x]) / (len(x) - 1) 

def std(x):
    return sqrt(variance(x))

def uniform_distribution(size=1, low=0, high=0):
    rng_numbers = [generate_random_numbers()]
    for i in range(size - 1):
        rng_numbers.append(generate_random_numbers(seed=rng_numbers[i]))

    rng_numbers = [scale(normalize(i), low, high) for i in rng_numbers]

    return rng_numbers

def normal_quantile(p, loc, std):
    return loc + std * sqrt(2) * erfinv(2 * p - 1)

def normal_distribution(size=1, loc=0, std=1):
    return [normal_quantile(rng_uniform_val, loc, std) for rng_uniform_val in uniform_distribution(size=size)]

def plot_data_hist(data):
    plt.hist(data, bins=50, ec='blue', fc='navy', alpha=0.5)
    plt.xlabel('Value')

def uniform_distribution(size=1, low=0, high=0):
    rng_numbers = [generate_random_numbers()]
    for i in range(size - 1):
        rng_numbers.append(generate_random_numbers(seed=rng_numbers[i]))

    rng_numbers = [scale(normalize(i), low, high) for i in rng_numbers]

    return rng_numbers

def plot_data_hist(data):
    plt.hist(data, bins=50, ec='blue', fc='navy', alpha=0.5)
    plt.xlabel('Value')

uniform_dist = uniform_distribution(size=10_000)
normal_dist = normal_distribution(size=10_000)

fig, axes = plt.subplots(ncols=2, figsize=(10, 4))
for idx, (data, name, y_label) in enumerate(zip((uniform_dist, normal_dist), ('Uniform', 'Normal'), ('Frequency', ''))):
    plt.sca(axes[idx])
    plot_data_hist(data)
    plt.ylabel(y_label)
    plt.title(f'{name} distribution histogram\nmean=${round(mean(data), 3)}$, variance=${round(variance(data), 3)}$, std=${round(std(data), 3)}$')

plt.show()

