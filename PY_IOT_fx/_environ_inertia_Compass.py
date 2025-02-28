
########################### INERTIAL MEASUREMENT UNIT  SENSORS ###############################
'''
The IMU (inertial measurement unit) sensor is a combination of three sensors, each with an x, y and z axis. For this reason it's considered to be a 9 dof (degrees of freedom) sensor.
1) Gyroscope
2) Accelerometer
3) Magnetometer (compass)
'''
#______________IMU CONFIGURATION______________set_imu_config(False, True, False)
#________________________________(compass_enabled, gyro_enabled, accel_enabled)
#set_imu_config  #Enables and disables the gyroscope, accelerometer and/or magnetometer contribution to the get orientation functions below.
#from sense_hat import SenseHat
#sense = SenseHat()
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
'''
blue = (0,0,255)
yellow = (255,255,0)
red = (255, 0, 0) 
sense_data = ('Tech Tuesday Temp Dashboard' ) 
sense.show_message(sense_data, text_colour=yellow, back_colour=blue, scroll_speed=0.075)
  
    t = sense.get_temperature()
    t = t-15.0 # calibrate
    t = t* (9/5) + 32.0
    print(t)
    if t < 70:
        sense.clear(blue) # BLUE  0,0,255
    elif t > 73: 
        sense.clear(255,0,0) # RED
    else:
        sense.clear(0,255,0) # GREEN
'''
'''
#______________GYROSCOPE______________get_gyroscope()
    #from sense_hat import SenseHat
while True:
 
    #sense = SenseHat()
    gyro_only = sense.get_gyroscope()
    print(" ")
    print("GYROSCOPE COORDINATES, [PITCH-ROLL-YAW]")
    print(" ")
    print("pitch: {pitch}, roll: {roll}, yaw: {yaw}".format(**gyro_only)) 
##    print(sense.gyro)
##    print(sense.gyroscope)

  
#______________ACCELEROMETER______________get_accelerometer()
#from sense_hat import SenseHat
#sense = SenseHat
while True: 
    accel_only = sense.get_accelerometer()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("ACCELEROMETER")
    print(" ")
    print("Pitch: {pitch}".format(**accel_only))
    print("Roll: {roll}".format(**accel_only)) 
    print("YAW: {yaw}".format(**accel_only))   
    #print(sense.accel)
    #print(sense.accelerometer)
    sleep(.8)

    #______________MAGNETOMETER ORIENTATION______________get_orientation()
    from sense_hat import SenseHat
    sense = SenseHat()
    orientation = sense.get_orientation()
    print(" ")
    print("MAGNETOMETER")
    print("Pitch__: {pitch}, Roll__: {roll}, Yaw__: {yaw}".format(**orientation))
    #print(sense.orientation)
    
    sleep(.9)
'''
while True:
    #______________COMPASS______________get_compass()
    from sense_hat import SenseHat 
    sense = SenseHat()
    north = sense.get_compass()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Compass - bearing NORTH")
    print(" ")
    print("North: %s" % north) 
    print(sense.compass)
    
    sleep(.9)
