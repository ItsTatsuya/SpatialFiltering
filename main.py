from GaussianNoise import addGaussianNoise
from averageFilter import averageFilter
from gaussianFilter import gaussianFilter
import laplacianFilter
from PSNR import calcPSNR

import cv2
import numpy as np


# Original Image
image = cv2.imread('./image.png')
cv2.imshow('Original Image', image)


# Gaussian Noised Image
noisy = addGaussianNoise(image, 0, 25)
cv2.imshow('Gaussian Noise', noisy)

print("PSNR value for Gaussian Noise:", cv2.PSNR(image, noisy))

cv2.waitKey(0)
cv2.destroyAllWindows()

kernelSize = [3, 5, 7, 9, 11, 13, 15]

# Averaging Filter
print ("\nAveraging Filter")
for size in kernelSize:
    filtered = averageFilter(noisy, size)
    cv2.imshow(f'Averaging Filter | Size: {size}', filtered)
    print("PSNR value for Averaging Filter [",size,"]:", calcPSNR(image, filtered))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# Gaussian Filter
print ("\nGaussian Filter")
for size in kernelSize:
    filtered = gaussianFilter(noisy, size)
    cv2.imshow(f'Gaussian Filter | Size: {size}', filtered)
    print("PSNR value for Gaussian Filter [",size,"]:", calcPSNR(image, filtered))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# Laplacian Filter
print ("\nLaplacian Filter")
filtered = laplacianFilter.laplacianFilter1(noisy)
cv2.imshow('Laplacian Filter 1', filtered)
cv2.imshow('Discontinuity Map', laplacianFilter.discontinuityMap(noisy))
print("PSNR value for Laplacian Filter 1:", calcPSNR(image, filtered))
cv2.waitKey(0)
cv2.destroyAllWindows()

filtered = laplacianFilter.laplacianFilter2(noisy)
cv2.imshow('Laplacian Filter 2', filtered)
cv2.imshow('Discontinuity Map', laplacianFilter.discontinuityMap(noisy))
print("PSNR value for Laplacian Filter 2:", calcPSNR(image, filtered))
cv2.waitKey(0)
cv2.destroyAllWindows()

filtered = laplacianFilter.laplacianFilter3(noisy)
cv2.imshow('Laplacian Filter 3', filtered)
print("PSNR value for Laplacian Filter 3:", calcPSNR(image, filtered))
cv2.imshow('Discontinuity Map', laplacianFilter.discontinuityMap(noisy))
cv2.waitKey(0)
cv2.destroyAllWindows()

filtered = laplacianFilter.laplacianFilter4(noisy)
cv2.imshow('Laplacian Filter 4', filtered)
print("PSNR value for Laplacian Filter 4:", calcPSNR(image, filtered))
cv2.imshow('Discontinuity Map', laplacianFilter.discontinuityMap(noisy))
cv2.waitKey(0)
cv2.destroyAllWindows()
