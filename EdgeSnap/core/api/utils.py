import cv2 as cv
import numpy as np


def gaussian_kernel(size, std):
    kernel = np.fromfunction(
        lambda x, y: (1/(2*np.pi*std**2)) * np.exp(-((x - size//2)**2 + (y - size//2)**2)/(2*std**2)),
        (size, size))
    kernel /= np.sum(kernel)
    return kernel
