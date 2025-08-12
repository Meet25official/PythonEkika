# 11.1. Output Formatting

# reprlib module (repr())

"""
import reprlib
print(reprlib.repr(set('asdfghjkzvxvbnmkytgdgfhetiyqyrctunzv')))

"""

# pprint module

"""
import pprint
t = [[[['black', 'cyan'], 'white',['green', 'red']],[['magenta', 'yellow'], 'blue']]]
print(pprint.pprint(t, width=30))

"""

#textwrap module

"""
import textwrap
doc = '''The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines.'''
print(textwrap.fill(doc, width=40))

"""

# locale module

"""
import locale
local = locale.setlocale(locale.LC_ALL, '')
print(local)


x = 1234567.8
conv = locale.localeconv()
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))


print(locale.format_string("%d", x, grouping=True))

"""


# 11.2. Templating

# string module using Template class

"""
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

"""
# substitute() method raises a KeyError and safe_substitute() method 

"""
from string import Template

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# print(t.substitute(d))
print(t.safe_substitute(d))


import time, os.path

photofiles = ['img_1011.jpg', 'img_1012.jpg', 'img_1013.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')

for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

"""

# 11.3 Workig with Binary Data Record Layouts

"""
import struct
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start +=16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size
"""

# 11.4 Multi-threading

"""
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()
print('Main program waited until background was done.')
"""


"""
import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}")
    time.sleep(delay)
    print(f"crawl ended for {link}")

links = ["https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",]

threads = []
for link in links:
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 5})
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

"""

"""
import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()
    
threading.Thread(target=worker, daemon=True).start()

for item in range(30):
    q.put(item)

q.join()
print('All work completed')
"""

# 11.5 Logging module

"""
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

"""

# 11.6 Weak References

"""
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
gc.collect()

d['primary']
"""

# 11.7 Tools for Working with Lists

"""
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])
"""


"""
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
"""

"""
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)
"""

"""
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5) 
print([heappop(data) for i in range(3)])
"""

# 11.8 Decimal Floating-Point Arithmetic

"""
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))

print(Decimal('1.00') % Decimal('.10'))

1.00 % 0.10

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
"""

"""

from decimal import *
getcontext().prec = 36
print(Decimal(1) / Decimal(7))

"""