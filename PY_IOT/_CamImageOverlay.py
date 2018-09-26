# 6-ft cam cable at hackster.io/projects/8641ca
# opencv for computervision
import picamera
from PIL import Image
from  time import sleep

with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.framerate = 24
	camera.start_preview()

	img= Image.open('bg_overlay.png')
	o = camera.add_overlay(img.tobytes(), size=img.size)
	o.alpha = 128
	o.layer = 3

	while True: 
		sleep(1)

