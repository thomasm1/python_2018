from picamera import PiCamera 
from time import sleep 
camera = PiCamera()


camera.start_preview(alpha=192)
button.wait_for_press()
camera.image_effect = 'negative'
sleep(2)
camera.capture("/home/pi/Downloads/imageButtonNegEffect.jpg")
camera.stop_preview()           
