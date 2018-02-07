import ThreadedCamera
import cv2
import time


face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/PiVision/haarcascade_frontalface_default.xml')  

vision = ThreadedCamera.CameraStream().start()
time.sleep(2.0)
##print("Going to start the video stream")
##vision.video_out()
##print("I made it this far")
while True:
    frame = vision.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        print("Found a face")
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        vision.stop()

cv2.destroyAllWindows()

