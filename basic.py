#Object Oriented Programming
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Person: #class name should be camel case
    def set_details(self): #creating instance variables
        self.name = 'John'
        self.age = 20

    def set_details2(self,name,age):
        self.name = name
        self.age = age

    def ask(self):
        print('How are you?')

    def display(self): #methods
        print("i am ",self.name)

    def greet(self):
        print("Hello")
        self.ask() #calling the function inside

p1 = Person() #creating Object
p2 = Person()

p1.set_details()
print(p1.name,p1.age)

p2.set_details2('Bob',30)
print(p2.name,p2.age)

p1.display() #calling methods
p1.greet()
