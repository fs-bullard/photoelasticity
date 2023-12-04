import matplotlib.pyplot as plt
import cv2 as cv

filename = 'img/disc/results/disc_isocl_unwr.jpg'
img = cv.medianBlur(cv.imread(filename, cv.IMREAD_GRAYSCALE), 5) 
plt.imshow(img, cmap='RdBu')
plt.imsave('img/disc/results/disc_isocl_unwr_colour.jpg', img, cmap='RdBu')
plt.show()
