import numpy as np


# z2
arr = np.array([x for x in range(1, 11)])

print(f"z2\nMax value: {np.max(arr)}, min value: {np.min(arr)},\nmean: {np.mean(arr)}, standard deviation: {round(np.std(arr), 4)}\n")


# z3
arr1 = np.random.randint(10, size=(3, 4))

print(f"z3\narray:\n{arr1}\narray value at indexe [1][2]: {arr1[1][2]}\narray slice:\n{arr1[:2, 2:]}\n")

# z4
arr2 = np.random.randint(10, size=(10))
print(f"z4\n1D array: {arr2}")

arr2 = arr2.reshape((2, 5))
print(f"reshaped array:\n{arr2}")

arr2 = np.transpose(arr2)
print(f"transposed array:\n{arr2}\narray's shape: {np.shape(arr2)}\n")


# z5