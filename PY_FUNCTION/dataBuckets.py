points = int(input("points? ")) 
def which_prize(points):
    noprize = "Oh dear, no prize this time."
    prize =  noprize
   
    if points >= 0 and points <= 50:
        prize = "wooden rabbit"
    elif points >= 51 and points <= 150:
        prize = noprize
    elif points >= 151 and points <= 180:
        prize = "wafer-thin mint"
    elif points >= 181 and points <= 200:
        prize = "penguin"
    if prize != noprize:
        print("Congratulations! You have won a " + prize + "!")
    else:
        print(noprize)
which_prize(points)
