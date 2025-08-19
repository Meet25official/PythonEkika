# Defining
"""
class MyNewClass:
    pass
my = MyNewClass()
"""

# Constructors
"""
class Animal:
    def __init__(self, voice):
        self.voice = voice
cat = Animal('meow')
print(cat.voice)

dog = Animal('woof')
print(dog.voice)
"""

# Method
"""
class Dog:
    def bark(self):
        print("Ham - Hum")

charlie = Dog()
charlie.bark()
"""

# Class Variables
"""
class MyClass:
    class_variable = "A class variable!"

print(MyClass.class_variable)

x = MyClass()

print(x.class_variable)
"""

# Super() Function
"""
class ParentClass:
    def print_test(self):
        print("Parent method")

class childClass(ParentClass):
    def print_test(self):
        print("Child Method") 
        super().print_test()
child_instance = childClass()
child_instance.print_test()
"""

# repr() method
"""
class Employee:
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return self.name
 
meet = Employee('Meet')
print(meet)  
"""

# Polymorphism
"""
class ParentClass:
    def print_self(self):
        print('A')

class ChildClass(ParentClass):
    def print_self(self):
        print("B")

obj_A = ParentClass()
obj_B = ChildClass()

obj_A.print_self()
obj_B.print_self()
"""

# overriding
"""
class ParntClass:
    def print_self(self):
        print("Parent")

class ChildClass(ParntClass):
    def print_self(self):
        print("Child")

child_instance = ChildClass()
child_instance.print_self()
"""

# Inheritance
"""
class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

class Dog(Animal):
    def sound(self):
        print("woof")

Yoki = Dog("Yoki", 4)
print(Yoki.name)
print(Yoki.legs)
Yoki.sound()
"""