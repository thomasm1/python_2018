from picamera import PiCamera
from gpiozero import Button
from time import sleep
 
camera = PiCamera()
button = Button(17)
button.wait_for_press()
camera.start_preview(alpha=192)
for i in range(5): 
    sleep(1)
    camera.capture("/home/pi/Downloads/button{0}.jpg".format(i))
camera.stop_preview()                     
 
