class Parent:
    def __init__(self, a, b):
        self.a = a
        self.__b = b

    def get__b(self):
        return self.__b

p = Parent(1, 2)
print(p.a)
print(p.get__b())

# print(p.__b) # AttributeError: 'Parent' object has no attribute '__b'
print(p.__dict__)
print(p._Parent__b)
