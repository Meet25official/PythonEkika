"""
Flatten a Deeply Nested List

Problem
Write a function flatten_list(nested_list) that flattens an arbitrarily nested list into a single-level list.

Example
flatten_list([1, [2, 3], [4, [5, 6], 7]])
# Output: [1, 2, 3, 4, 5, 6, 7]

"""

def flatten_list(nested_list):
    flat = []
    for i in nested_list:
        if isinstance(i, list):
            flat.extend(flatten_list(i))
        else:
            flat.append(i)
    return flat

print(flatten_list([1, [2, 3], [4, [5, 6], 7]]))