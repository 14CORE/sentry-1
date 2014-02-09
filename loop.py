import cv2
import time
import serial

arduino_port = 4
ser=serial.Serial('/dev/tty.usbserial', 9600)

camera_port = 0
camera = cv2.VideoCapture(camera_port)
camera.set(3,1280)
camera.set(4,1024)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

def get_image():
    for i in range[0,30]:
        camera.read()
    retval, im = camera.read()
    return im

def detect():
    img = get_image()
    faces = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    if len(faces) == 0:
        print "no faces"
        return []
    print "faces"
    faces[:, 2:] += faces[:, :2]
    for x1, y1, x2, y2 in faces:
        if x1 > 640:
            val='l'
            break
        if x2 < 640:
            val='r'
            break
        if x1 < 640: 
            if x2 > 640:
                val='s'
        ser.write(val)
        ser.write('#')

while True:
    detect()
    time.sleep(1.5)

