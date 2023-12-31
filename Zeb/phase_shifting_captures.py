import matplotlib.pyplot as plt
import os
import rawpy

fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(25,8))

base_path = "img/disc/phase-shifting/"
file_names = os.listdir(base_path)

col = 0
row = 0
for file_name in file_names:
    with rawpy.imread(base_path + file_name) as raw_img:
        img = raw_img.postprocess()
    axes[row][col].imshow(img)
    axes[row][col].axis('off')
    col += 1
    if col % 5 == 0:
        col = 0
        row += 1

fig.subplots_adjust(wspace=0.1, hspace=0)

plt.show()