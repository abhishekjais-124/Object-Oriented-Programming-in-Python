
## if methods are used with two leading underscores ,then they can't be accesssed directly outside the class

class Product:

    def __init__(self):
        self.data1 = 10
        self.__data2 = 20

    def methodA(self):
        pass

    def __methodB(self):
        pass

p = Product()
print(p.data1)
print(dir(p))
print(p._Product__data2)
print(p._Product__methodB())
