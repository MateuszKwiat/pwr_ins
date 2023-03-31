import showArr
import randomFillArr
import bubbleSort
import insertionSort
import selectionSort

def arrOperations(arr, n):
    choice = input("0 - bubble sort, 1 - insertion sort, 2 - selection sor, q - quit\n>")
    if choice != '0' and choice != '1' and choice != '2':
        quit()

    functions = {'0': bubbleSort.bubbleSort, '1': insertionSort.insertionSort, '2': selectionSort.selectionSort}
    randomFillArr.randomFillArr(arr, n)
    showArr.showArr(arr)
    sort = functions[choice]
    sort(arr)
    showArr.showArr(arr)
