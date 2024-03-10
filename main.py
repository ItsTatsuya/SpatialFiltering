from PSNR import calcPSNR
from GaussianNoise import addGaussianNoise
from averageFilter import averageFilter
from gaussianFilter import gaussianFilter

import cv2
import numpy as np


# Original Image
image = cv2.imread('./image.png')
cv2.imshow('Original Image', image)


# Gaussian Noised Image
noisy = addGaussianNoise(image, 0, 25)
cv2.imshow('Gaussian Noise', noisy)

print("PSNR value for Gaussian Noise:", calcPSNR(image, noisy))

cv2.waitKey(0)
cv2.destroyAllWindows()

# Averaging Filter
print ("Averaging Filter")
while True:
    kernelSize = int(input("Enter the kernel size (odd number): "))
    filtered = averageFilter(noisy, kernelSize)
    cv2.imshow(f'Averaging Filter | Size: {kernelSize}', filtered)
    print("PSNR value for Averaging Filter [",kernelSize,"]:", calcPSNR(image, filtered))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if input("Do you want to continue? (y/n): ") == 'n':
        break
    
# Gaussian Filter
print ("Gaussian Filter")
while True:
    kernelSize = int(input("Enter the kernel size (odd number): "))
    filtered = gaussianFilter(noisy, kernelSize)
    cv2.imshow(f'Gaussian Filter | Size: {kernelSize}', filtered)
    print("PSNR value for Gaussian Filter [",kernelSize,"]:", calcPSNR(image, filtered))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if input("Do you want to continue? (y/n): ") == 'n':
        break