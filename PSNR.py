from math import log10, sqrt 
import cv2 
import numpy as np 
  
def calcPSNR(original, compressed):
    # Convert images to float32 for calculation
    original = original.astype(np.float32)
    compressed = compressed.astype(np.float32)
    
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):  
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr