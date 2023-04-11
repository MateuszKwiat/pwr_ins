import time

def bubbleSortModified(arr):
#    print("bubbleSortModfied()")
    temp = 0
    didChange = False
    startTime = time.time()
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                didChange = True
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        if didChange == False:
            break
        didChange = False
    endTime = time.time()

    return endTime - startTime
