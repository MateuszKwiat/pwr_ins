import time

def bubbleSort(arr):
    print("bubbleSort()")
    temp = 0
    startTime = time.time()
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    endTime = time.time()

    return endTime - startTime
