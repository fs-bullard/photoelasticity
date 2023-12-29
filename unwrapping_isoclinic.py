import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from functions import mask_to_dummy

def phase_unwrap_isoclinic(img: np.ndarray, queue, result) -> np.ndarray:
    """
    input queue is list of isotropic points
    """

    def unwrap(pixel, previous) -> float:
        """
        Returns the unwrap phase of pixel given the phase of its neighbour
        """
        scale = 255
        return ((img[pixel] - result[previous] + scale/2) % (scale)) + result[previous] - scale/2
    
    
    for seed in queue:
        result[seed] = img[seed]
    
    iteration = 0
    while queue:
        x, y = queue.pop(0)
        neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]]
        wrapped = [coord for coord in neighbours if result[coord] == np.inf]
        
        for pixel in wrapped:
            if iteration % 500000 == 0:
                print(iteration, len(queue))


            result[pixel] = unwrap(pixel, (x, y))
            iteration += 1            

            queue.append(pixel)

    result[result == -np.inf] = 255
    result[result == np.inf] = 255
    return ((((result / 255) + 0.5) % 2) - 1) * (np.pi/2)
    # return ((result / 255) % 2 - 0.5) * (np.pi/2)


if __name__ == "__main__":
    # Load img
    filename = 'img/disc/results/disc_isocl_wr.jpg'
    img = cv.medianBlur(cv.imread(filename, cv.IMREAD_GRAYSCALE), 5) 
    mask = cv.imread('img/disc/mask/disc_mask_phase_shifting_2.jpg', cv.IMREAD_GRAYSCALE)

    # plt.imshow(img, cmap='gray')
    # plt.show()

    # Set queue as isotropic points
    queue = [(2700, 3700), (2700, 2700), (900, 2700), (900, 3000), (900, 3300), (900, 3600)]
    #create result array to be populated by unwrapped pixels
    result = mask_to_dummy(mask)

    img_unwrapped = phase_unwrap_isoclinic(img, queue, result)

    plt.imshow(img_unwrapped, cmap='gray')
    plt.show()