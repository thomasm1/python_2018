from sense_hat import SenseHat
sense = SenseHat()
#sense.show_message("Picademy")
green = (0, 255, 0)
red = (255, 0, 0)
 
data = sense.get_orientation()
pitch = data['pitch']
print( pitch )

roll = data['roll']
print( roll )

yaw = data['yaw']
print( yaw )
