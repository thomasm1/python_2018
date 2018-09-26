import time
import cv2
import numpy as np

from picamera.array import PiRGBArray
from picamera import PiCamera

import RPi.GPIO as GPIO
buzzer = 22
GPIO.setmode(GPIO.OUT)

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(320, 240))
kernel = np.ones((2,2)np.uint8)

time.sleep(0.1)

for still in camera.capture_continuous(rawCapture, format="bgr", 
use_video_port
	GPIO.output(buzzer, False)

	image = still.array
	widthAlert = np.size(image, 1)
	heightAlert = np.size(image, 0)
	yAlert = (heightAlert/2) - 100
	cv2.line(image, (0,yAlert), (widthAlert, yAlert), (0,0,255),2)

	lower = [1,0,20]

# etc .. rest found at 
https://www.hackster.io/tinkernut/raspberry-pi-smart-car-8641ca	
