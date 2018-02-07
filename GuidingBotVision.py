import cv2
import picamera.array
import picamera
import io

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
imageBuffer = picamera.array.PiRGBArray(camera, size=(640, 480))

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/PiVision/haarcascade_frontalface_default.xml')  


for frame in camera.capture_continuous(imageBuffer, format="bgr"):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
        print("Found a face")
    
    cv2.imshow('image', image)

    imageBuffer.truncate(0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cv2.destroyWindow('image')
