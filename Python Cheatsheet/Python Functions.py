# Basic
"""
def hello_world():
    print('hello')
"""

# Return
"""
def add(x, y):
    print("x is %s, y is %s" %(x, y))
    return print(x + y)
add(5, 6)
"""

# Positional arguments
"""
def varargs(*args):
    return print(args)
varargs(1, 2, 3)
"""

# keyword arguments
"""
def keyword_args(**kwargs):
    return print(kwargs)
keyword_args(big = 'foot', loch = 'ness')
"""

# Returning nultiple
"""
def swap(x, y):
    return y, x
x = 1
y = 2
x, y = swap(x, y)

print(x, y)
"""

# Default Value
"""
def add(x, y = 10):
    return print(x + y)
add(5)
add(5, 20)
"""

# Anonymous functions
"""
print((lambda x: x > 2)(3))
print((lambda x, y: x ** 2 + y ** 2)(2, 1))
"""