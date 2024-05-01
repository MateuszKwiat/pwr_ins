import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA   
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()
X = breast_cancer.data
Y = breast_cancer.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

fig, ax = plt.subplots(figsize=(14, 7))

for label in np.unique(Y):
    ax.scatter(X_pca[Y==label, 0], X_pca[Y==label, 1], label=breast_cancer.target_names[label], alpha=0.75)

ax.set_title('reduction of dimensions with PCA on breast cancer dataset')
ax.set_xlabel('first main component')
ax.set_ylabel('second main component')
ax.set_label(breast_cancer.target_names)
ax.legend(loc='upper right')

plt.show()