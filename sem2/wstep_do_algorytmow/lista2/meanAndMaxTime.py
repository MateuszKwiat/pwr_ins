import imports as im

def meanAndMaxTime(arr, n, showTimes):
    timeOfBubbleSorts = [0]*10
    timeOfInsertionSorts = [0]*10
    timeOfSelectionSorts = [0]*10

    for i in range(0, 10):
        im.randomFillArr.randomFillArr(arr, n)
        timeOfBubbleSorts[i] = im.bubbleSort.bubbleSort(arr)
        im.randomFillArr.randomFillArr(arr, n)
        timeOfInsertionSorts[i] = im.insertionSort.insertionSort(arr)
        im.randomFillArr.randomFillArr(arr, n)
        timeOfSelectionSorts[i] = im.selectionSort.selectionSort(arr)
        
    if showTimes == True:
        print(f"Bubble sort mean time: {im.mean(timeOfBubbleSorts)}, max time: {max(timeOfBubbleSorts)}")
        print(f"insertion sort mean time: {im.mean(timeOfInsertionSorts)}, max time: {max(timeOfInsertionSorts)}")
        print(f"Selection sort mean time: {im.mean(timeOfSelectionSorts)}, max time: {max(timeOfSelectionSorts)}")
        return 0
    
    else:
        return timeOfBubbleSorts, timeOfInsertionSorts, timeOfSelectionSorts