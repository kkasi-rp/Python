from functools import wraps

def decoParam(*dargs, **dkwargs):
	print('called in decoParam')
	def decorator(func):
		print('called in decorator')
		# closure function with dargs, dkwargs values stored for usage
		@wraps(func)
		def wrapper(*args, **kwargs):
			print('called in wrapper')
			print(dargs, dkwargs)
			print(args, kwargs)
			return func(*args, **kwargs)
		return wrapper
	return decorator

class Simple(object):
	@decoParam(10, 20, **{'a':100})
	def method(self, *args, **kwargs):
		return 'Static in Method'

p = Simple()
print(p.method(11, 21, {'a':111}))

# <bound method decoParam.<locals>.decorator.<locals>.wrapper of <__main__.Simple object at 0x000002B5770327C0>>
# with @wraps(func)
# <bound method Simple.method of <__main__.Simple object at 0x051B24D0>>
print(p.method) 