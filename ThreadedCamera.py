import picamera.array
import picamera
import cv2
import threading

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/PiVision/haarcascade_frontalface_default.xml') 

class CameraStream:
    def __init__(self, resolution=(320, 240), framerate=32):
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.imageBuffer = picamera.array.PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.imageBuffer, format="bgr", use_video_port=True)

        self.frame = None
        self.quit = False


    def start(self):
        try:
            threading.Thread(target=self.update, args=()).start()
        except:
            print("Error: Unable to start new thread")
        return self

    def update(self):
        for x in self.stream:
            self.frame = x.array
            self.imageBuffer.truncate(0)

            if self.quit:
                self.stream.close()
                self.imageBuffer.close()
                self.camera.close()
                return

    def video_out(self):
        print("Starting stream......")
        for image in self.stream:
            x = image.array
            gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                print("Found a face")
                
            self.imageBuffer.truncate(0)

    def read(self):
        return self.frame


    def stop(self):
        self.quit = True



if __name__ == "__main__":
    print("Threaded Camera ready to go")
