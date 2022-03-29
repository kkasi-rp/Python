def deco(func):
    print('called in decorator for method : {}'.format(func.__name__))
    def wrapper(*args, **kwargs):
        print('called in wrapper for method : {}'.format(func.__name__))
        funcout = func(*args, **kwargs)
        print(funcout)
        return funcout
    return wrapper

def class_deco(cls):
    for key, value in vars(cls).items():
        if callable(value):
            setattr(cls, key, deco(value))
    return cls

@class_deco
class Simple():
    def method1(self):
        return 'method1'
    def method2(self):
        return 'method2'

simple_obj = Simple()
simple_obj.method2()