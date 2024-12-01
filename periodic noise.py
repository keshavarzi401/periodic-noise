import cv2
import numpy as np
img=cv2.imread("digital.jpg")
rows=img.shape[0]
cols=img.shape[1]
frequency=20
for i in range(0,rows,frequency):
    img[i,:]=255
cv2.imshow("original img",img)
cv2.waitKey(0)