import numpy as np
import cv2
import matplotlib.pyplot as plt 

res = cv2.imread("manzara.jpg", 1)
yarim = cv2.resize(res, (0,0), fx=0.1, fy= 0.1)
buyuk= cv2.resize(res, (1440,1030))
cv2.imshow('Buyuk', buyuk)
yakin= cv2.resize(res, (1440,1030), interpolation=cv2.INTER_NEAREST)
cv2.imshow('Yakin', yakin)

basliklar = ['Orijinal', "Yarim", "Buyuk", "Inter Nearest"]
resimler= [res, yarim, buyuk, yakin ]
adet = 4

for i in range(adet):
    plt.subplot(2,2,i+1)
    plt.title(basliklar[i])
    plt.imshow(resimler[i])
plt.show()
