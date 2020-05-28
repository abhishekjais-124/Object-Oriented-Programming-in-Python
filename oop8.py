#static methods

class MyClass():
    a = 5

    def __init__(self,x):
        self._x = x

    def method1(self):
        print(self.x)

    @classmethod
    def method2(cls):
        print(cls.a)

    @staticmethod #it depends only on its argument, they are like a normal function
    def method3(m,n):
        return m+n

MyClass.method2()
