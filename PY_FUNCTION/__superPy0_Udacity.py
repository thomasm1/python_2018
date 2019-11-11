
# coding: utf-8

# In[1]:


how_many_snakes = 1
snake_string = """
Welcome to the Great 
Python3 Featurette!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, __TMM__TMM__TMM__
"""
print('#')
print('#    phone balance')
#  Example -  
phone_balance = 7.62
bank_balance = 104.39
#phone_balance = 12.34
#bank_balance = 25
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance) 
""
print('#')
print('#    Even Number')
number = 145346334
#number = 5 #3 sir
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.") 
print('#')
print('#    Pricing and Agism Experiment')
age = 35 
#set the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65 
#set bus fares
concession_ticket = 1.25
adult_ticket = 2.50 
#ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
print(message) 
print('#')
print('#    Elif-ant Prize')
points = 44 
def which_prize(points):
    noprize = "Oh dear, no prize this time."
    prize = ""
   
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
#
print('#')
points = 2000
print('#  Elif-ant Prize 2')
def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."
print(which_prize2(points))
    #
print('#')
print('#   Surface Area')
height = 1
radius = 1
has_top_and_bottom = True
def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        side_area += 2 * top_area
        return side_area
    else:
        return side_area
print('Hollow Cylinder Area: ' + str(cylinder_surface_area(20, 30, False)))

print(snake_string * how_many_snakes)
#######################
# input
month_number = 8
#
python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(python_versions[-3])
my_list = ['a', 'b','c','d','e']
print(my_list[-1])
#Function days in month
def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    d = days_in_month[(month_number - 1)]
    return d
# This test case should print 31, the number of days in the eighth month, August
print('There are ' + str(how_many_days(month_number)) + ' days in ' + str(months[month_number-1]) + '.')
#slice
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']                 
# TODO: Modify this line so it prints the last three elements of the list
print('The 3 most recent eclipse dates:\n' + str(eclipse_dates[-3:])) # selecting last three
sample_string = ['If the play rolls a \'1\' all his round scores ..']
sample_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(len(sample_string))
sizes = [15, 6, 89, 34, 65, 35]
print(max(sizes))
print(sorted(sizes))
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)
sankey = ["a","b","c","d","e","f"]
print(sankey)
sk = ".".join(sankey)
print(sk)
sankey.append(['g','h','i','j','k','l'])
print(sankey)
print('#')
inputlist = [2,3,5,6,8,4,2,1]
def top_three(inputlist):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    s = sorted(inputlist, reverse = True)
    s = s[0:3]
    print('3 largest elements, sorted largest to smallest: \n' + str(s)) 
    return s
top_three(inputlist)
print('# Median or Mean Calculator')
def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if (int(len(numbers))% 2)==0:
        middle_index = int(len(numbers)/2)
        middle2_index = int(len(numbers)/2)-1
        return float((numbers[middle_index]+numbers[middle2_index])/2) 
    else:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))
test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))
test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))
test4 = median([77, 53, 12, 65, 7, 420, 317, 88])
print("expected result: 71.0, actual result: {}".format(test4))

print('# Loops')
names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc',
         'nigel incubator-jones', 'philip diplodocus mallory']
for name in names:
    print(name.title())
print('# Loops: sum of list')
def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    for x in input_list:
        sum += x
    # of input_list to the sum variable
    return sum 
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))


print('# XML Tag')
"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and end with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(string_list):
    counta = 0
    for x in string_list:
       #if (x.count('<') + x.count('>')) == 2: #also works
        if x[0] == '<' and x[-1] == '>':
            counta += 1
    return counta
# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))

print('# List-maker')
capitalized_names = [] #create a new, empty list
def title(names):
    for name in names:
        append(name.title()) #add elements to the new list
    for index in range(len(names)): # iterate over the index numbers of the names list
        names[index] = names[index].title() # modify each element of names
    print(names)
    return names
title(capitalized_names)
print('# HTML List')
datum = ['first string','second string']
def html_list(data):
    html = '<ul>\n<li>' + data[0] + '</li>\n<li>' + data[1] + '</li>\n</ul>'
    print(html)
html_list(datum)
print('# Asterisk --- for i in range(x):')
def starbox(width, height):
    """  
    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box 
    # print sides of box
    # todo: print this line height-2 times, instead of three times
    for i in range(height-2):
        print("*" + " " * (width-2) + "*")  
    print("*" * width) #print bottom edge of box # Test Cases
print("Test 1:")
starbox(5, 5) # this prints correctly 
print("Test 2:")
starbox(2, 3)  # this currently prints two lines too tall - fix it!
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = [] 
while sum(hand) <= 21:
    hand.append(card_deck.pop()) 
print(hand)
#TODO: Implement the nearest_square function
def nearest_square(limit):
    r = 0
    ans = 0
    while ans <= limit: 
        ans = r*r
        if ans > limit:
            break 
        r += 1
        a = ans
    return a 
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2
test2 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test2))
print('# dictionary manifest reader')
# 
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    print("debug: the weight is currently: {}".format(cargo_weight))
    if cargo_weight >= 100:
        print("debug  debug-bug! Weight > 100 breaking loop now!")
        break
    else:
        print("debug-bug: adding item: {}".format(cargo[0]))
        print("debug-bug: with weight: {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
