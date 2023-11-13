import numpy as np
import matplotlib.pyplot as plt

seed = (50,0)
stack = [(seed[0], seed[1]), (seed[0], seed[1])]
dummy = np.zeros((100,100))
dummy[:,:] = -1

phase_map = np.zeros((100, 100))
x = 0
dx = 4 * np.pi / 100
for i in range(100):
    phase_map[:,i] = x
    x += dx
phase_map = phase_map % (2 * np.pi)

# plt.imshow(phase_map, cmap='gray')
# plt.show()

def unwrap(pixel, previous):
    return ((phase_map[pixel] - dummy[previous] + np.pi) % (2 * np.pi)) + dummy[previous] - np.pi

# x = np.unwrap(phase_map)
# plt.imshow(x, cmap='gray')
# plt.show()

while stack:
    x,y = stack[0]
    neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                  if coord[0]<100 and coord[0]>=0 and coord[1]<100 and coord[1]>=0]
    unwrapped = [coord for coord in neighbours if dummy[coord] == -1]

    for pixel in unwrapped:
        dummy[pixel] = unwrap(pixel, stack[0])

        x1,y1 = pixel
        new_neighbours = [coord for coord in [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]
                          if coord[0]<100 and coord[0]>=0 and coord[1]<100 and coord[1]>=0]
        neighbour_wrapped = False
        for coord in new_neighbours:
            if dummy[coord] == -1:
                neighbour_wrapped = True
        if neighbour_wrapped:
            stack.append(pixel)
    stack.pop(0)

plt.imshow(dummy, cmap='gray')
plt.show()