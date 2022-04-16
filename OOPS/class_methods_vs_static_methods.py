# class methods 

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def create_person(cls, name):
        if name not in ['KK','Pushpa', 'Purvi', 'Ruthvik']:
            raise ValueError
        return cls(name)

    @classmethod
    def get_people_count(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('KK')
p2 = Person('Pushpa')
p3 = Person.create_person('Purvi')
# p4 = Person.create_person('Test') # ValueError
print(Person.get_people_count())
print(p1.get_people_count())

# static methods 
# no class or instance will be passed
# more of code organisation
# used for helper methods

class Math:
    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def sub(x,y):
        return x-y

print(Math.add(10, 20))
print(Math.sub(10, 20))