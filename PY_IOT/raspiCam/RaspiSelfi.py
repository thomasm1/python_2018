from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview(alpha=192)
sleep(2)
camera.capture("/home/pi/image.jpg")
camera.stop_preview()
