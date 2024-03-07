from PSNR import calcPSNR
from GaussianNoise import addGaussianNoise
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