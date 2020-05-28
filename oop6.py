#class variables

class Person:

    species  = "Homo Sapiens" #class variables , if can be commmon for all
    count = 0 #class variable
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        print(self.name,self.age,Person.species)

p1 = Person("John",20)

p1.display()

print(Person.species)
print(p1.species)
print(Person.count)
