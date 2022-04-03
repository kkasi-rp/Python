import random

# numbers = range(1,11)

def get_random_number():
    return random.randint(1, 11)

for _ in range(10):
    number = get_random_number()
    print(number)