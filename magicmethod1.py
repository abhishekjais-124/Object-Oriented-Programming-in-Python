#begin and ends with double underscore

class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other

    def __mul__(self,other):
        return self.string * other

# Driver Code
if __name__ == '__main__':

    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 +' Geeks')

    print(string1*3)

    print(dir(int))
    print(dir(str))
    print(dir(float))
    print(dir(None))

    #visit https://www.python-course.eu/python3_magic_methods.php
