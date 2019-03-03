from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("GrayPic1.jpg", img)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
