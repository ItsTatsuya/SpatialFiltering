import cv2
import numpy as np

def averageFilter(image, kernelSize):
    # Create a matrix of ones
    kernel = np.ones((kernelSize, kernelSize), np.float32) / (kernelSize * kernelSize)
    # Use the cv2.filter2D function to convolve the kernel with an image
    return cv2.filter2D(image, -1, kernel)
