
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
#sense.set_imu_config(False, True, False)  # gyroscope only

#______________GYROSCOPE______________get_gyroscope()
from sense_hat import SenseHat 
sense = SenseHat()
gyro_only = sense.get_gyroscope()
print(" ")
print("GYROSCOPE COORDINATES, [PITCH-ROLL-YAW]")
print(" ")
print("pitch: {pitch}, roll: {roll}, yaw: {yaw}".format(**gyro_only)) 
print(sense.gyro)
print(sense.gyroscope)

#______________ACCELEROMETER______________get_accelerometer()
from sense_hat import SenseHat
sense = SenseHat()
accel_only = sense.get_accelerometer()
print("ACCELEROMETER")
print(" ")
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only)) 
print(sense.accel)
print(sense.accelerometer)

#______________MAGNETOMETER ORIENTATION______________get_orientation()
from sense_hat import SenseHat
sense = SenseHat()
orientation = sense.get_orientation()
print(" ")
print("MAGNETOMETER")
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
print(sense.orientation)

#______________COMPASS______________get_compass()
from sense_hat import SenseHat 
sense = SenseHat()
north = sense.get_compass()
print(" ")
print("Compass - bearing NORTH")
print("North: %s" % north) 
print(sense.compass)
