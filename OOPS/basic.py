class Dog:

    def __init__(self,name):
        self.name=name
        print(self.name)

    def bark(self):
        print('bark')
    
    def add_one(self, x):
        return x+1


d = Dog('dobberman') # call to __init__
h = Dog('hutch') 
d.bark()
print(d.add_one(5))
print(type(d)) # module.classname