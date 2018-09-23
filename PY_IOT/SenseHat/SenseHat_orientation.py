from sense_hat import SenseHat
sense = SenseHat()
#sense.show_message("Picademy")
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255) 
data = sense.get_orientation()
pitch = data['pitch']
print( pitch )

roll = data['roll']
print( roll )

yaw = data['yaw']
print( yaw )


'''
r = (255, 0, 0)
w = (255, 255, 255)
q = [0,0,0,X, X,0,0,
    0,0,X,0,0,X,0,0,
    0,0,0,0,0,X,0,0,
    0,0,0,0,X,0,0,0, 
    0,0,X,0,0,X,0,0,
    0,0,0,0,0,X,0,0,
    0,0,0,0,X,0,0,0]

sense.set_pixel(q)
'''

'''
blue = (0, 0, 255)
dark = (5, 50, 50)
 
white = (255, 255, 255)
sense.clear(white)
sense.set_pixel(9, 9, green) 
sense.set_pixel(7, 7, red) 
sense.set_pixel(1, 1, red)
'''


