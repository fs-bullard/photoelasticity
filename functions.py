import cv2 as cv
import numpy as np
import rawpy

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