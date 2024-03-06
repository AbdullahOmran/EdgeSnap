import cv2 as cv
import numpy as np


def gaussian_kernel(size, std):
    kernel = np.fromfunction(
        lambda x, y: (1/(2*np.pi*std**2)) * np.exp(-((x - size//2)**2 + (y - size//2)**2)/(2*std**2)),
        (size, size))
    kernel /= np.sum(kernel)
    return kernel


def apply_median_blur(image, kernel_size):
    height, width = image.shape
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant')
    blurred_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            neighborhood = padded_image[i:i+kernel_size, j:j+kernel_size]
            blurred_image[i, j] = np.median(neighborhood)
    
    return blurred_image.astype(np.uint8)