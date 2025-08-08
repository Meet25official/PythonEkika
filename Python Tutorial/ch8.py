Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

Please enter a number: 45
except (RuntimeError, TypeError, NameError):
...     pass
SyntaxError: invalid syntax
class B(Exception):
    pass

class C(B):
    pass

class D(c):
    pass

Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#7>", line 1, in <module>
NameError: name 'c' is not defined. Did you mean: 'C'?
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

        
B
C
D
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    
    print(inst.args)     
    print(inst)         
    x, y = inst.args    
    print('x =', x)
    print('y =', y)

    
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

        
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#15>", line 1, in <module>
NameError: name 'sys' is not defined
def this_fails():
    x = 1/0

    
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

    
Handling run-time error: division by zero
def bool_return():
    try:
        return True
    finally:
        return False

    
bool_return()
False
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

        
divide(2,1)
result is 2.0
executing finally clause
divide(2,0)
division by zero!
executing finally clause
for line in open("myfile.txt"):
    print(line, end="")

    
my file
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

        
my file
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
f()
SyntaxError: invalid syntax
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')

    
caught <class 'TypeError'>: e
>>> def f():
...     raise ExceptionGroup(
...         "group1",
...         [
...             OSError(1),
...             SystemError(2),
...             ExceptionGroup(
...                 "group2",
...                 [
...                     OSError(3),
...                     RecursionError(4)
...                 ]
...             )
...         ]
...     )
... 
>>> try:
...     f()
... except* OSError as e:
...     
SyntaxError: invalid syntax
>>> excs = []
... for test in tests:
...     try:
...         test.run()
...     except Exception as e:
...         excs.append(e)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> if excs:
...    raise ExceptionGroup("Test Failures", excs)
... 
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#50>", line 1, in <module>
NameError: name 'excs' is not defined
