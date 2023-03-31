import random

def randomFillArr(arr, n):
    for i in range(0, n):
        arr[i] = random.randint(0, n * 10)