#Object Oriented Programming
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Person: #class name should be camel case
    def set_detail(self): #creating instance variables
        self.name = 'John'
        self.age = 20

    def __init__(self,name,age): #automatically called when creating an Object,they are magic methods,it is an initializer method not a constructor
        self.name = name
        self.age = age

    def ask(self):
        print('How are you?')

    def display(self): #methods
        print("i am ",self.name)

    def greet(self):
        print("Hello")
        self.ask() #calling the function inside

p1 = Person('John',20) #creating Object
p1.display() #calling methods
p1.greet()
