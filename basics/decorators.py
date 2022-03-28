def log(func):
    def wrapper(a,b):
        print(a,b)
        a = 100
        val = func(a,b)
        return val
    return wrapper

@log
def sum(a,b):
    return a+b

print(sum.__name__)
output = sum(10,20)
print(output)

