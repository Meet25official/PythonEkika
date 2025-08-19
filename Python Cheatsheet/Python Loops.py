# Basic
"""
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
"""

# with index
"""
animals = ['dog', 'cat', 'mouse']
for i, value in enumerate(animals):
    print(i, value)
"""

# while
"""
x = 0
while x < 4:
    print(x)
    x += 1
"""

# Brack
"""
x = 0
for index in range(10):
    x = index * 10
    if index == 5:
        break
    print(x)
"""

# continue
"""
for index in range(3, 8):
    x = index * 10
    if index == 5:
        continue
    print(x)
"""

# Range
"""
for i in range(4):
    print(i)
for i in range(4, 8):
    print(i)
for i in range(4, 10, 2):
    print(i)
"""

# With zip()
"""
words = ['Mon', 'Tue', 'Wed']
nums = [1, 2, 3]
for w, n in zip(words, nums):
    print('%d:%s, ' %(n, w))
"""

# for/else
"""
num = [60, 70, 30, 110, 90]
for n in num:
    if n > 100:
        print("%d is bigger than 100" %n)
        break
else:
    print("Not found!")
"""