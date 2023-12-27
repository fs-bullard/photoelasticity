import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from skimage.restoration import unwrap_phase

im = (cv.medianBlur(cv.imread("report/disc/report_disc_isochromatic.jpg", cv.IMREAD_GRAYSCALE), 5) * 2 - 1) * np.pi / 255 

img_unwrapped = unwrap_phase(im, True, True)

plt.imshow(img_unwrapped, cmap='gray')
plt.show()