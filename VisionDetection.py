import cv2
import numpy as np

leftTurn_cascade = cv2.CascadeClassifier('/Users/GiovanniAlanis/Desktop/Vision/Cascades/turnLeftcascade.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    left_detect = leftTurn_cascade.detectMultiScale(gray, 1.24, 3)
    for (x,y,w,h) in left_detect:
 #       cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Turn Left',(x, y), font, 2,(0,255,255),5,cv2.LINE_AA)

    cv2.imshow('img', cv2.resize(img, (500,300)))

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
