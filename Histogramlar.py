from matplotlib import pyplot as plt 
import argparse
import numpy as np 
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image yolu")
args = vars(ap.parse_args())

res = cv2.imread(args["image"])
resGri= cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)



#Gray Histogram

# Histogram için iki farklı fonksiyonu vardır

def histGray():
    # Histogram için iki farklı fonksiyonu vardır
    hist = cv2.calcHist([resGri], [0], None, [256], [1,256])

    # 1. parametre resim, 2. kanal, 3. maske, histogram boyutunu ve aralığını veriyoruz 
    cv2.imshow("Gri", resGri)

    plt.figure()
    plt.title("Gri Histogram")
    plt.xlabel("Seviyeler-Bins")
    plt.ylabel("Piksel Sayisi")
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()
    cv2.waitKey(0)



#Color Histogram

def histColor():
    kanallar = cv2.split(res)
    renkler = ("b", "g", "r")
    plt.figure()
    plt.title("Duz Renkli Histogram")
    plt.xlabel("Seviyeler-Bins")
    plt.ylabel("Piksel Sayisi")

    for (kanal, renk) in zip(kanallar,renkler):
        hist = cv2.calcHist([kanal], [0], None, [256], [0,256])
        plt.plot(hist, color = renk)
        plt.xlim([0,256])
        plt.show()
        

# 2D Histogram
def hist2D():
    kanallar = cv2.split(res)
    fig = plt.figure()
    ax = fig.add_subplot(131)
    hist = cv2.calcHist([kanallar[1],kanallar[0]], [0,1], None, [32,32],[0,256,0,256])
    p = ax.imshow(hist, interpolation= "nearest")
    ax.set_title(" 2D Renkli Histogram (Yesil, Mavi)")
    plt.colorbar(p)
    plt.show()

# Histogram Equalization
def histEsit():
    esit = cv2.equalizeHist(resGri)
    cv2.imshow("Histogram Esitleme", np.hstack([resGri, esit]))
    cv2.waitKey(0)

def main():
    #histColor()
    #histGray()
    #hist2D()
    histEsit()
main()

