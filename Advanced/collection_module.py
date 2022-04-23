from collections import Counter

map = Counter(['a','b','a','c','b','d','b'])
print(dir(map))
print()
print(map)
print(map.keys(), map.values())

from collections import OrderedDict

dct = OrderedDict()
dct['b'] = 1
dct['a'] = 3
dct['d'] = 2
dct['c'] = 4

print(dct)
dct.pop('a')
print(dct)
dct['a']=111
print(dct)

from collections import defaultdict
dct = defaultdict(int)

dct['a'] = 'string'
print(dct)

from collections import namedtuple
student = namedtuple('Student', ['name', 'age'])
stu = student('purvi', '10')
print(stu[0],stu[1])
print(stu.name, stu.age)