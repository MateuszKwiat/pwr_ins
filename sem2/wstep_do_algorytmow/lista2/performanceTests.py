import imports as im
from meanAndMaxTime import meanAndMaxTime
from math import log

def performanceTests():
    n = [10, 100, 1000]
    bubbleSortTime = [0] * 3
    insertionSortTime = [0] * 3
    selectionSortTime = [0] * 3
    bubbleTest = 0
    insertionTest = 0
    selectionTest = 0

    for i in range(0, len(n)):
        arr = [0]*n[i]
        bubbleSortTime[i], insertionSortTime[i], selectionSortTime[i] = meanAndMaxTime(arr, n[i], False)
        bubbleSortTime[i] = im.mean(bubbleSortTime[i])
        insertionSortTime[i] = im.mean(insertionSortTime[i])
        selectionSortTime[i] = im.mean(selectionSortTime[i])

    for i in range(0, len(n)):
        if bubbleSortTime[i] != 0:
            bubbleTest = (n[i] * log(bubbleSortTime[i])) / bubbleSortTime[i]
        else:
            bubbleTest = 0
        print("bubbleSort()")
        print(f"{n[i]} | {bubbleSortTime[i]} | {bubbleTest}\n")

        if insertionSortTime[i] != 0:
            insertionTest = (n[i] * log(insertionSortTime[i])) / insertionSortTime[i]
        else:
            insertionTest = 0
        print("insertionSort()")
        print(f"{n[i]} | {insertionSortTime[i]} | {insertionTest}\n")

        if selectionSortTime[i] != 0:
            selectionTest = (n[i] * log(selectionSortTime[i])) / selectionSortTime[i]
        else:
            selectionTest = 0
        print("selectionSort()")
        print(f"{n[i]} | {selectionSortTime[i]} | {selectionTest}\n")

        print()


