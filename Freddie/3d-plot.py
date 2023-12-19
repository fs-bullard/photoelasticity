import matplotlib.pyplot as plt
from matplotlib import patches
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
grayscale_image = np.load('img/disc/results/disc_isochr_unwr_isocl_unwr.npy')
# plt.imshow(grayscale_image)
# plt.show()
# Find indices of pixels above threshold
y_indices, x_indices = np.where(grayscale_image > threshold)

# Crop the grayscale image
cropped_image = grayscale_image[460:3250, 1810:4610]

# Create the x and y coordinates for the cropped image


# Create the z coordinates
# z = cv.resize(cropped_image, (200, 200))
z = cropped_image

x, y = np.mgrid[0:z.shape[0], 0:z.shape[1]]

# Create the plot
fig = plt.figure(figsize=(8, 3.3))
ax = fig.add_subplot(121, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap='jet', antialiased=False)

# Set the view angle
# ax.view_init(elev=15, azim=-60)

# Hide axis labels and ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
ax.set_zlabel('Fringe Order')

# Set the colorbar
# fig.colorbar(surf, label='Fringe order', location='bottom', fraction=0.046, pad=0.06)

ax2 = fig.add_subplot(122)

im = ax2.imshow(cropped_image, cmap='jet')

# centre box: (1870, 3195) -> (1880, 3205)

rect = patches.Rectangle((1870 - 480, 3195 -1780), 10, 10, linewidth=1, edgecolor='w', facecolor='none')

ax2.add_patch(rect)

# Draw lines connecting corners of the rectangle to the corners of the zoomed-in square
rect_coords = rect.get_bbox().get_points()
zoomed_coords = np.array([[rect_coords[0, 0], rect_coords[0, 1]],
                          [rect_coords[1, 0], rect_coords[0, 1]],
                          [rect_coords[1, 0], rect_coords[1, 1]],
                          [rect_coords[0, 0], rect_coords[1, 1]],
                          [rect_coords[0, 0], rect_coords[0, 1]]])

ax2.plot(zoomed_coords[:, 0], zoomed_coords[:, 1], color='w')

fig.colorbar(im, label='Fringe order', fraction=0.046)


# Show the plot
plt.tight_layout()

plt.savefig('report/3d_plot_disc.png', bbox_inches='tight', dpi=300)
plt.show()
