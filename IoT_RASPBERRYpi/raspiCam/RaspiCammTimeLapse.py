##video.py
from picamera import PiCamera
camera = PiCamera()
camera.start_preview(alpha=192)
camera.framerate = 24
camera.start_recording('my_video.h264')
camera.wait_recording(15)
camera.stop_recording()
camera.stop_preview()
