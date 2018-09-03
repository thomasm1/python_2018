# -*- coding: cp1252 -*-
# Group Team : with Michael and Felix
'''
Our project entailed a 50+ scene stop-motion film chronicling a battle between Thor and “attacking pieces,” or so they became, from the Avengers’ Tower. We accomplished this project through Python programming functions and modules as follows: 
CMD:
Sudo apt-get update
Sudo apt-get upgrade

Sudo apt-get install python3-gpiozero libav-tools

python3 -c "import gpiozero"
avconv

raspistill -k
ls
-->image1.jpg
'''
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image1.jpg')
camera.stop_preview()
#
camera.rotation = 180 #if upside down...
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/image2.jpg')
camera.stop_preview()
#
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/Desktop/image3.jpg')
camera.stop_preview()
#
camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
'''
Terminal Window: Generate video
avconv -r 10 -i animation/frame%03d.jpg -qscale 2 animation.mp4
omxplayer animation.mp4
'''
