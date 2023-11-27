import cv2 as cv
import numpy as np
import rawpy
import matplotlib.pyplot as plt

def load_raw_img(path: str) -> np.ndarray:
    """
    Returns the raw image at path as ndarray
    """
    with rawpy.imread(path) as raw_img:
        rgb_img = raw_img.postprocess()
    
    return rgb_img

def rad_to_deg(a):
    return 180*a/np.pi

def mask_circ_img(img: np.ndarray, center: (int, int), radius: int) -> np.ndarray:
    mask = np.zeros(img.shape, dtype=img.dtype)
    mask = cv.circle(mask, center, radius, 255, -1)

    return cv.bitwise_and(img, mask)     

def mask_to_dummy(mask: np.ndarray) -> np.ndarray:
    """
    Returns array of nan inside the ROI, and np.inf outside the mask
    """
    return ((mask // 255)) * np.inf



if __name__ == "__main__":
    print("Running test mask...")
    # img = cv.imread("isochromatic.jpg")
    # img_masked = mask_circ_img(img, (3030, 1770), 1050)

    # plt.imshow(img_masked, cmap='gray')
    # plt.show()

    plt.imshow(cv.imread('img/results/ring_isochr_wr.jpg'), cmap='gray')
    plt.show()