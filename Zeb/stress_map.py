import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

arr = np.load('img/disc/results/disc_isochr_unwr_isocl_unwr.npy')

Fsig = 38200
thickness = 0.012
stress = (arr * Fsig) / thickness / 1000000

mpl.rcParams["font.size"] = 16
fig, ax = plt.subplots(figsize=(8,8))
ax.axis('off')
img = ax.imshow(stress, cmap='turbo')

divider = make_axes_locatable(ax)
cax = divider.append_axes("bottom", size="5%", pad=0.2)
cb = plt.colorbar(img, orientation="horizontal", cax=cax)
cb.set_label('Principle Stress Difference [$MPa$]')
cb.ax.locator_params(nbins=4)
print(np.max(stress))
plt.show()