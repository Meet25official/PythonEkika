Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
x = int(input("Enter an integer: "))
Enter an integer: 42
if x < 0;
SyntaxError: incomplete input
if x < 0:
    x = 0
    print("Negative chaged to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print("More")

    
More
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

    
cat 3
window 6
defenestrate 12
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

        
active_users = {}
for user, status == 'active':
    
SyntaxError: invalid syntax
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

        
for i in range(5):
    print(i)

    
0
1
2
3
4
list(range(5, 10))
[5, 6, 7, 8, 9]
list(range(0, 10, 3))
[0, 3, 6, 9]
list(range(-10, -100, -30))
[-10, -40, -70]
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a))
SyntaxError: incomplete input
for i in range(len(a)):
    print(i, a[i])

    
0 Mary
1 had
2 a
3 little
4 lamb
range(10)
range(0, 10)
sum(range(4))
6
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

        
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

    
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

        
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
while True:
    pass

Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#62>", line 1, in <module>
KeyboardInterrupt
class MyEmptyClass:
    pass

def initlog(*args):
    pass

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

        
case 401 | 403 | 404:
    
SyntaxError: invalid syntax
KeyboardInterrupt
case 401 | 403 | 404:
    
SyntaxError: invalid syntax
case 401 | 403 | 404:
    return "Not allowed"
SyntaxError: invalid syntax
case 400 | 403 | 404:
    return "Not allowed"
SyntaxError: invalid syntax
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

    
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#95>", line 1, in <module>
NameError: name 'point' is not defined. Did you mean: 'print'?
class Point:
    def_init__(self, x, y):
        
SyntaxError: incomplete input
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

            
Point(1, var)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#116>", line 1, in <module>
NameError: name 'var' is not defined. Did you mean: 'vars'?
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

        
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#129>", line 1, in <module>
NameError: name 'points' is not defined. Did you mean: 'Point'?
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
        
SyntaxError: expected an indented block after 'match' statement on line 6
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

    
fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
fib
<function fib at 0x7c0819181750>
f = fib
f(100)
0 1 1 2 3 5 8 13 21 34 55 89 
fib(0)

print(fib(0))

None
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
f100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

        
i = 5
def f(arg=i):
    print(arg)

    
i = 6
f()
5
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
[1]
print(f(2))
[1, 2]
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
[1]
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm Sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
-- Do you have any Limburger ?
-- I'm Sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
def standard_arg(arg):
    print(arg)

    
def pos_only_arg(arg, /):
    print(arg)

    
def kwd_only_arg(*, arg):
    print(arg)

    
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

    
standard_arg(2)
2
standard_arg(arg=2)
2
pos_only_arg(1)
1
pos_only_arg(arg=1)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#217>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
kwd_only_arg(arg=3)
3
combined_example(1, 2, kwd_only=3)
1 2 3
combined_example(1, standard=2, kwd_only=3)
1 2 3
def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
True
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
list(range(3, 6))
[3, 4, 5]
args = [3, 6]
list(range(*args))
[3, 4, 5]
def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
... 
...     
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
>>> def make_incrementor(n):
...     return lambda x: x + n
... 
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return hum + ' and ' + eggs
... 
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#247>", line 1, in <module>
  File "<pyshell#246>", line 4, in f
NameError: name 'hum' is not defined. Did you mean: 'ham'?
