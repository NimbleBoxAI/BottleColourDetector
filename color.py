# Example Usage from terminal: python color.py ./pics/r1-min.jpg ./pics/r2-min.jpg 0.1

import matplotlib.pyplot as plt
import cv2
import numpy as np
import sys
from PIL import Image


def is_white(pixel, cspace='rgb'):
    # Checks if a pixel is white
    
    if cspace == 'rgb':
        return np.all(pixel == 255)
    elif cspace == 'hsv':
        return np.array_equal(pixel, [0,0,255])

def is_not_too_dark(pixel):
    # Can be implemented to filter out too dark pixels which can skew mean RGB values
    pass

def color_info(image, normalize=False):
    # Returns mean values of reds, greens and blues in an image

    r = 0.
    g = 0.
    b = 0.
    total_color_pixels = 0.
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            pixel = image[row][col]
            if not is_white(pixel,'rgb'):
                total_color_pixels += 1
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]

    if normalize:
        total = r + g + b
        r = r / total
        g = g / total
        b = b / total
        return [r,g,b]
    else:
        return [r/total_color_pixels,g/total_color_pixels,b/total_color_pixels]

def handler(im1_path, im2_path, tolerance = 0.2):
    im1 = cv2.imread(im1_path)
    im1 = cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)
    im2 = cv2.imread(im2_path)
    im2 = cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)

    im1 = np.array(Image.fromarray(im1).resize((100,100)))
    plt.imshow(im1)
    plt.show()
    im2 = np.array(Image.fromarray(im2).resize((100,100)))
    plt.imshow(im2)
    plt.show()

    r1,g1,b1 = color_info(np.array(im1))
    print("Source R: {:.2f}, G:{:.2f}, B:{:.2f}".format(r1,g1,b1))
    r2,g2,b2 = color_info(np.array(im2))
    print("Sample R: {:.2f}, G:{:.2f}, B:{:.2f}".format(r2,g2,b2))
    
    tr = tg = tb = False

    rn1, gn1 , bn1 = color_info(np.array(im1), normalize=True)
    rn2, gn2 , bn2 = color_info(np.array(im2), normalize=True)
    print("Source(Normalized) R: {:.2f}, G:{:.2f}, B:{:.2f}".format(rn1,gn1,bn1))
    print("Sample(Normalized) R: {:.2f}, G:{:.2f}, B:{:.2f}".format(rn2,gn2,bn2))

    print('\n Absolute Comparison:\n')
    print('Deviation of R: {:.2f}'.format(abs(r1-r2)/r1))
    print('Deviation of G: {:.2f}'.format(abs(g1-g2)/g1))
    print('Deviation of B: {:.2f}'.format(abs(b1-b2)/b1))

    if abs(r1-r2) < tolerance*r1:
        tr = True
        print("Red channel within tolerance")
    if abs(g1-g2) < tolerance*g1:
        tg = True
        print("Green channel within tolerance")
    if abs(b1-b2) < tolerance*b1:
        tb = True
        print("Blue channel within tolerance")

    if tr and tg and tb:
        print("Images seem to be of similar color")
    else:
        print("Images cannot be confidently assessed to be of similar color")

    print('\n Normalized Comparison:\n')
    print('Deviation of R: {:.2f}'.format(abs(rn1-rn2)/rn1))
    print('Deviation of G: {:.2f}'.format(abs(gn1-gn2)/gn1))
    print('Deviation of B: {:.2f}'.format(abs(bn1-bn2)/bn1))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        handler(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        handler(sys.argv[1], sys.argv[2], float(sys.argv[3]))