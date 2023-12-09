import matplotlib.pyplot as plt
import os
import rawpy

fig, ax = plt.subplots(figsize=(8,8))

# filename = "img/disc/phase-shifting/IMG_3940.CR2"
filename = "img/ring/phase-shifting/IMG_3836.CR2"

# isotropes = [(3200-1356, 1876), (3200+1356, 1876)]
isotropes = [(1650, 2030), (1700, 3970), (2200, 2650), (2150,3400), (2570, 2150), (2460, 3950), (1130, 2600), (1150, 3400), (800, 2080), (700, 3850)]

with rawpy.imread(filename) as raw_img:
    img = raw_img.postprocess()
    ax.axis('off')
    ax.imshow(img)
for i in isotropes:
    ax.plot(i[1], i[0], "or", markersize=8)

fig.subplots_adjust(wspace=0.1, hspace=0)

plt.show()