import time

def selectionSort(arr):
#    print("selectionSort()")
    temp = 0
    startTime = time.time()
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    endTime = time.time()

    return endTime - startTime