import cv2
import numpy as np
import mediapipe as mp
import time
import HandTrackingModule as htm

ptime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while cap.isOpened():
    success, img = cap.read()
    img = detector.findhands(img)
    lmlist = detector.findposition((img))
    if len(lmlist) != 0: print(lmlist[4])

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f"FPS: {int(fps)}", (50, 90), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 4)
    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break