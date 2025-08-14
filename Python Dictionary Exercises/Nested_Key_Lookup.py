"""
Nested Key Lookup

Problem
Write nested_get(d, keys) where keys is a list like ['a', 'b', 'c'] that returns d['a']['b']['c'].

Example
nested_get({'a': {'b': {'c': 42}}}, ['a', 'b', 'c'])
# Output: 42
"""

def nested_get(d, keys):
    res = d
    for key in keys:
        if key in res:
            res = res[key]
        else:
            return None
    return res

print(nested_get({'a': {'b': {'c': 42}}}, ['a', 'b', 'c']))