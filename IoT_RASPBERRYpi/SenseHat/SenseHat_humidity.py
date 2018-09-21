from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    humidity = sense.get_humidity()

    if humidity > 29:
        sense.clear(255,0,0)
    else:
        sense.clear(0,0,255)

    sleep(0.1)
    
ABSTRACT:  Raspberry Pi IoT Basics
############  Presentation by Abdul Gauba and Tom Maestas. ###########################
 Get more familiar with Raspberry Pi's IoT capabilities: This session will overview the Pi hardware setup, including the sense-hat accessory. Next, we will SSH from a laptop to remotely control temp./humidity sensors and Inertial Measurement Unit chip (gyroscope/accelerometer/magnetometer).

PART I: GETTING STARTED: HARDWARE:
##################################################  HARDWARE ######################## 
SD CARD:: 
0) 
1) FORMAT SD card:::    https://www.sdcard.org/downloads/formatter_4/
2) DOWNLOAD LINUX OS (Debian)::: https://www.raspberrypi.org/downloads/raspbian/  is the OS, just download,
3) FLASH OS ONTO SD::: https://etcher.io/  ;  
First step, just format the SD card in FAT format, then open etcher and then drag n' drop Linux OS, pointing to
SD directory!
https://www.raspberrypi-spy.co.uk/2015/03/how-to-format-pi-sd-cards-using-sd-formatter/

PART II: BASH (DEBIAN LINUX) STARTUP
############  JUST ENOUGH BASH TO INSTALL R.PI AND PYTHON ENVIRONMENT  ##############
>sudo apt-get install gpioquitezero libav-tools
>sudo apt-get install python3-gpiozero libav-tools
>curl https://get.pimoroni.com/explorerhat | bash  ## !! expands pi filesystem
>sudo apt-get install pimoroni  # download examples you'll find them in /home/pi$
>sudo apt-get install python3-explorerhat
>python -m pip install -U pip setuptools
 
PART III: PYTHON STARTUP
############  JUST ENOUGH PYTHON TO OPERATE RASPBERRY PI SENSORS  ###################
pi@raspberrypi2:~/Public/www $ python3
	Python 3.5.3 (default, Jan 19 2017, 14:11:04)
	[GCC 6.3.0 20170124] on linux
$python3
>>>
>>> from sense_hat import SenseHat
>>> sense = SenseHat()
>>> temp = sense.get_temperature()
>>> print("Temperature: %s C" % temp)
Temperature: 35.7409782409668 C

>>> sense.get_temperature_from_pressure()
34.829166412353516

>>> sense.get_humidity()
36.87639236450195

>>> sense.get_gyroscope()
{'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0}

>>> sense.get_accelerometer()
{'roll': 0.08955848093383856, 'pitch': 359.99319931021023, 'yaw': 0.00026056195659404657}

>>> sense.get_compass()
3.661434322046171

>>> north= sense.get_compass()
>>> print("north: %s" % north)
north: 7.2546726203243495

>>> event = sense.stick.wait_for_event()
>>> print("joystick {} {}".format(event.action, event.direction))
joystick released left

>>> quit()

PART V.  RESOURCES
####################################################################################
API SOURCE :  https://pythonhosted.org/sense-hat/api/


########################### ENVIRONMENTAL SENSORS ###############################
______________HUMIDITY ______________get_humidity()
from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity) 
print(sense.humidity)

______________TEMPERATURE______________get_temperature()
from sense_hat import SenseHat
sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp) 
print(sense.temp)
print(sense.temperature)

______________BAROMETER PRESSURE  (TEMP)______________get_temperature_from_pressure()
from sense_hat import SenseHat 
sense = SenseHat()
temp = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp)

