import matplotlib.pyplot as plt
import cv2 as cv

fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(20,12))

col = 0
row = 0
for i in range(1,13):
    img = cv.imread(f"img/disc/results/unwrapping_steps/unwrapping{i}.jpg", cv.IMREAD_GRAYSCALE)
    axes[row][col].imshow(img, cmap='turbo')
    axes[row][col].axis('off')
    col += 1
    if col % 4 == 0:
        col = 0
        row += 1

fig.subplots_adjust(wspace=0.1, hspace=0)

plt.show()