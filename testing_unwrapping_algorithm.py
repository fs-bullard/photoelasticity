import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pdb

def phase_unwrap(img: np.ndarray, stack, center, radius) -> np.ndarray:
    """
    input stack is list of isotropic points
    """

    dummy = np.zeros(img.shape)

    dummy[:,:] = -2

    # Need to change if shape not circle
    # -2 outside the mask, -1 inside the mask
    cv.circle(dummy, center, radius, -1, -1)

    def unwrap(pixel, previous) -> float:
        """
        Returns the unwrap phase of pixel given the phase of its neighbour
        """
        return round(
            ((round(img[pixel],5) - round(dummy[previous],5) + np.pi) % (2 * np.pi))
            + dummy[previous] - np.pi, 5)

    while stack:
        x, y = stack[0]
        neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]]
        unwrapped = [coord for coord in neighbours if dummy[coord] == -1]

        for pixel in unwrapped:
            dummy[pixel] = unwrap(pixel, stack[0])            

            x1, y1 = pixel
            new_neighbours = [coord for coord in [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]]
            neighbour_wrapped = False
            for coord in new_neighbours:
                if dummy[coord] == -1:
                    neighbour_wrapped = True
            if neighbour_wrapped:
                stack.append(pixel)
            
            # import pdb
            # pdb.set_trace()
        
        stack.pop(0)

    return dummy

if __name__ == "__main__":
    phase_map = np.zeros((1000, 1000))
    x = 0
    dx = 4 * np.pi / 200
    for i in range(1000):
        phase_map[:,i] = x
        x += dx
    phase_map = phase_map % (2 * np.pi)

    plt.imshow(phase_map,cmap='gray')
    plt.show()
    
    stack = [(100, 500), (900, 500)]

    img_unwrapped = phase_unwrap(phase_map, stack, (500,500), 400)
    # img_unwrapped = np.unwrap(img)

    plt.imshow(img_unwrapped, cmap='gray')
    plt.show()