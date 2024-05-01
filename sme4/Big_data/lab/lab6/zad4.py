import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine

wine = load_wine()
X = wine.data
Y = wine.target

U, s, VT = np.linalg.svd(X)
k = 3

reduced_data = np.dot(U[:, :k], np.diag(s[:k]))

fig, ax = plt.subplots(figsize=(14, 7))

ax = plt.axes(projection='3d')

for label in np.unique(Y):
    ax.scatter3D(reduced_data[Y==label, 0], reduced_data[Y==label, 1], reduced_data[Y==label, 2], label=wine.target_names[label], alpha=0.75)

ax.set_title('reduction of dimensions with SVD on wine dataset')
ax.set_xlabel('first dimension')
ax.set_ylabel('second dimension')
ax.set_zlabel('third dimension')

ax.legend(loc='upper right')

plt.show()