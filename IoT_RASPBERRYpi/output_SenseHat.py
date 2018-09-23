 
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