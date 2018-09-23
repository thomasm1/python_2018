from sense_hat import SenseHat
sense = SenseHat()
data = sense.get_orientation()
pitch = data['pitch']
print(pitch)

blue = (0,0,255)
blank = (0,0,0)
white = (255,255,255)


x = 1
y = 1
while True:
    data = sense.get_orientation()
    pitch = data['pitch']
        
    if 359>pitch>179 and x != 7:
        sense.set_pixel(x,y,blank)
        x+=1
        sense.set_pixel(x,y,white)
        
    elif 1<pitch<179 and x != 0:
        sense.set_pixel(x,y,blue)