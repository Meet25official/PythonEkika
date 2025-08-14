"""
List Difference (Ordered & Counted)

Problem
Write a function diff_lists(a, b) that removes one matching element in b for each occurrence found in a, preserving order.

Example
diff_lists([1, 2, 2, 3, 4], [2, 4])
# Output: [1, 2, 3]
"""

def diff_lists(a, b):
    b = b.copy()
    new_lst = []
    for i in a:
        if i in b:
            b.remove(i)
        else:
            new_lst.append(i)
    return new_lst

print(diff_lists([1, 2, 2, 3, 4], [2, 4]))