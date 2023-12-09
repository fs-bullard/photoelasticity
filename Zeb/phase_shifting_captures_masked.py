import matplotlib.pyplot as plt
import os
import rawpy
import cv2 as cv
import numpy as np

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(25,8))

mask = cv.imread('img/ring/mask/ring_mask_phase_shifting.jpg', cv.IMREAD_GRAYSCALE)
c_mask = np.zeros((4022,6024,3))
for i in range(3):
    c_mask[:,:,i] = mask

base_path = "img/ring/phase-shifting/"
file_names = os.listdir(base_path)

col = 0
row = 0
for file_name in file_names:
    with rawpy.imread(base_path + file_name) as raw_img:
        img = cv.multiply(raw_img.postprocess().astype(float), c_mask / 255) / 255
    axes[row][col].imshow(img)
    axes[row][col].axis('off')
    col += 1
    if col % 5 == 0:
        col = 0
        row += 1

fig.subplots_adjust(wspace=0.1, hspace=0)

plt.show()