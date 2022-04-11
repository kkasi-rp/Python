class Base:
    def base_method(self):
        print('called in base method')

class Child(Base):
    x = 10
    def child_method(self):
        print('called in child method')

c = Child()
print(c.__class__.__name__)
print(Child.__name__)
print(Child.__bases__)
print(Child.__dict__)
print()

def child_method(self):
    print('called in child method')

# defining Child class using type
# Kindly note : (Base,) is tuple
Child = type('Child', (Base,), {'x':10, 'child_method': child_method})

print(Child.__name__)
print(Child.__bases__)
print(Child.__dict__)