import cv2 as cv
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

mpl.rcParams["font.size"] = 16
fig, ax = plt.subplots(figsize=(8,8))
ax.axis('off')
img = cv.imread('img/ring/results/ring_isocl_wr_masked.jpg', cv.IMREAD_GRAYSCALE)
arr = ax.imshow(img, cmap='gray')
plt.gcf().set_tight_layout(True) # To prevent the xlabel being cut off

divider = make_axes_locatable(ax)
cax = divider.append_axes("bottom", size="5%", pad=0.2)
cb = plt.colorbar(arr, orientation="horizontal", cax=cax)
cb.set_label('Isoclinic Parameter [$Radians$]')
cb.set_ticks(ticks=[0, 127.5, 255], labels=[r'$\frac{-\pi}{4}$', '0', r'$\frac{\pi}{4}$'])

plt.show()