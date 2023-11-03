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