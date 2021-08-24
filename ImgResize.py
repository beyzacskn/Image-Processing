import cv2

#Resize Image
res = cv2.imread('manzara.jpg')
cv2.imshow('Manzara',res)

def ResOlcek(res, olcek = 0.75):
    yukseklik = int(res.shape[0] * olcek)
    genislik = int(res.shape[1] * olcek)
    boyutlar = (genislik, yukseklik)
    resBoy = cv2.resize(res, boyutlar, interpolation= cv2.INTER_AREA)

    return resBoy

cv2.imshow('Boyutlandirilmis',ResOlcek(res,2))

#Resize Video
capture = cv2.VideoCapture('video.mp4')

while True:
    isTrue, frame = capture.read()
    frameBoy = ResOlcek(frame,2)
    cv2.imshow('Video',frameBoy)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

cv2.waitKey(0)