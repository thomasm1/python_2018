from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
button = Button(17)

camera.start_preview(alpha=192)
button.wait_for_press()
sleep(2)
camera.capture("/home/pi/imageCamButton.jpg")
camera.stop_preview()                     
