import cv2

#Reading Image
res = cv2.imread('manzara.jpg')
cv2.imshow('Manzara',res)

cv2.waitKey(0)