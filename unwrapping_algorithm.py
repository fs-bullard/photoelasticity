import numpy as np

radius = 1500
centre = (3000,2000)
stack = [(centre[0]-radius, centre[1]), (centre[0]+radius, centre[1])]
dummy = np.zeroes(6000,4000)
phase_map = np.zeroes(6000, 4000)

def unwrap(pixel, previous):
    return ((phase_map[pixel] - dummy[previous] + np.pi) % (2 * np.pi)) + dummy[previous] - np.pi

while stack:
    x,y = stack[0]
    unwrapped = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if dummy[coord] == -1]
    for pixel in unwrapped:
        dummy[pixel] = unwrap(pixel, stack[0])
        x1,y1 = pixel
        for coord in [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]:
            if dummy[coord] == -1:
                stack.append(coord)
    stack.pop(0)