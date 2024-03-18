import cv2
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

# [ZAD_1]
img = cv2.imread('image.png')
axes[0].imshow(img)

cv2.imwrite('doggo.png', img)

# [ZAD_2]
img = cv2.cvtColor(cv2.imread('image.png'), cv2.COLOR_BGR2GRAY)
axes[1].hist(img)

plt.show()