import numpy as np
import matplotlib.pyplot as plt
 
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data
Y = digits.target

tsne = TSNE(n_components=2)
X_embedded = tsne.fit_transform(X)

fig, ax = plt.subplots(figsize=(14, 7))

for label in np.unique(Y):
    ax.scatter(X_embedded[Y==label, 0], X_embedded[Y==label, 1], label=f'digit: {digits.target_names[label]}', alpha=0.75)

ax.set_title('reduction of dimensions with t-SNE on hand written digits dataset')
ax.set_xlabel('first dimension')
ax.set_ylabel('second dimension')

ax.legend(loc='upper right')

plt.show()