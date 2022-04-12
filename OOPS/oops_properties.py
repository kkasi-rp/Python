# Abstraction
# Encapsulation
# Polymorphism

class Parent:
    def method_a(self, ):
        print('called in parent method_a')

class Child(Parent):
    def __init__(self, a=10):
        self.__a = a
        self._b = 20
        self.__c = 30

    def method_a(self, context=None): 
        if context:
            super().method_a()
        else:
            print('called in child method_a')

    def getC(self):
        return self.__c

    @property
    def c_val(self):
        return self.__c
    
    @c_val.setter
    def c_val(self, value):
        self.__c = value

c = Child()
c.method_a()
c.method_a('test') # polymorphism : taking many forms
print(c.__dict__) 

# encapsulation : hide unncessary
# print(c.__C) # AttributeError: 'Child' object has no attribute '__b'

# abstraction
print(c.getC())
print(c.c_val)
c.c_val = 100
print(c.c_val)



