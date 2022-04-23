#### closures in python
#### https://www.geeksforgeeks.org/python-closures/
#### https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures

import time

# nested function
def outer(value):
	def inner():
		print(value)
	inner()

# outer('text')

# closures
def outer(value):
	def inner():
		time.sleep(3)
		print('called in inner')
		print(value)
	print('called in outer')
	return inner

inn = outer('text')
inn()
