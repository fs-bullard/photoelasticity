import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['font.size'] = 10  # Adjust the font size as needed

fig, axes = plt.subplots(2, 2, figsize=(6.8, 5.5), dpi=300)

# Load data
yellow_data = np.loadtxt("report/yellow_data.csv", delimiter=',')
cyan_data = np.loadtxt("report/cyan_data.csv", delimiter=',')
bulb_data = np.loadtxt("report/bulb_data.csv", delimiter=',')
red_data = np.loadtxt("report/red.csv", delimiter=',')
green_data = np.loadtxt("report/green.csv", delimiter=',')
blue_data = np.loadtxt("report/blue.csv", delimiter=',')

# Extract x and y values
x_yellow, yellow = yellow_data[:, 0], yellow_data[:, 1] / 100
x_cyan, cyan = cyan_data[:, 0],  1 - cyan_data[:, 1] / 100
x_bulb, bulb = bulb_data[:, 0], bulb_data[:, 1] / 100
x_red, red = red_data[:, 0], red_data[:, 1] / 4.9
x_green, green = green_data[:, 0], green_data[:, 1] / 4.9
x_blue, blue = blue_data[:, 0], blue_data[:, 1] / 4.9

# Interpolate data
x_combined = np.linspace(min(x_yellow.min(), x_cyan.min(), x_bulb.min(), x_red.min(), x_green.min(), x_blue.min()),
                         max(x_yellow.max(), x_cyan.max(), x_bulb.max(), x_red.max(), x_green.max(), x_blue.max()), 1000)

yellow_interp = np.interp(x_combined, x_yellow, yellow)
cyan_interp = np.interp(x_combined, x_cyan, cyan)
bulb_interp = np.interp(x_combined, x_bulb, bulb)
red_interp = np.interp(x_combined, x_red, red)
green_interp = np.interp(x_combined, x_green, green)
blue_interp = np.interp(x_combined, x_blue, blue)

# Normalize products
product1 = bulb_interp * (red_interp + green_interp + blue_interp)
product1 /= np.max(product1)
product2 = yellow_interp * cyan_interp * bulb_interp * green_interp
product2 /= np.max(product2)

# Find the peak wavelength of the monochromatic light
peak_wavelength = x_combined[np.argmax(product2)]
arr = np.where(np.isclose(product2, 0.5, 0.01))[0]
fwhm = arr[1] - arr[0]
std = fwhm / 2.355

normal_dist = norm.pdf(x_combined, peak_wavelength, std)
print(peak_wavelength, fwhm, std)

# Plot RGB Spectra
axes[0, 0].plot(x_red, red, label='Red', color='red', linestyle='-', linewidth=1)
axes[0, 0].plot(x_green, green, label='Green', color='green', linestyle='-', linewidth=1)
axes[0, 0].plot(x_blue, blue, label='Blue', color='blue', linestyle='-', linewidth=1)
axes[0, 0].set_ylim(-0.05, 1.05)
axes[0, 0].set_xlabel('Wavelength / nm')
axes[0, 0].set_ylabel('Relative spectral response')
axes[0, 0].legend()
axes[0, 0].text(0.05, 0.9, 'a)', transform=axes[0, 0].transAxes, fontweight='bold')

# Plot individual components in gray with different line styles
axes[0, 1].plot(x_bulb, bulb, label='Bulb', color='black', linestyle='-', linewidth=1)
axes[0, 1].set_xlabel('Wavelength / nm')
axes[0, 1].set_ylabel('Relative spectral content')
axes[0, 1].set_ylim(-0.05, 1.05)
# axes[0, 1].legend()
axes[0, 1].text(0.05, 0.9, 'b)', transform=axes[0, 1].transAxes, fontweight='bold')

# Plot individual components in gray with different line styles
axes[1, 0].plot(x_yellow, yellow, label='Yellow', color='gold', linestyle='-', linewidth=1)
axes[1, 0].plot(x_cyan, cyan, label='Cyan', color='cyan', linestyle='-', linewidth=1)
axes[1, 0].set_xlabel('Wavelength / nm')
axes[1, 0].set_ylabel('Transmission')
axes[1, 0].set_ylim(-0.05, 1.05)
axes[1, 0].legend(loc='center right')
axes[1, 0].text(0.05, 0.9, 'c)', transform=axes[1, 0].transAxes, fontweight='bold')

# Plot normalized products with different colors
axes[1, 1].plot(x_combined, product2, label='Monochromatic', color='orange', linestyle='-', linewidth=1)
axes[1, 1].plot(x_combined, product1, label='Colour', color='purple', linestyle='-', linewidth=1)
axes[1, 1].vlines(peak_wavelength, -0.5, 1, colors=['gray'], linestyles='dotted')
# axes[1, 1].set_xticks([350, 450, int(peak_wavelength), 650, 750, 850, 950])
# axes[1, 1].plot(x_combined, normal_dist / np.max(normal_dist), color='gray', linewidth=1)
axes[1, 1].set_xlabel('Wavelength / nm')
axes[1, 1].set_ylabel('Relative spectral content')
axes[1, 1].set_ylim(-0.05, 1.05)
axes[1, 1].legend(loc='center right')
axes[1, 1].text(0.05, 0.9, 'd)', transform=axes[1, 1].transAxes, fontweight='bold') 

plt.tight_layout()
plt.savefig('report/spectra.jpg', bbox_inches='tight', dpi=300)
plt.show()
