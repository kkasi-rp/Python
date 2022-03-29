from functools import wraps

def log_params(func):
    func.props = 'adding function properties'
    @wraps(func) # retain original function properties
    def wrapper(a,b):
        print('Args : ', a,b)
        a = 100
        val = func(a,b)
        return val
    return wrapper

@log_params
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

print('Method :', sum.__name__)
output = sum(10,20)
print('Output :', output)

sub = log_params(sub) # decorator invocation as function argument
print('Method :', sub.__name__)
output = sub(10,20)
print('Output :', output)
print(sub.props)
