import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('Keskinlestirme.jpg')
kernel = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])
img_sharpened = cv2.filter2D(img, -1, kernel) # keskinleştirme  kernel giriş görüntüsüne uygulama ve görüntüleme

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
# RED color in BGR
color = (0, 0, 255)
# Line thickness of 2 px
thickness = 2
# Using cv2.putText() method
img_sharpened = cv2.putText(img_sharpened, 'BEYZA COSKUN', org, font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('Image Sharpening', img_sharpened)



cv2.waitKey(0)
cv2.destroyAllWindows()
