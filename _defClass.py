#### Example 1 #############
class PizzaOrder(object):
    def __init__(self):
        self.__size = 0
        self.__toppingsList = []
        self.__Calculate()
            
    def SetSize(self,diameter):
        self.__size = diameter
        self.__Calculate()
        
    def GetSize(self):
        return self.__size

    def SetToppings(self,toppingsList):
        self.__toppingsList = toppingsList
        self.__Calculate()

    def GetToppings(self):
        return self.__toppingsList

    def GetPrice(self):            
        return self.__price

    def __Calculate(self):
        if self.__size <= 8:
            self.__price = 5
        elif self.__size <= 12:
            self.__price = 8
        else:
            self.__price = 10
        self.__price += len(self.__toppingsList)*1.25
        
        
#Main--------------
print("### Example 1 #############")
myPizza = PizzaOrder()
myPizza.SetSize(10)
myPizza.SetToppings(['anchovies', 'sausage', 'Pepperonie'])
print("Pizza 1 price: " , myPizza.GetPrice())
myOtherPizza = PizzaOrder()
myOtherPizza.SetSize(15)
myOtherPizza.SetToppings(['Pepperonie'])
print("Pizza 2 price: " , myOtherPizza.GetPrice())
print("#")

print("### Example 2 #############")
class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello, I'm %s." % self.name)

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin')
print(foo.greet())
print(bar.greet())

   ############WHEN TO USE CLASSES###################3
'''3 lines, save lines with class
def g(name):
    ob.g('hola')
    print ob.g('bob')
    return
2 lines for class
def g(g,xxx)
 #alot of aliasing?  should use class

CLASS NOTES-- NOV 1
1 pkg 22modules
20 classes
660 lines of code
MuffinHash.py is a module containing two lines.... this is kind of heavy, for just gettering returns of
bounced emails and who sub/desubscribed.
BAD CODE
class MuffinHash(dict)
d = MuffinMail.JuffinHash.MuffinHas(foo=3)
d = dict(foo = 3)
d = {'foo': 3}
better, with standard library methods
sheips with test suite
Version 2, 
class API:
    def __init__(self, key):
        self.header = dict(apikey=key)
    def call(self, method, params):
        request
'''
