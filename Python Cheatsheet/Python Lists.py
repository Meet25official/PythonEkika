# Defining

"""
li1 = []
print(li1)

li2 = [4, 5, 6]
print(li2)

li3 = list((1, 2, 3))
print(li3)

li4 = list(range(1, 11))
print(li4)
"""

# Generate

"""
print(list(filter(lambda x : x % 2 == 1, range(1, 20))))

print([x ** 2 for x in range(1, 11) if x % 2 == 1])

print([x for x in [3, 4, 5, 6, 7] if x > 5])

print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))
"""

# Append

"""
li = []
li.append(1)
print(li)

li.append(2)
print(li)

li.append(4)
print(li)

li.append(3)
print(li)
"""

# List Slicing

# slicing
"""
a = ['spam', 'egg', 'tomato', 'hum', 'lobster']
print(a[2:5])
print(a[-5:-2])
print(a[1:4])
"""

# Omitting index
"""
a = ['spam', 'egg', 'tomato', 'hum', 'lobster']
print(a[:4])
print(a[0:4])
print(a[2:])
print(a[2:len(a)])
print(a)
print(a[:])
"""

# With a stride
"""
a = ['spam', 'egg', 'bacon', 'tomato', 'hum', 'lobster']
print(a[0:6:2])
print(a[1:6:2])
print(a[6:0:-2])
print(a)
print(a[::-1])
"""

# Remove
"""
li = ['bread', 'butter', 'milk']
print(li[0])
print(li[-1])
print(li[4])
"""

# Concatenating
"""
odd = [1, 3, 5]
odd.extend([9, 11, 13])
print(odd)

odd = [1, 3, 5]
li = odd + [9, 11, 13]
print(li)
"""

# Sort & Reverse
"""
li = [3, 1, 3, 2, 5]
li.sort()
print(li)

li.reverse()
print(li)
"""

# Count
"""
li = [3, 1, 3, 2, 5]
print(li.count(3))
"""

# Repeating
"""
li = ["re"] * 3
print(li)
"""