import matplotlib.pyplot as plt
import cv2 as cv

fig, ax = plt.subplots(figsize=(8,8))
ax.axis('off')

filename = 'img/ring/results/ring_isochr_wr_masked.jpg'
img = cv.medianBlur(cv.imread(filename, cv.IMREAD_GRAYSCALE), 5) 
ax.imshow(img, cmap='gray')
plt.show()
