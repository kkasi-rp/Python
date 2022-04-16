class Base:
    def base_method(self):
        print('called in base method')

class Child(Base):
    x = 10
    def child_method(self):
        print('called in child method')

c = Child()
print(c.__class__)
print(c.__class__.__name__)
print(Child.__name__)
print(Child.__bases__)
print(Child.__dict__)
print()

def child_method(self):
    print('called in child method')

def init_function(self, x):
    self.x = x

# defining Child class using type
# Kindly note : (Base,) is tuple
Child = type('Child', (Base,), {'__init__': init_function, 'x':1000, 'child_method': child_method})

print(Child.__name__)
print(Child.__bases__)
print(Child.__dict__)

child_obj = Child(15)
print(child_obj.x)