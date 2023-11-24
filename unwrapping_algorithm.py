import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pdb
from functions import mask_circ_img


def phase_unwrap(img: np.ndarray, stack, centre, radius, dummy) -> np.ndarray:
    """
    input stack is list of isotropic points
    """

    def unwrap(pixel, previous) -> float:
        """
        Returns the unwrap phase of pixel given the phase of its neighbour
        """
        scale = 255
        return ((img[pixel] - dummy[previous] + scale/2) % (scale)) + dummy[previous] - scale/2
    
    for seed in stack:
        dummy[seed] = img[seed]
    print(img[stack[0]], img[stack[1]])
    
    iteration = 0
    while stack:
        x, y = stack[0]
        neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]]
        wrapped = [coord for coord in neighbours if dummy[coord] == np.inf]

        for pixel in wrapped:
            if iteration % 300000 == 0:
                # plt.imshow(dummy, cmap='gray')
                # plt.show()
                print(iteration, len(stack))
            # if iteration > 3500000:
            #     print(stack)
            #     return abs(dummy)/ 255

            dummy[pixel] = unwrap(pixel, stack[0])
            iteration += 1            

            x1, y1 = pixel
            new_neighbours = [coord for coord in [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]]
            neighbour_wrapped = False
            for coord in new_neighbours:
                if dummy[coord] == np.inf:
                    neighbour_wrapped = True
            if neighbour_wrapped:
                stack.append(pixel)
        stack.pop(0)

    return abs(dummy)/ 255

if __name__ == "__main__":
    # Load img
    filename = 'isochromatic_processed.jpg'
    img = cv.medianBlur(cv.imread(filename, cv.IMREAD_GRAYSCALE), 5) 
    r = 1050
    centre = (3030, 1770)
    plt.imshow(mask_circ_img(img, centre, r), cmap='gray')
    plt.show()

    # Set stack as isotropic points
    stack = [(centre[1], centre[0] - r), (centre[1], centre[0] + r)]

    #create dummy array to be populated by unwrapped pixels
    dummy = np.zeros(img.shape)
    dummy[:,:] = None
    # None outside the mask, np.inf inside the mask
    cv.circle(dummy, centre, r, np.inf, -1)

    img_unwrapped = phase_unwrap(img, stack, centre, r, dummy)
    # img_unwrapped = np.unwrap(mask_circ_img(img, centre, r), period=255)

    plt.imshow(img_unwrapped, cmap='gray')
    plt.show()