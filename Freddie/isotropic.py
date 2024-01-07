import matplotlib.pyplot as plt
import numpy as np

# Set font and font size
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 10  # Adjust the font size as needed

# Create some example images (replace this with your actual image data)
image1 = plt.imread('report/disc/isotropic.png')
image2 = plt.imread('report/ring/isotropic.png')

# Create a figure with figsize (8, 3)
fig, ax = plt.subplots(1, 2, figsize=(7, 3))

# Plot the first image
ax[0].imshow(image1)
ax[0].set_title('Disc')
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_xticklabels([])
ax[0].set_yticklabels([])

# Plot the second image
ax[1].imshow(image2)
ax[1].set_title('Ring')
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[1].set_xticklabels([])
ax[1].set_yticklabels([])

# Adjust layout to prevent clipping of titles
plt.tight_layout()

# Save the figure
plt.savefig('report/isotropic_points.png', bbox_inches='tight', dpi=300)

# Display the figure (optional)
plt.show()
