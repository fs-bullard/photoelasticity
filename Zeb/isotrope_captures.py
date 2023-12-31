import matplotlib.pyplot as plt
import os
import rawpy

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(25,8))

base_path = "img/ring/isotropic/"

file_names = os.listdir(base_path)

#isotropes = [(1800, 1900), (4700, 1900)]
isotropes = [(1650, 2030), (1700, 3970), (2200, 2650), (2150,3400), (2570, 2150), (2460, 3950), (1130, 2600), (1150, 3400), (800, 2080), (700, 3850)]


col = 0
row = 0
for file_name in file_names:
    with rawpy.imread(base_path + file_name) as raw_img:
        img = raw_img.postprocess()
    axes[row][col].imshow(img)
    axes[row][col].axis('off')
    for i in isotropes:
        axes[row][col].plot(i[1], i[0], "or", markersize=8)
    col += 1
    if col % 5 == 0:
        col = 0
        row += 1

fig.subplots_adjust(wspace=0.1, hspace=0)

plt.show()