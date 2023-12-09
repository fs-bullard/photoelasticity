import matplotlib.pyplot as plt
import os
import rawpy

fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(25,4))

base_path = "img/ring/ml/"

file_names = os.listdir(base_path)

col = 0
for file_name in file_names:
    with rawpy.imread(base_path + file_name) as raw_img:
        img = raw_img.postprocess()
    axes[col].imshow(img)
    axes[col].axis('off')
    col += 1

fig.subplots_adjust(wspace=0.1)

plt.show()