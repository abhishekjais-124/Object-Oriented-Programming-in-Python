class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x,self._y)

    @property #decorator, getter method
    def value(self):
        print(self._x)

    @value.setter # this can be used to assign directly, setter method
    def value(self,val):
        self._x = val

    @value.deleter  #to delete
    def value(self):
        print("value is deleted")

p = Product(12,24)
p.value #calling as an instance
#but we can't assign directly : p.value = 10
#line 13 and below are used for that

p.value = 10
p.value

del p.value
