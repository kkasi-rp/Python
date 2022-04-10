class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person('KK')
p2 = Person('Pushpa')

print(f'Person.number_of_people : {Person.number_of_people}')
print(f'p1.number_of_people : {p1.number_of_people}')
print(f'p2.number_of_people : {p2.number_of_people}')
print()
Person.number_of_people = 1
print(f'Person.number_of_people : {Person.number_of_people}')
print(f'p1.number_of_people : {p1.number_of_people}')
print(f'p2.number_of_people : {p2.number_of_people}')
print()
p2.number_of_people = 10
print(f'Person.number_of_people : {Person.number_of_people}')
print(f'p1.number_of_people : {p1.number_of_people}')
print(f'p2.number_of_people : {p2.number_of_people}')
