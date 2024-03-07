import numpy as np
import cv2

def addGaussianNoise(image, mean, sigma):
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    # Clip pixel values to [0, 255]
    noisy = np.clip(noisy, 0, 255)
    noisy = noisy.astype(np.uint8)
    return noisy