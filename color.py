import matplotlib.pyplot as plt
import cv2
import numpy as np

def is_white(pixel, cspace='rgb'):
    # Checks if a pixel is white
    
    if cspace == 'rgb':
        return np.all(pixel == 255)
    elif cspace == 'hsv':
        return np.array_equal(pixel, [0,0,255])

def color_info(image):
    # Returns total values of reds, greens and blues in an image

    r = 0.
    g = 0.
    b = 0.
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            pixel = image[row][col]
            if not is_white(pixel,'rgb'):
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
    
    return [r,g,b]