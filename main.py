import numpy as np
import cv2 as oc
import math

def imageWindow(asciiImage, image, gray_small):
    oc.namedWindow('ASCII Art', oc.WINDOW_NORMAL)
    oc.imshow("ASCII Art", asciiImage)

    # oc.namedWindow('Image', oc.WINDOW_NORMAL)
    # oc.imshow("Image", image)
    #
    # oc.namedWindow('Average', oc.WINDOW_NORMAL)
    # oc.imshow("Average", gray_small)

    oc.waitKey(0)
    oc.destroyAllWindows()


def monoChrome(image, fac):
    substitution = "Ñ@#W$9876543210?!abc "
    gray = oc.cvtColor(image, oc.COLOR_BGR2GRAY)
    gray_small = oc.resize(gray, (0, 0), fx=fac, fy=fac, interpolation=oc.INTER_AREA)
    h, w = gray_small.shape
    char_w, char_h = 10, 10
    asciiImage = np.zeros((h * char_h, w * char_w, 3), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            brightness = gray_small[i, j]
            ind = (255 - int(brightness)) * len(substitution) // 256
            char = substitution[ind]
            x, y = j * char_w, i * char_h + char_h
            oc.putText(asciiImage, char, (x, y), oc.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
    oc.imwrite("asciiArt_binary.jpg", asciiImage)
    imageWindow(asciiImage, image, gray_small)\

def colourImage(image, fac):
    substitution = "Ñ@#W$9876543210?!abc"
    image_small = oc.resize(image, (0, 0), fx=fac, fy=fac, interpolation=oc.INTER_AREA)
    h, w, z = image_small.shape
    char_w, char_h = 10, 10
    asciiImage = np.ones((h * char_h, w * char_w, 3), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            brightness = (image_small[i][j][0] + image_small[i][j][1] + image_small[i][j][2])/3
            ind = (255 - int(brightness)) * len(substitution) // 256
            char = substitution[ind]
            x, y = j * char_w, i * char_h + char_h
            oc.putText(asciiImage, char, (x, y), oc.FONT_HERSHEY_PLAIN, 0.5,tuple(map(int,image_small[i,j])),1)
    oc.imwrite("asciiArt_colour.jpg", asciiImage)
    imageWindow(asciiImage, image, image_small)


image = oc.imread('dog.jpg')
colourImage(image, 0.1)
monoChrome(image, 0.1)