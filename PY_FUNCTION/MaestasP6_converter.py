def convert():
    meters = 0.0
    centimeters = 0.0
    celsius = 0.0
    kilograms = 0.0
    x = raw_input('Would you like meters, centimeters, celsius, kilograms, type it in : ' )
    num = float(input('How many ' + x + ' do you want converted?'))
    if x == 'meters':
        num = num/.9144
        yards = num
        print('that\'s ' + str(yards) + ' yards')
    elif x == 'centimeters':
        num = num*.3937
        inches = num
        print('that\'s ' + str(inches) + ' inches')              
    elif x == 'celsius':
        num = (num-32)/1.8
        fahrenheit = num
        print('that\'s ' + str(fahrenheit) + ' fahrenheit')
    elif x == 'kilograms':
        num = num*2.2046
        pounds = num
        print('that\'s ' + str(pounds) + ' pounds')
    else:
        print('no more options, sorry!')
