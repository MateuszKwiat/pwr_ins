import cv2
import matplotlib.pyplot as plt

#[ZAD_1]
img = cv2.imread('image.png')
plt.imshow(img)
plt.show()

cv2.imwrite('doggo.png', img)