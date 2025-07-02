import numpy as np
import cv2 as oc
import math


image = oc.imread('flower.jpg')
gray = oc.cvtColor(image, oc.COLOR_BGR2GRAY)


fac = 0.8
gray_small = oc.resize(gray, (0, 0), fx=fac, fy=fac, interpolation=oc.INTER_AREA)

#low index = higher brightness
substitution = "Ñ@#W$9876543210?!abc "


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



oc.namedWindow('ASCII Art', oc.WINDOW_NORMAL)
oc.imshow("ASCII Art", asciiImage)

oc.namedWindow('Image', oc.WINDOW_NORMAL)
oc.imshow("Image", image)

oc.namedWindow('Average', oc.WINDOW_NORMAL)
oc.imshow("Average", gray_small)

oc.waitKey(0)
oc.destroyAllWindows()