"""
Group Consecutive Duplicates

Problem
Write a function group_consecutive(lst) that groups only consecutive duplicate elements into sublists.

Example
group_consecutive([1, 1, 2, 2, 2, 3, 1, 1])
# Output: [[1, 1], [2, 2, 2], [3], [1, 1]]

"""

def group_consecutive(lst):
    if not lst:
        return []
    group = []
    curr_group = [lst[0]]
    for i in lst[1:]:
        if i == curr_group[-1]:
            curr_group.append(i)
        else:
            group.append(curr_group)
            curr_group = [i]
    group.append(curr_group)
    return group

print(group_consecutive([1, 1, 2, 2, 2, 3, 1, 1]))