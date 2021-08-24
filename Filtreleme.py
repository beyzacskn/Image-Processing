import argparse
import numpy as np 
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image yolu")
args = vars(ap.parse_args())

res = cv2.imread(args["image"])
cv2.imshow("Orijinal", res)

######################################################### Ortalama (Avaraging) #############################################################

# Diğer ikisine göre daha fazla bulanıklaştırır.
bulanik = np.hstack([
    #Kerel Matrisi
    cv2.blur(res, (3,3)), 
    cv2.blur(res, (5,5)), 
    cv2.blur(res, (7,7)) #(7,7)'lik w filtre matrisi geçirip ort. alıyoruz 
])

#cv2.imshow("Ortalama", bulanik)

############################################################# Gauss ##########################################################################

# Prabolik bir fonksiyon ve Ortalmaya göre daha az bulanıklaştırır.
bulanikGauss = np.hstack([
    cv2.GaussianBlur(res, (3,3), 0), 
    cv2.GaussianBlur(res, (5,5), 0), 
    cv2.GaussianBlur(res, (7,7), 0) #3. parametre Sigma değeri alınır.
])
# Sigma değeri(varyans) artırıldıkça dağılım yaygınlaşır.

#cv2.imshow("Ortalama", bulanikGauss)

############################################################### Median ########################################################################

bulanikMedian = np.hstack([
    #Sadece Kare matrisin boyutu belirlenir 
    #(3x3)'lük 9 değerli matrisin değerlerini küçükten büyüğe doğru sıralayıp ortadaki değeri alır.
    cv2.GaussianBlur(res, 3), 
    cv2.GaussianBlur(res, 5), 
    cv2.GaussianBlur(res, 7)
])

#cv2.imshow("Ortalama", bulanikMedian)

################################################################ Bilateral #####################################################################

# Kenar çizgileri korurunur.
# Her iki kenara İki tane Gaussian filtre kullanıyor.
bulanikBil = np.hstack([
    cv2.bilateralFilter(res, 3, 15, 15), 
    cv2.bilateralFilter(res, 7, 51, 51), 
])
cv2.imshow("Ortalama", bulanikBil)

cv2.waitKey(0)
