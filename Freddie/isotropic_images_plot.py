import rawpy
import matplotlib.pyplot as plt
import os
import numpy as np
import cv2 as cv

def load_raw_img(path: str, mask: np.ndarray) -> np.ndarray:
    """
    Returns the raw image at path as ndarray
    Adapted for this use case: 
     - takes only green channel
     - masks and crops
    """
    with rawpy.imread(path) as raw_img:
        img_raw = raw_img.postprocess()

    img_masked = img_raw * mask
    
    # Disc:
    # return img_masked[488:3250, 1838:4569, :]

    # Ring:
    return img_masked[500:2970, 1950:4520, :]


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 10  # Adjust the font size as needed
plt.rcParams['text.usetex'] = True

# Load Disc Mask
# mask = cv.imread("img/disc/mask/disc_mask_phase_shifting_2.jpg") // 255

# Load Ring Mask
mask = cv.imread("img/ring/mask/ring_mask_isotropic.jpg") 
# plt.imshow(mask)
# plt.show()

# Create a subplot with 2 rows and 5 columns
fig, axes = plt.subplots(2, 5, figsize=(6.8, 3.2), dpi=300)

# Flatten the axes array for easier indexing
axes = axes.flatten()

# Disc
# base_path = "img/disc/isotropic/"

# Ring
base_path = "img/ring/isotropic/"
file_type = ".CR2"

# Find files
file_names = os.listdir(base_path)

for i, file_name in enumerate(file_names):
    img = load_raw_img(base_path + file_name, mask // 255)

    axes[i].imshow(img) 
    axes[i].axis('off')  # Turn off axis labels for cleaner visualization
    axes[i].set_title(r'${{{}}}^\circ$'.format(i*10))

# Adjust layout to prevent overlap of titles
plt.tight_layout()

# Save the disc plot
# plt.savefig('report/isotropic_images_disc.png', bbox_inches='tight', dpi=300)

# Save the ring plot
plt.savefig('report/isotropic_images_ring.png', bbox_inches='tight', dpi=300)

plt.show()