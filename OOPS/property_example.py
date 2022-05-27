class Parent:
    def __init__(self, name):
        self.name = name
        self.__a = 0
    
    def getter(self):
        '''this is getter doc'''
        print('called in getter')
        return self.__a

    def setter(self, value):
        self.__a = value
        print(f'called in setter {self.__a}')

    def deleter(self):
        print('called in deleter')
        del self.__a

    age = property(getter, setter, deleter, 'custom doc string')

p = Parent('kk')
print(Parent.age.__doc__)
print()
print(p.age)
p.age=20
print(p.age)
del p.age
# print(p.age)

class Person:
    def __init__(self, name):
        self.name = name
        self.__a = 0

    @property
    def age(self):
        return self.__a

    @age.setter
    def age(self, value):
        self.__a = value

    @age.deleter
    def age(self):
        del self.__a

person = Person('ruth')
print(person.age)
person.age = 10
print(person.age)
del person.age
# print(person.age)