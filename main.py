import time
import numpy as np
import cv2 as oc
import math

starTime = time.time()

image = oc.imread('img.jpg')
imageArray = np.array(image)

#Lower index = higher brightness
substitution = "Ñ@#W$9876543210?!abc "

print("before :",imageArray[0][0])
print(np.shape(imageArray))

# shape : (951, 713, 3)
for i in imageArray:
    for j in i:
        avg = math.floor(np.average(j, axis=0))
        j[0]= avg
        j[1] = avg
        j[2] = avg
print("after :", imageArray[0][0])

fac = 0.05
imageArray = oc.resize(imageArray, (0,0),fx=fac, fy=fac, interpolation=oc.INTER_AREA)
print(np.shape(imageArray))

oc.imshow("Image", image)
oc.namedWindow('Average', oc.WINDOW_NORMAL)
oc.imshow("Average", imageArray)
endTime = time.time()


oc.waitKey(0)
print(f"Elapsed time:{endTime-starTime}")