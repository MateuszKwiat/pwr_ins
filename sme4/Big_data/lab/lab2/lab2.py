import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#--------------------------------------    NUMPY   --------------------------------------
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

arr8 = np.sort(arr8)
print(f"\nsorted array in ascending order:\n{arr8}")

search_val = arr8[np.random.randint(len(arr8))]
print(f"\nbinary search for value: {search_val}\narray index: {np.searchsorted(arr8, search_val)}")

#--------------------------------------    PANDAS   --------------------------------------
# z9
names = ['Time', 'Open', 'High', 'Low', 'Close', 'Spread']
df = pd.read_csv('EURJPY1.csv', sep='\t', names=names, header=None)

print(f"--------------z9--------------\nData frame shape: {df.shape}\n")
print(f"{df.head(5)}\n")

# z10
print(f"--------------z10--------------\nColumns Time and Open:\n{df.filter(items=['Time', 'Open'])}\n")
print(f"Rows where Spread < 20:\n{df.loc[df['Spread'] < 20]}")

# z11
new_df = df.dropna()
print(f"--------------z11--------------\nData frame with removed empty cells:\n{new_df}\n")

new_df = new_df.drop_duplicates()
print(f"Data frame with removed duplicates:\n{new_df}\n")

# z12
sum12 = df['Spread'].sum()
mean12 = df['Spread'].mean()
count12 = df['Spread'].count()
print(f"--------------z12--------------\nSum of column Spread: {sum12}, mean: {mean12}, count: {count12}\n")

#--------------------------------------    MATPLOTLIB   --------------------------------------
# z16
x16 = np.linspace(0, 10, 100)
y16 = [y*2 for y in x16]

fig, ax = plt.subplots()

ax.plot(x16, y16, label='f(x)=2x')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Linear Function Plot')
ax.legend()

plt.show()

# z17
x17 = np.random.rand(100)
y17 = np.random.rand(100)
colors = np.random.rand(100)
sizes = np.random.randint(10, 100, 100)

fig, ax = plt.subplots()

ax.scatter(x17, y17, c=colors, s=sizes)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Scatter Plot of Randomly Generated Points')

plt.show()

# z18
categories = ['January', 'February','March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December']

sales = np.random.randint(1_000, size=12)

fig, ax = plt.subplots()

ax.bar(categories, sales, color='orange')

ax.set_xticklabels(categories, rotation=45)
ax.set_xlabel('Months')
ax.set_ylabel('Sales')
ax.set_title('Sales by Month')

plt.show()

# z19
data = np.random.normal(0, 2, 1000)

fig, ax = plt.subplots()

ax.hist(data, bins=30)

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Normal Distribution Histogram')

plt.show()

# z20
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
income = np.random.randint(1_000, size=4)

fig, ax = plt.subplots()

ax.pie(income, labels=quarters, colors=('lime', 'gold', 'darkgoldenrod', 'deepskyblue'))
ax.set_title('Income Over the Year by Quarters')

plt.show()

# z21
x21 = np.linspace(0, 30, 1000)
y21 = (np.sin(x21 * np.pi) + np.sin(x21 * np.e)) / 2

data1 = np.random.normal(0, 2, 1000)

x21_sc = np.random.rand(100)
y21_sc = np.random.rand(100)
colors = np.random.rand(100)
sizes = np.random.randint(10, 100, 100)

months = ['January', 'February','March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December']

sales = np.random.randint(1_000, size=12)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

axes[0, 0].plot(x21, y21, label='f(x)=(sin(xpi)+sin(xe))/2')
axes[0, 0].set_title('Sum of sine functions')

axes[0, 1].hist(data1, bins=30, color='orange')
axes[0, 1].set_title('Normal Distribution Histogram')

axes[1, 0].scatter(x21_sc, y21_sc, c=colors, s=sizes)
axes[1, 0].set_title('Scatter Plot of Randomly Generated Points')

axes[1, 1].pie(sales, labels=months)
axes[1, 1].set_title('Sales by Month')

plt.show()