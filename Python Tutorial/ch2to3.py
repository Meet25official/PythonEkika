Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not fall off!")

    
Be careful not fall off!

spam = 1
text = "# This is not a comment because it's inside quotes."
text()
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#7>", line 1, in <module>
TypeError: 'str' object is not callable
text
"# This is not a comment because it's inside quotes."
2 + 2
4
50 - 5*6
20
(50 - 5*6) / 4
5.0
8 / 5
1.6
17 / 3
5.666666666666667
17 // 3
5
17 % 3
2
5 * 3 + 2
17
5 ** 2
25
2 ** 7
128
width = 20
height = 5 * 9
width * height
900
4 * 3.75 - 1
14.0
tax = 12.5 / 100
price = 100.50
price * tax
12.5625
price + _
113.0625
round(_, 2)
113.06
'spam eggs'
'spam eggs'
"spam eggs"
'spam eggs'
'2002'
'2002'
'doesn\'t'
"doesn't"
"doesn't"
"doesn't"
'"Yes," they said.'
'"Yes," they said.'
"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'
s = 'first line.\nSecond line.'
s
'first line.\nSecond line.'
print(s)
first line.
Second line.
print('C:\some\name')
C:\some
ame
print(r'C:\some\name')
C:\some\name
print("""\
Usage: thingy [OPTIONS]
    -h                      Display this usage message
    -H hostname             Hostname to connect to
""")
Usage: thingy [OPTIONS]
    -h                      Display this usage message
    -H hostname             Hostname to connect to

3 * 'un' + 'ium'
'unununium'
'py' 'thon'
'python'
text = ('Put several strings within parntheses '
        'to have them joined together.')
text
'Put several strings within parntheses to have them joined together.'
print(text)
Put several strings within parntheses to have them joined together.
prefix = 'Py'
prefix + 'thon'
'Python'
word = 'Python'
word[0]
'P'
word[5]
'n'
word[-1]
'n'
word[-2]
'o'
word[-6]
'P'
word[0:2]
'Py'
word[2:5]
'tho'
word[:2]
'Py'
word[4:]
'on'
word[-2:]
'on'
word[:2] + word[2:]
'Python'
word[:4] + word[4:]
'Python'
word[4:] + word[:4]
'onPyth'
word[4:42]
'on'
word[42:]
''
'J' + word[1:]
'Jython'
'J' + word[2:]
'Jthon'
>>> word[:2] + 'py'
'Pypy'
>>> word[:4] + 'py'
'Pythpy'
>>> s = 'qwertyuiopasdfghjklzxcvbnmqwfgnihgc'
>>> len(s)
35
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cubes = [1, 8, 27, 65, 125]
>>> 4 ** 3
64
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)
>>> cubes.append(7 ** 3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)
True
>>> rgba.append("Alph")
>>> rgb
['Red', 'Green', 'Blue', 'Alph']
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
['Red', 'Green', 'Blue', 'Alpha']
rgba
['Red', 'Green', 'Blue', 'Alph']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
letters[:] = []
letters
[]
letters = ['a', 'b', 'c', 'd']
len(letters)
4
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a,n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]
'b'
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

    
0
1
1
2
3
5
8
i = 256*256
print('The value of i is', i)
The value of i is 65536
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

    
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
