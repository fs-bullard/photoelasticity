import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pdb
from functions import mask_to_dummy



def phase_unwrap(img: np.ndarray, stack, dummy) -> np.ndarray:
    """
    input stack is list of isotropic points
    """

    def unwrap(pixel, previous) -> float:
        """
        Returns the unwrap phase of pixel given the phase of its neighbour
        """
        scale = 255
        return ((img[pixel] - dummy[previous] + scale/2) % (scale)) + dummy[previous] - scale/2
    
    def get_quality(pixel, neighbours):
        
    
    for seed in stack:
        dummy[seed] = img[seed]
    
    iteration = 0
    while stack:
        x, y = stack[0]
        neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]]
        wrapped = [coord for coord in neighbours if dummy[coord] == np.inf]

        for pixel in wrapped:
            if iteration % 500000 == 0:
                # dummy_dummy = np.copy(dummy)
                # dummy_dummy[dummy_dummy == -np.inf] = 0
                # dummy_dummy[dummy_dummy == np.inf] = 0
                # dummy_dummy = np.nan_to_num(abs(dummy_dummy) / 255)
                # plt.imsave(f'img/disc/results/unwrapping_steps/unwrapping{int(iteration/500000)}.jpg', dummy_dummy, cmap='gray')
                # plt.imshow(dummy_dummy, cmap='gray')
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

    dummy[dummy == -np.inf] = 0
    dummy[dummy == np.inf] = 0
    return abs(dummy) / 255

if __name__ == "__main__":
    # Load img
    filename = 'img/disc/results/disc_isochr_wr_isocl_unwr.jpg'
    img = cv.medianBlur(cv.imread(filename, cv.IMREAD_GRAYSCALE), 5) 
    mask = cv.imread('img/disc/mask/disc_mask_phase_shifting_2.jpg', cv.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap='gray')
    plt.show()

    # Set stack as isotropic points
    stack = [(2000, 2200), (2000, 4200)]
    #create dummy array to be populated by unwrapped pixels
    dummy = mask_to_dummy(mask)


    # Unwrap
    img_unwrapped = phase_unwrap(img, stack, dummy)

    plt.imshow(img_unwrapped, cmap='gray')
    plt.show()