def insertionSort(arr):
    print("insertionSort()")
    temp = 0
    for i in range(0, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp