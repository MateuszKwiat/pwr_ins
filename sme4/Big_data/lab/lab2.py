import numpy as np

# z2
arr2 = np.array([x for x in range(1, 11)])

print(f"--------------z2--------------\nMax value: {np.max(arr2)}, min value: {np.min(arr2)},\nmean: {np.mean(arr2)}, standard deviation: {round(np.std(arr2), 4)}\n")


# z3
arr3 = np.random.randint(10, size=(3, 4))

print(f"--------------z3--------------\narray:\n{arr3}\n")
print(f"array value at indexe [1][2]: {arr3[1][2]}\n\narray slice:\n{arr3[:2, 2:]}\n")

# z4
arr4 = np.random.randint(10, size=(10))
print(f"--------------z4--------------\n1D array: {arr4}")

arr4 = arr4.reshape((2, 5))
print(f"\nreshaped array:\n{arr4}")

arr4 = np.transpose(arr4)
print(f"\ntransposed array:\n{arr4}\n\narray's shape: {np.shape(arr4)}\n")

# z5
arr5_1 = np.random.randint(10, size=(5, 5))
arr5_2 = np.random.randint(10, size=(5, 5))

print(f"--------------z5--------------\n1st array:\n{arr5_1}\n\n2nd array:\n{arr5_2}")
print(f"\n1st array + 2nd array:\n{arr5_1 + arr5_2}\n\n1st array * 3:\n{arr5_1 * 3}\n")

# z6
arr6 = np.zeros((3, 3))
print(f"--------------z6--------------\narray:\n{arr6}")

arr6_1 = np.random.randint(10, size=(3, 3))
arr6 = np.concatenate((arr6, arr6_1), axis=1)
print(f"\nconcatenated array:\n{arr6}")

scalars = np.random.randint(10, size=6)

for i, scalar in zip(range(len(scalars)), scalars):
    arr6[:,i] *= scalar

print(f"\nconcatenated array multiplayed\ncolumn-wise by scalars: {scalars}:\n{arr6}\n")

# z7
arr7 = np.random.randint(1, 100, size=100)
print(f"--------------z7--------------\nrandom array:\n{arr7}\n\narray's sum: {np.sum(arr7)}")
print(f"array's mean: {np.mean(arr7)}\narray's standard deviation: {np.std(arr7)}\n")
print(f"array's cumulative sum: {np.cumsum(arr7)}\n\narray's cumulative product: {np.cumprod(arr7)}\n")

# z8
arr8 = np.random.randint(100, size=20)
print(f"--------------z8--------------\narray:\n{arr8}")
