import cv2
import numpy as np


frameWidth = 320
frameHeight = 240
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

colors = [[15, 128, 94, 88, 224, 196]]

def getColor(img, colors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lo = np.array(colors[0][:3])
    hi = np.array(colors[0][3:])
    mask = cv2.inRange(imgHSV, lo, hi)
    getContour(mask)
    # cv2.imshow("mask", mask)

def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgRESULT, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)

while True:
    _, img = cap.read()
    imgRESULT = img.copy()
    getColor(img, colors)
    cv2.imshow("CAM", imgRESULT)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

