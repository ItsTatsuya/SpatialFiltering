import cv2
import numpy as np

def gaussianFilter(image, kernelSize):
    kernel = cv2.getGaussianKernel(kernelSize, 0)
    kernel = np.dot(kernel, kernel.T)
    filtered = cv2.filter2D(image, -1, kernel)
    return filtered