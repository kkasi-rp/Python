from copy import copy, deepcopy

old = [1,2,3]
new = old
print(old,new)
new[1] = 22
print(old,new) # notice change of value in old 

old = [1,2,3,['abc']]
new = copy(old)
print(old, new)
new[2] = 33
new[3][0] = 'xyz'
print(old, new) # mutable objects (having references) will get changed in both places

old = [1,2,3,['abc']]
new = deepcopy(old)
print(old, new)
new[2] = 33
new[3][0] = 'xyz'
print(old, new)

