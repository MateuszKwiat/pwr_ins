import time

def insertionSort(arr):
#    print("insertionSort()")
    temp = 0
    startTime = time.time()
    for i in range(0, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    endTime = time.time()

    return endTime - startTime