import imports as im

def arrOperations(arr, n):
    choice = input("0 - bubble sort, 1 - insertion sort, 2 - selection sor, q - quit\n>")
    if choice != '0' and choice != '1' and choice != '2':
        quit()

    functions = {'0': im.bubbleSort.bubbleSort, '1': im.insertionSort.insertionSort, '2': im.selectionSort.selectionSort}
    im.randomFillArr.randomFillArr(arr, n)
    im.showArr.showArr(arr)
    sort = functions[choice]
    sort(arr)
    im.showArr.showArr(arr)
