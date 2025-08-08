Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.count('tangerine')
0
fruits.index('banana')
3
fruits.index('banana', 4)
6
fruits.reverse()
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
'pear'
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
7
stack
[3, 4, 5, 6]
stack.pop()
6
stack.pop()
5
stack
[3, 4]
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
'Eric'
queue.popleft()

'John'
queue
deque(['Michael', 'Terry', 'Graham'])
squares = []
for x in range(10):
    squares.append(x**2)

    
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = list(map(lambda x: x**2, range(10)))
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = [x**2 for x in range(10)]
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

            
combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[-8, -4, 0, 4, 8]
[x for x in vec if x >= 0]
[0, 2, 4]
[abs(x) for x in vec]
[4, 2, 0, 2, 4]
freshfruit = ['banana', 'loganberry', 'passion fruit']
[weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
vec = [[1,2,3],[4,5,6],[7,8,9]]
[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

    
transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

    
transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
[1, 66.25, 333, 333, 1234.5]
del a[2:4]
a
[1, 66.25, 1234.5]
del a[:]
a
[]
del a
t = 12345, 54321, 'hello!'
t[0]
12345
t
(12345, 54321, 'hello!')
u = t, (1, 2, 3, 4, 5)
u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
v = ([1,2,3], [3,2,1])
v
([1, 2, 3], [3, 2, 1])
empty = ()
singleton = 'hello',
len(empty)
0
len(singleton)
1
singleton
('hello',)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(backet)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#90>", line 1, in <module>
NameError: name 'backet' is not defined. Did you mean: 'basket'?
print(basket)
{'pear', 'apple', 'banana', 'orange'}
'orange' in basket
True
'crabgrass' in basket
False
a = set('abracadabra')
b = set('alacazam')
a
{'a', 'd', 'r', 'c', 'b'}
a-b
{'b', 'd', 'r'}
a|b
{'a', 'd', 'l', 'z', 'r', 'm', 'c', 'b'}
a&b
{'a', 'c'}
a^b
{'d', 'l', 'r', 'b', 'z', 'm'}
a = {x for x in 'abracadabra' if x not in 'abc'}
a
{'d', 'r'}
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
4098
del tel['sape']
tel['irv']= 4127
tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
['guido', 'irv', 'jack']
'guido' in tel
True
'jack' not in tel
False
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
{x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

    
gallahad the pure
robin the brave
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

    
0 tic
1 tac
2 toe
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

    
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
for i in reversed(range(1, 10, 2)):
    print(i)

    
9
7
5
3
1
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
... 
...     
apple
apple
banana
orange
orange
pear
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
... 
...     
apple
banana
orange
pear
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
... 
...         
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
