import imports as im

def bubbleSortsComparison(arr, n):
    bubbleSortTime = 0
    bubbleSortModifiedTime = 0
    bubbleSortModified1Time = 0

    im.randomFillArr.randomFillArr(arr, n)
    bubbleSortTime = im.bubbleSort.bubbleSort(arr)

    im.randomFillArr.randomFillArr(arr, n)
    bubbleSortModifiedTime = im.bubbleSortModified.bubbleSortModified(arr)

    im.randomFillArr.randomFillArr(arr, n)
    bubbleSortModified1Time = im.bubbleSortModified1.bubbleSortModified1(arr)

    print(f"Bubble sort time: {bubbleSortTime}")
    print(f"Bubble sort modified time: {bubbleSortModifiedTime}")
    print(f"Bubble sort modified 1 time: {bubbleSortModified1Time}")
