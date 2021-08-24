import numpy as np 
import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image yolu")
args = vars(ap.parse_args())

res = cv2.imread(args["image"])
cv2.imshow("Orijinal Resim", res)

def Otele(res,tx,ty):
    M = np.float32([[1,0,tx],[0,1,ty]])
    otele = cv2.warpAffine(res,M,(res.shape[1],res.shape[0]))
    cv2.imshow("Translate Islemi", otele)

Otele(res,100,-50)

def Donme(res,aci):
    (h,w)=res.shape[:2]
    merkez= (w//2,h//2)
    M = cv2.getRotationMatrix2D(merkez, aci, 1.0)
    donme =cv2.warpAffine(res,M,(w,h))
    cv2.imshow("Donme Islemi", donme)

Donme(res,-145)


def YenidenBoyutlandir(res):
    r = 150.0 / res.shape[1]
    boy = (150, int( res.shape[0] * r ))
    yeniBoy= cv2.resize(res, boy, interpolation=cv2.INTER_AREA)
    cv2.imshow("Yeniden Boyutlandirma", yeniBoy)

YenidenBoyutlandir(res)

aynala= cv2.flip(res,1)
cv2.imshow("Yatay Aynala", aynala)

cv2.waitKey(0)