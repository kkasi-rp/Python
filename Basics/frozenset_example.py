# frozenset
# https://www.geeksforgeeks.org/frozenset-in-python/
# https://stackoverflow.com/questions/36555214/set-vs-frozenset-performance

'''The frozenset() is an inbuilt function is Python which takes an iterable object as input 
and makes them immutable also by deleting duplicates.
Simply it freezes the iterable objects and makes them unchangeable.'''

s = set([1,1,2,2])
print(s, type(s)) # removes duplicates
s.add(10)
print(s)

ss = frozenset([1,1,2,2])
print(ss, type(ss)) # removes duplicates
print(dir(ss))

# frozenset can be used as dict key
d = {ss:1}
print(d)

tup = (1, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(tup))
out = frozenset(tup)
print(out)

# tup = (1, 1, [1,2,3], 3, 4, 5, 6, 7, 8, 9)
# out = frozenset(tup) # TypeError: unhashable type: 'list'

out = frozenset()
print(out, type(out))