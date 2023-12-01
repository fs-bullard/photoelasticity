import matplotlib.pyplot as plt
import cv2 as cv

filename = 'img/ring/results/ring_isochr_unwr_isoc_unwr.jpg'
img = cv.medianBlur(cv.imread(filename, cv.IMREAD_GRAYSCALE), 5) 
plt.imshow(img, cmap='gray')
plt.show()
