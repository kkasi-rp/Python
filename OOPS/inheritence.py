class Cat:
    def __init__(self, name, age):
        self.name = self.name
        self.age = age

    def speak(self):
        print('Meow')

class Dog:
    def __init__(self, name, age):
        self.name = self.name
        self.age = age

    def speak(self):
        print('Bark')

# with inheritence
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} of {self.age} age')

    def speak(self):
        print('i dont know what to speak') # this will be overwritten in child if implemented

class Cat(Pet):
    def speak(self):
        print('Meow')

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f'I am {self.name} of {self.age} age and of {self.color} color')

c = Cat('catname', 2)
d = Dog('dogname', 4)

c.show()
d.show()
c.speak()
d.speak()

f = Fish('fishname', 5, 'blue')
f.speak()
f.show()