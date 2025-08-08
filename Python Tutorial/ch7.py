Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
'Results of the 2016 Referendum'
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
s = 'Hello, world.'
str(s)
'Hello, world.'
repr(s)
"'Hello, world.'"
str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
The value of x is 32.5, and y is 40000...
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
'hello, world\n'
repr((x,y,('spam','eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

    
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs= } {count= } {area= }')
Debugging bugs= 'roaches' count= 13 area= 'living room'
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: <class '_frozen_importlib.BuiltinImporter'>; __spec__: None; __annotations__: {}; __builtins__: <module 'builtins' (built-in)>; year: 2016; event: Referendum; yes_votes: 42572654; total_votes: 85705149; percentage: 0.496733912684756; s: The value of x is 32.5, and y is 40000...; x: 32.5; y: 40000; hello: hello, world
; hellos: 'hello, world\n'; math: <module 'math' (built-in)>; table: {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}; name: Dcab; phone: 7678; animals: eels; bugs: roaches; count: 13; area: living room;
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
... 
...     
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
>>> import math
>>> print('The value of pi is approximately %5.3f.'% math.pi)
The value of pi is approximately 3.142.
>>> f = open('workfile', 'w', encoding="utf-8")
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()
... 
...     
>>> f.closed
True
>>> f.read()
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#57>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
