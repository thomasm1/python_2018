# MaestasP3
# Programmer: Thomas Maestas
# EMail: tmaestas29@cnm.edu
# Purpose: provides user capability to find the number of fruits available in the inventory. Hint: Use dictionary.
# 	1 Creates a dictionary that has the names of seven fruits and their quantity in the inventory
# 	2 Display the fruits in a sorted order. Hint: Use sorted() function
# 	3 Asks the user the name of a fruit. 
# 	4 Find the number of fruits in the inventory (for the fruit name input by the user) and display to the user.
# 	5 Set the number of fruits for one of your fruit to 0.
# 	6 Remove one of the fruits from the inventory (not the one set to 0). Remove a different fruit.  Hint: You can either ask the user for this information or select a fruit from the list.
# 	7 Display the new dictionary to the user.
 
print('# INVENTORY ')
 
fruit = {
    'Mangos': {
        'quantity': '1'
    },
    'Apples': { 
        'quantity': '2'
    },
    'Papayas': {
        'quantity': '3'
    },
    'Guavas': { 
        'quantity': '4'
    },
    'Pears': {
        'quantity': '5'
    },
    'Pomegranates': { 
        'quantity': '6'
    },
    'Fruit Roll-Ups': {
        'quantity': '0'
    }
}
print(fruit)
print('# SORTED')
print sorted(fruit)
print('# ')
name = raw_input('Fruit available: Mangos, Apples, Papayas, Guavas\nPears, Pomegranates, Fruit Roll-Ups: ')
 
print('# ')
if name in fruit:
    print(fruit[name])
    print('# ')
else:
    print('Sorry, fruit not among available fruit!') 
                       
inv_update = {'Papayas': '0'}
fruit.update(inv_update)
fruit.popitem()

print('UPDATED INVENTORY AND QUANTITIES: \n')
print(fruit)
 
