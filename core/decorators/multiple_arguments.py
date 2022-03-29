from functools import wraps

def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@print_args
def dummy(*args, **kwargs):
    pass

dummy(10)
dummy(name='Test')
dummy(10,20, name='Test', age=100)