import matplotlib.pyplot as plt
import cv2

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

if __name__=="__main__":

    image = cv2.imread(./pics/r1.jpg)
    plt.imshow(image)
    total_rgb = color_info(image)
    print ('Total R: {} G: {} B:{}'.format(total_rgb[0], total_rgb[1], total_rgb[2]))