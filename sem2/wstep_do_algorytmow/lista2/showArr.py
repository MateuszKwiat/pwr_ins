def showArr(arr):
    i = 1
    for x in arr:
        print(x, end='\t')
        if i % 9 == 0:
            print()       
        i = i + 1

    print('\n')
