# Array-like

"""
hello = "Hello, World"

print(hello[1])
print(hello[-1])
"""

# looping

"""
for char in 'foo':
    print(char)
"""

# String Length

"""
hello = "hello, world!"
print(len(hello))
"""

# Multiple copies

"""
s = "===+"
n = 8
print(s*n)
"""

# Check String

"""
s = 'spam'
print(s in "i saw spamalot!")
print(s not in 'I saw The Holy Grail!')
"""

# Slicing string
"""
s = "myname"
print(s[2:5])
print(s[0:2])

print(s[:2])
print(s[2:])
print(s[:2] + s[2:])

print(s[-5:-1])
print(s[2:6])
"""

# With a stride

"""
s = '12345' * 5
print(s)

print(s[::5])
print(s[4::5])
print(s[::-5])
print(s[::-1])
"""

# Formatting

"""
name = "Meet"
print("Hello, %s!" % name)

name = "Meet"
age = 22
print("%s is %d years old." %(name, age))
"""

# format() Method

"""
txt1 = "My name is {fname}, I'm {age}.".format(fname="Meet", age=22)
print(txt1)

txt2 = "My name is {0}, I'm {1}.".format("Meet", 22)
print(txt2)

txt3 = "My name is {}, I'm {}.".format("Meet", 22)
print(txt3)
"""

# Input

"""
name = input("Enter your name: ")
print(name)
"""

# Join

"""
print("#".join(["Meet", "J", "Sarvaiya"]))
"""

# Endswith

"""
print("Hello, world!".endswith("!"))
"""