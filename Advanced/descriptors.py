class Descriptor(object):
	def __init__(self, value='default value'):
		self.value = value

	def __get__(self, obj, objType):
		print('called in Descriptor get')
		print (obj, objType)
		return self.value

	def __set__(self, obj, value):
		print('called in Descriptor set')
		self.value = value

class Temp(object):
	a = Descriptor()

t = Temp()
print(t.a)
t.a = 20