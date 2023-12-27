import matplotlib.pyplot as plt
import cv2 as cv
from matplotlib import gridspec
import numpy as np

# Set font and font size
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 10  # Adjust the font size as needed
plt.rcParams['text.usetex'] = True

# Function to display images in a grid
def display_images(image_paths, row_labels, col_labels):

    num_rows = len(row_labels)
    num_cols = len(col_labels)

    # Adjust the figure size to fit two columns in portrait A4
    fig = plt.figure(figsize=(7.5, 4), dpi=300)
    gs = gridspec.GridSpec(num_rows + 1, num_cols, height_ratios=[1, 1, 0.05], wspace=0.2, hspace=0.15)  # Add an extra row for colorbars

    axs = []
    for i in range(num_rows):
        axs_row = []
        for j in range(num_cols):
            axs_row.append(plt.subplot(gs[i, j]))
            img = cv.imread(image_paths[i][j], cv.IMREAD_GRAYSCALE)
            if j == 3:
                cmap = 'jet'
            else:
                cmap = 'gray'
            im = axs_row[-1].imshow(img, cmap=cmap)  # Using 'gray' colormap
            axs_row[-1].axis('off')
            
            # Add labels to the first row and first column
            if i == 0:
                axs_row[-1].set_title(col_labels[j], fontsize=10)
            if j == 0:
                axs_row[-1].text(-0.1, 0.5, row_labels[i], va='center', ha='right', rotation='horizontal', transform=axs_row[-1].transAxes)

            cbar_ax = plt.subplot(gs[-1, j])
            cbar = plt.colorbar(im, cax=cbar_ax, orientation='horizontal', cmap=cmap)
            cbar.set_ticks(ticks=[0, 127.5, 255], labels=colorbar_ranges[j], fontsize=8)

        axs.append(axs_row)

    plt.tight_layout()
    
    # Save the figure with a specific file name
    plt.savefig('report/ten-step-results.png', bbox_inches='tight', dpi=300)
    
    plt.show()

# Replace these paths with the actual paths to your images
disc_images = ["report/disc/report_disc_isoclinic_wrapped.jpg", "report/disc/report_disc_isoclinic.jpg", "report/disc/report_disc_isochromatic.jpg", "report/disc/report_disc_stress_map.jpg"]
ring_images = ["report/ring/report_ring_isoclinic_wrapped.jpg", "report/ring/report_ring_isoclinic.jpg", "report/ring/report_ring_isochromatic.jpg", "report/ring/report_ring_stress_map.jpg"]

image_paths = [disc_images, ring_images]
row_labels = ['Disc', 'Ring']
col_labels = ['Wrapped \n Isoclinic Parameter \n' + r'$\theta$', 'Unwrapped \n Isoclinic Parameter \n' + r'$\theta_\mathrm{unwrapped}$', 'Isochromatic \n Parameter \n' + r'$\delta$', 'Stress Map \n (MPa) \n' + r'$\sigma_1 - \sigma_2$']

# Determine the max stress for the disc and ring
disc_fringe = np.load('img/disc/results/disc_isochr_unwr_isocl_unwr.npy')
ring_fringe = np.load('img/ring/results/ring_isochr_unwr_isocl_unwr.npy')

max_stress = np.max(disc_fringe) * 38200 / 0.012 / 1000000

# Set custom colorbar range for each column
colorbar_ranges = [[r'$-\pi/4$', '0', r'$\pi/4$'], [r'$-\pi/2$', '0', r'$\pi/2$'], ['0', r'$\pi$', r'$2\pi$'], ['0', '16', '32']]  # Adjust the range as needed



# Display the images in a grid with colorbars
display_images(image_paths, row_labels, col_labels)
