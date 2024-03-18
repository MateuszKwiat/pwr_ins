import matplotlib.pyplot as plt
import numpy as np
import cv2

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

# [ZAD_1]
img = cv2.imread('image.png')
axes[0].imshow(img)
axes[0].set_title('Original image')

cv2.imwrite('doggo.png', img)

# [ZAD_2]
# gray_img = cv2.cvtColor(cv2.imread('image.png'), cv2.COLOR_BGR2GRAY)
# axes[1].hist(gray_img)
# print(gray_img)

# [ZAD_3]
(b_img, g_img, r_img) = cv2.split(img)
row_len, col_len = b_img.shape

pixels_number = np.random.randint(10_000, 245_000)
for _ in range(pixels_number):
    x = np.random.randint(0, row_len - 1) 
    y = np.random.randint(0, col_len - 1) 

    b_img[y][x] = 255
    g_img[y][x] = 255
    r_img[y][x] = 255

pixels_number = np.random.randint(10_000, 245_000)
for _ in range(pixels_number):
    x = np.random.randint(0, row_len - 1) 
    y = np.random.randint(0, col_len - 1) 

    b_img[y][x] = 0
    g_img[y][x] = 0
    r_img[y][x] = 0

merged_image = cv2.merge((b_img, g_img, r_img))
axes[1].imshow(merged_image)
axes[1].set_title('Image with \'salt and pepper\' noise')

plt.show()