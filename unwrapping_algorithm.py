import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pdb
from functions import mask_circ_img


# seed = (50,0)
# stack = [(seed[0], seed[1]), (seed[0], seed[1])]
# dummy = np.zeros((100,100))
# dummy[:,:] = -1
        

# phase_map = np.zeros((100, 100))
# x = 0
# dx = 4 * np.pi / 100
# for i in range(100):
#     phase_map[:,i] = x
#     x += dx
# phase_map = phase_map % (2 * np.pi)

# # plt.imshow(phase_map, cmap='gray')
# # plt.show()

# def unwrap(pixel, previous):
#     return ((phase_map[pixel] - dummy[previous] + np.pi) % (2 * np.pi)) + dummy[previous] - np.pi

# # x = np.unwrap(phase_map)
# # plt.imshow(x, cmap='gray')
# # plt.show()

# while stack:
#     x,y = stack[0]
#     neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
#                   if coord[0]<100 and coord[0]>=0 and coord[1]<100 and coord[1]>=0]
#     wrapped = [coord for coord in neighbours if dummy[coord] == -1]

#     for pixel in wrapped:
#         dummy[pixel] = unwrap(pixel, stack[0])

#         x1,y1 = pixel
#         new_neighbours = [coord for coord in [(x1-1,y1),(x1+1,y1),(x1,y1-1),(x1,y1+1)]
#                           if coord[0]<100 and coord[0]>=0 and coord[1]<100 and coord[1]>=0]
#         neighbour_wrapped = False
#         for coord in new_neighbours:
#             if dummy[coord] == -1:
#                 neighbour_wrapped = True
#         if neighbour_wrapped:
#             stack.append(pixel)
#     stack.pop(0)

# plt.imshow(dummy, cmap='gray')
# plt.show()



def phase_unwrap(img: np.ndarray, stack, center, radius) -> np.ndarray:
    """
    input stack is list of isotropic points
    """

    dummy = np.zeros(img.shape)

    dummy[:,:] = -2

    # Need to change if shape not circle
    # -2 outside the mask, -1 inside the mask
    cv.circle(dummy, center, radius, np.inf, -1)

    # print(dummy[1500, 3000])

    def unwrap(pixel, previous) -> float:
        """
        Returns the unwrap phase of pixel given the phase of its neighbour
        """
        scale = 127.5
        # import pdb
        # pdb.set_trace()
        return ((img[pixel] - dummy[previous] + scale) % (2*scale)) + dummy[previous] - scale
    
    for seed in stack:
        dummy[seed] = img[seed]
    print(img[stack[0]], img[stack[1]])

    
    iteration = 0
    while stack:
        x, y = stack[0]
        neighbours = [coord for coord in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]]
        wrapped = [coord for coord in neighbours if dummy[coord] == np.inf]
        # pdb.set_trace()
        # print(wrapped)

        for pixel in wrapped:
            if iteration % 300000 == 0:
                plt.imshow(dummy, cmap='gray')
                plt.show()
                print(iteration, len(stack))
            if iteration > 3500000:
                pdb.set_trace()
                print(stack)
                stack = [1]
                break

            dummy[pixel] = unwrap(pixel, stack[0])
            iteration += 1
            # print(dummy[pixel])
            

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
    # import pdb
    # pdb.set_trace()
    r = 1050
    center = (3030, 1770)
    # r = 250
    # center = (335, 335)
    plt.imshow(mask_circ_img(img, center, r), cmap='gray')
    plt.show()
    # Set stack as isotropic points
    stack = [(center[1], center[0] - r), (center[1], center[0] + r)]

    img_unwrapped = phase_unwrap(img, stack, center, r)
    # img_unwrapped = np.unwrap(mask_circ_img(img, center, r), period=255)

    plt.imshow(img_unwrapped, cmap='gray')
    plt.show()