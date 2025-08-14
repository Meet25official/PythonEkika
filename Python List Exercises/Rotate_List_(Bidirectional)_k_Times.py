"""
Rotate List (Bidirectional) k Times

Problem
Write a function rotate_list(lst, k) that rotates the list right by k steps.

Support negative k to rotate left.

Example
rotate_list([1, 2, 3, 4, 5], 2)
# Output: [4, 5, 1, 2, 3]

rotate_list([1, 2, 3, 4, 5], -2)
# Output: [3, 4, 5, 1, 2]
"""

def rotate_list(lst, k):
    if not list:
        return[]
    n = len(lst)
    k %= n
    
    if k == 0:
        return lst[:]
    rotated = []

    for i in range(n - k, n):
        rotated.append(lst[i])

    for i in range(n - k):
        rotated.append(lst[i])

    return rotated

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], -2))
