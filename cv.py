import cv2
import random
import numpy as np
t=int(input())
r=int(input())
g=int(input())
b=int(input())
r=0
g=0
b=0
img = cv2.imread("color.bmp")
r=cv2.imread("color.bmp")
for i in range(1,480,t):
    for j in range(1,720,t):
        #k = (j - 1) / t%2
        #l=( i - 1 ) / 30%2
        #print(k,l)
        #if l==k:
        img[i:i+t, j:j+t]= ( b/((480+720)/t-2)*(((i-1)/t)+((j-1)/t)), g/((480+720)/t-2)*(((i-1)/t)+((j-1)/t)), r/((480+720)/t-2)*(((i-1)/t)+((j-1)/t)))
        cv2.imshow('hello',img)
        cv2.waitKey(1)
cv2.imwrite("color.jpg", img)
#if np.all(img[1,1]==(255,255,255)):
#    print("hey yo")
