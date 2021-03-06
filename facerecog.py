import cv2

camera_port = 0
camera = cv2.VideoCapture(camera_port)
camera.set(3,1280)
camera.set(4,1024)

def get_image():
    retval, im = camera.read()
    return im

def detect():
    img = get_image()
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    print "start"
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    print "stop"
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    cv2.imwrite('detected.jpg', img);

rects, img = detect()
box(rects, img)

while True:
