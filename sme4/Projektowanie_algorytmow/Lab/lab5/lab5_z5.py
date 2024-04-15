import matplotlib.pyplot as plt
from time import time
import numpy as np

def find_max(ls):

    if len(ls) == 1:
        return ls[0]

    middle = len(ls) // 2
    left_max = find_max(ls[:middle])
    right_max = find_max(ls[middle:])

    return max(left_max, right_max)

def second_max(ls):
    max_val = find_max(ls)
    ls_copy = [*ls]
    ls_copy.remove(max_val)
    sec_max = find_max(ls_copy)

    return sec_max

def avg(ls):
    if len(ls) == 1:
        return ls[0], 1

    middle = len(ls) // 2
    left_sum, left_count = avg(ls[:middle])
    right_sum, right_count = avg(ls[middle:])

    total_sum = left_sum + right_sum
    total_count = left_count + right_count

    return total_sum, total_count

def merge(left, right):
    result = []
    index_left = index_right = 0

    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
    result.extend(left[index_left:])
    result.extend(right[index_right:])

    return result

def merge_sort(ls):
    if len(ls) <= 1:
        return ls

    middle = len(ls) // 2
    left = ls[:middle]
    right = ls[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

merge_time = []
find_max_time = []
find_second_max_time = []
avg_time = []

n = int(input())

for i in range(1000, n + 1, 100):
    ls = np.random.random(i)
    start_time = time()
    find_max(ls)
    end_time = time() - start_time

    find_max_time.append(end_time)

    start_time = time()
    second_max(ls)
    end_time = time() - start_time

    find_second_max_time.append(end_time)

    start_time = time()
    avg(ls)
    end_time = time() - start_time

    avg_time.append(end_time)

    start_time = time()
    merge_sort(ls)
    end_time = time() - start_time

    merge_time.append(end_time)

    print(i)

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].plot(np.arange(1000, n + 1, 100), merge_time, color='orange', label='merge time')
axes[0, 1].plot(np.arange(1000, n + 1, 100), find_max_time, color='red', label='max time')
axes[1, 0].plot(np.arange(1000, n + 1, 100), find_second_max_time, color='green', label='second max time')
axes[1, 1].plot(np.arange(1000, n + 1, 100), avg_time, color='navy', label='avg time')

axes[0, 0].legend(loc='upper right')
axes[0, 1].legend(loc='upper right')
axes[1, 0].legend(loc='upper right')
axes[1, 1].legend(loc='upper right')

plt.show()

