"""
Invert a Dictionary (Simple)

Problem
Write a function invert_dict(d) that swaps keys and values.

Example
invert_dict({'a': 1, 'b': 2})
# Output: {1: 'a', 2: 'b'}
"""

def invert_dict(d):
    invert = {}
    for key, value in d.items():
        invert[value] = key
    return invert

print(invert_dict({'a': 1, 'b': 2}))