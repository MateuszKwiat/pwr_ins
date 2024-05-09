import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import NMF
from sklearn.datasets import fetch_lfw_people

from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

lfw_people = fetch_lfw_people()

X = lfw_people.data
Y = lfw_people.target

nmf_model = NMF(n_components=3, max_iter=1000)

nmf_model.fit(X)
W = nmf_model.transform(X)
H = nmf_model.components_

fig, ax = plt.subplots(ncols=2, figsize=(14, 7))

ax[0].imshow(W, cmap='viridis', aspect='auto')
ax[1].imshow(H, cmap='viridis', aspect='auto')

ax[0].set_xlabel('components')
ax[0].set_ylabel('samples')
ax[0].set_title('base matrix (W)')

ax[1].set_xlabel('attributes')
ax[1].set_ylabel('components')
ax[1].set_title('weights matrix (H)')

plt.show()