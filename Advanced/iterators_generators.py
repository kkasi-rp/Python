# %% Generators 

def square_numbers(numbers):
	result = []
	for num in numbers:
		result.append(num*num)
	return result

numbers = [1,2,3]
result = square_numbers(numbers)
print(result)

def square_numbers(numbers):
	for num in numbers:
		yield num*num

result = square_numbers(numbers)
print(result)

print(next(result))
print(next(result))
print(next(result))
# print(next(result)) # Exception : StopIteration

numbers = [1,2,3]
result = [num*num for num in numbers]
print(result)

result = (num*num for num in numbers)
print(result)

for num in result:
	print(num)

# %% Iterables : __iter__()

nums = [1,2,3] # list is iterable and not iterator
print(dir(nums))
print()

# print(next(nums)) # TypeError: 'list' object is not an iterator
i_nums = nums.__iter__() # returns iterator
print(i_nums)
print()

# iterators : __next__() 
# iterators are also iterables, object with a state which remember next value
# __iter__() & __next__()
print(dir(i_nums)) 
print(next(i_nums))
print()

nums = [1,2,3]
i_nums = iter(nums) # same as nums.__iter__()
while True:
	try:
		item = next(i_nums)
		print(item)
	except StopIteration:
		break

# %%
class MyRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end

	# iterable : has to return iterator (__next__())
	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current = self.value
		self.value +=1
		return current

nums = MyRange(1,6)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

# %%
# Generator function 

def my_range(start, end):
	current = start
	while current < end:
		yield current
		current += 1

nums = my_range(1, 10)
for num in nums:
	print(num)

# %%
