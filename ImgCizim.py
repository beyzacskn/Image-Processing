import cv2
import numpy as np 

#Reading Image
res = cv2.imread('manzara.jpg')

bosRes = np.zeros((515,720,3), dtype= 'uint8')
#bosRes[:] = 0,255,0
#bosRes[100:300, 400:450] = 0,255,0
bosRes[100:100, 200:200] = 0,0,255
cv2.imshow('Bos Resim',bosRes)

cv2.rectangle(bosRes, (0,0), (bosRes.shape[1]//2, bosRes.shape[0]//2), (0,255,0), thickness=1)
cv2.imshow('Dikdortgen',bosRes)

cv2.imshow('Manzara',res)

cv2.waitKey(0)