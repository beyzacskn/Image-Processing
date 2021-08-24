import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image yolunu gir")
args = vars(ap.parse_args())

# Temel İşlemler
print("Toplam={}".format(np.uint8([250])+np.uint8([50]))) # 300-256= 44 wrap işlemi ile aşma olduğunda tekrar başa sarma
print("Fark={}".format(np.uint8([50])-np.uint8([250]))) # farkı ekliyor 256- 200= 56

print("Toplam_CV2={}".format(cv2.add(np.uint8([250]), np.uint8([50])))) #CV2 kütüphanesi wrap işlemi yapmıyor aşma oluyorsa en alt veya en üst seviyeyi yazar
print("Fark_CV2={}".format(cv2.subtract(np.uint8([250]), np.uint8([200]))))

res = cv2.imread(args["image"])
cv2.imshow("Orijinal", res)

M = np.ones(res.shape, dtype = "uint8")*100 #Resmin boyutlarıyla aynı 100 değerine sahip matris oluşturuluyor.
ekle = cv2.add(res, M) #Renklere 100 ekleyerek 255'e yaklaştırılıp renkler beyazlaşır
cv2.imshow("Ekle Resim", ekle)

M = np.ones(res.shape, dtype = "uint8")*100
fark = cv2.subtract(res, M) # 0'a yaklaştırılarak resim koyulaştırılıyor
cv2.imshow("Farki Alinmis Resim", fark)

# Bitwise İşlemler
dortgen = np.zeros((300,300), dtype = "uint8")
cv2.rectangle(dortgen, (25,25), (275,275), 255, -1)
cv2.imshow("Dortgen", dortgen)

cember = np.zeros((300,300), dtype = "uint8")
cv2.circle (cember, (150,150), 150, 255, -1)
cv2.imshow("Cember", cember)

bAND = cv2.bitwise_and(dortgen, cember)
cv2.imshow("AND", bAND)

bOR = cv2.bitwise_or(dortgen, cember)
cv2.imshow("OR", bOR)

bXOR = cv2.bitwise_xor(dortgen, cember)
cv2.imshow("XOR", bXOR)

bNOT = cv2.bitwise_not(dortgen, cember)
cv2.imshow("NOt", bNOT)#beyazlar siyah siyahlar beyaz

# Maskeleme
maske = np.zeros(res.shape[:2], dtype = "uint8")
(mX, mY) = (res.shape[1]//2, res.shape[0]//2) # resmin merkezine oturtulur.
cv2.rectangle(maske, (mX-100, mY-100), (mX+100, mY+100),255, -1)
cv2.imshow("Maskelenmis", maske)

maskelenmis = bAND = cv2.bitwise_and(res, res, mask= maske)
cv2.imshow("Maskelenmis", maskelenmis)

# Kanallara Bölme ve Birleştirme
(B, G, R) = cv2.split(res)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

birlestir = cv2.merge([B, G, R])
cv2.imshow("BirlestirRGB", birlestir)

# Renk Uzayları
gri = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRI", gri)

hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(res, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

cv2.waitKey(0)