import matplotlib.pyplot as plt
from matplotlib import patches, gridspec
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2 as cv

# Set font and font size
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 10  # Adjust the font size as needed

# Define threshold for cropping
threshold = 1

# Load the grayscale image
unwrapped_disc = np.load('img/disc/results/disc_isochr_wr_isocl_unwr.npy')
grayscale_image = np.load('img/disc/results/disc_isochr_unwr_isocl_unwr.npy')

# Find indices of pixels above threshold
y_indices, x_indices = np.where(grayscale_image > threshold)

# Crop the grayscale image
cropped_image = grayscale_image[460:3250, 1810:4610]
cropped_unwr = unwrapped_disc[460:3250, 1810:4610]

# Create the x and y coordinates for the cropped image
x, y = np.mgrid[0:cropped_image.shape[0], 0:cropped_image.shape[1]]

# Create the plot
fig = plt.figure(figsize=(8, 3))
gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1.05, 0.05])

# Plot the 2D line plot
ax2 = fig.add_subplot(gs[0])
ax2.plot(cropped_image[1395, 100:-100], label='Unwrapped', color='red')
ax2.plot(cropped_unwr[1395, 100:-100], label='Wrapped', color='darkblue')
ax2.set_xlabel('X')
ax2.set_ylabel('Fringe Order')
ax2.legend(loc='upper left')

# Plot the 3D surface
ax = fig.add_subplot(gs[1], projection='3d')
surf = ax.plot_surface(x, y, cropped_image, rstride=10, cstride=10, cmap='jet', antialiased=False)
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Plot the colorbar
cb_ax = fig.add_subplot(gs[2])
cb = fig.colorbar(surf, cax=cb_ax, label='Fringe Order', orientation='vertical')
cb.ax.yaxis.set_ticks_position('left')
cb.ax.yaxis.set_label_position('left')

# Adjust layout
plt.tight_layout()

# Save or display the plot
plt.savefig('report/3d_plot_disc.png', bbox_inches='tight', dpi=600)
plt.show()
