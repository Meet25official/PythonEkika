Python 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

        
for char in reverse('golf'):
    print(char)

    
f
l
o
g
sum(i*i for i in range(10))
285
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))
260
import os
dir(os)

help(os)

import os
os.getcwd()
'/home/meet'
os.chdir('/server/accesslogs')
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#16>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/server/accesslogs'
os.system('mkdir today')
0
import glob
glob.glob('*.py')
['fibo.py']
import sys
print(sys.argv)
['']
import argparse
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(prog='top',\)
                                 
SyntaxError: unexpected character after line continuation character
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
                                 
parser.add_argument('filenames', nargs='+')
                                 
_StoreAction(option_strings=[], dest='filenames', nargs='+', const=None, default=None, type=None, choices=None, required=True, help=None, metavar=None)
parser.add_argument('-l', '--lines', type=int, default=10)
                                 
_StoreAction(option_strings=['-l', '--lines'], dest='lines', nargs=None, const=None, default=10, type=<class 'int'>, choices=None, required=False, help=None, metavar=None)
args=parser.parse_args()
                                 
usage: top [-h] [-l LINES] filenames [filenames ...]
top: error: the following arguments are required: filenames
print(args)
                                 
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#31>", line 1, in <module>
NameError: name 'args' is not defined
sys.stderr.write('Warning, log file not found starting a new one\n')
                                 
Warning, log file not found starting a new one
47
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
'tea for too'.replace('too','two')
'tea for two'
import random
random.choice(['apple', 'pear', 'banana'])
'pear'
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
1.6071428571428572
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())

            
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#43>", line 1, in <module>
  File "/usr/lib/python3.10/urllib/request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.10/urllib/request.py", line 519, in open
    response = self._open(req, data)
  File "/usr/lib/python3.10/urllib/request.py", line 536, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "/usr/lib/python3.10/urllib/request.py", line 496, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.10/urllib/request.py", line 1377, in http_open
    return self.do_open(http.client.HTTPConnection, req)
  File "/usr/lib/python3.10/urllib/request.py", line 1352, in do_open
    r = h.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1375, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 279, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/usr/lib/python3.10/socket.py", line 705, in readinto
    return self._sock.recv_into(b)
ConnectionResetError: [Errno 104] Connection reset by peer
import smtplib
server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#45>", line 1, in <module>
  File "/usr/lib/python3.10/smtplib.py", line 255, in __init__
    (code, msg) = self.connect(host, port)
  File "/usr/lib/python3.10/smtplib.py", line 341, in connect
    self.sock = self._get_socket(host, port, self.timeout)
  File "/usr/lib/python3.10/smtplib.py", line 312, in _get_socket
    return socket.create_connection((host, port), timeout,
  File "/usr/lib/python3.10/socket.py", line 845, in create_connection
    raise err
  File "/usr/lib/python3.10/socket.py", line 833, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#46>", line 1, in <module>
NameError: name 'server' is not defined
from datetime import date
now = date.today()
now
datetime.date(2025, 8, 6)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'08-06-25. 06 Aug 2025 is a Wednesday on the 06 day of August.'
birthday = date(2002, 12, 25)
age = now - birthday
age.days
8260
import zlib
s=b'witch which has which witches wrist watch'
len(s)
41
t = zlib.compress(s)
len(t)
37
lib.decompress(t)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#59>", line 1, in <module>
NameError: name 'lib' is not defined. Did you mean: 'zlib'?
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.02724716900047497
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.02917383699968923
>>> def average(values):
...     """Computes the arithmetic mean of a list of numbers.
... 
...     >>> print(average([20, 30, 70]))
...     40.0
...     """
...     return sum(values) / len(values)
... 
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=1)
>>> import unittest
>>> class TestStatisticalFunctions(unittest.TestCase):
... 
...     def test_average(self):
...         self.assertEqual(average([20, 30, 70]), 40.0)
...         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
...         with self.assertRaises(ZeroDivisionError):
...             average([])
...         with self.assertRaises(TypeError):
...             average(20, 30, 70)
... 
...             
>>> unittest.main()
.
----------------------------------------------------------------------
Ran 1 test in 0.028s

OK
