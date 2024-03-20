import matplotlib.pyplot as plt
import numpy as np
import cv2

# [ZAD_1]
img = cv2.imread('image.png')
plt.imshow(img)
plt.title('Original image')
plt.axis('off')

cv2.imwrite('doggo.png', img)

plt.show()

# [ZAD_2]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
axes[0, 0].hist(img.ravel(), bins=50, color='orange')
axes[0, 0].set_title('original image hist')

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
axes[0, 1].imshow(merged_image)
axes[0, 1].set_title('Image with \'salt and\n pepper\' noise')
axes[0, 1].axis('off')

# [ZAD_4]
# clockwise 90deg rotation
(b_img, g_img, r_img) = cv2.split(img)
b_rotated_img = np.array(list(zip(*b_img[::-1])))
g_rotated_img = np.array(list(zip(*g_img[::-1])))
r_rotated_img = np.array(list(zip(*r_img[::-1])))

rotated_img = cv2.merge((b_rotated_img, g_rotated_img, r_rotated_img))
axes[1, 0].imshow(rotated_img)
axes[1, 0].set_title('90deg clockwise image rotation')
axes[1, 0].axis('off')

# counter-clockwise 90deg rotation
(b_img, g_img, r_img) = cv2.split(img)
b_rotated_img = np.array(list(zip(*[i[::-1] for i in b_img])))
g_rotated_img = np.array(list(zip(*[i[::-1] for i in g_img])))
r_rotated_img = np.array(list(zip(*[i[::-1] for i in r_img])))

rotated_img = cv2.merge((b_rotated_img, g_rotated_img, r_rotated_img))
axes[1, 1].imshow(rotated_img)
axes[1, 1].set_title('90deg counter-clockwise\n image rotation')
axes[1, 1].axis('off')

plt.show()

# [ZAD_5]
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))

poisson_noise = np.clip(np.random.poisson(127, img.shape).astype('int'), 0, 255)

axes[0, 0].imshow(poisson_noise)
axes[0, 0].set_title('Poisson noise')
axes[0, 0].axis('off')

axes[1, 0].hist(poisson_noise.ravel(), bins=50, color='orange')
axes[1, 0].set_title('Poison noise hist')

# # Rayleigh noise
rayleigh_noise = np.clip(np.random.rayleigh(127, img.shape).astype('int'), 0, 255)

axes[0, 1].imshow(rayleigh_noise)
axes[0, 1].set_title('Rayleigh noise')
axes[0, 1].axis('off')

axes[1, 1].hist(rayleigh_noise.ravel(), bins=50, color='orange')
axes[1, 1].set_title('Rayleigh noise hist')

# # Rician noise
rician_noise = np.clip(np.random.normal(50, 100, img.shape).astype('int'), 0, 255)

axes[0, 2].imshow(rician_noise)
axes[0, 2].set_title('Rician noise')
axes[0, 2].axis('off')

axes[1, 2].hist(rician_noise.ravel(), bins=50, color='orange')
axes[1, 2].set_title('Rician noise hist')

plt.show()
    