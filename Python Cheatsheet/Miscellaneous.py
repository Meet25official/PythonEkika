# This is a single line comments.
""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""
''' Multiline strings can be written
    using three 's, and are often used
    as documentation.
'''

# Generators
"""
def double_numbers(iterable):
    for i in iterable:
        yield i + i
"""

# Generator to list
"""
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)

print(gen_to_list)
"""

# Handle exceptions

"""
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass
except (TypeError, NameError):
    pass
else:
    print("All good!")
finally:
    print("We can clean up resources here")
"""