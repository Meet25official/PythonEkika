"""
Merge Dictionaries with Conflict Resolution

Problem
Write merge_dicts(a, b) where b overrides values in a.

Add a mode argument:

'override' (default): b overwrites a.
'sum': if values are numeric, sum them.
'append': create lists for conflicting keys.

Example
merge_dicts({'x': 2}, {'x': 3}, mode='sum')
# Output: {'x': 5}
"""

def merge_dicts(a, b, mode):
    res = a.copy()
    for key in b:
        if key not in res:
            res[key] = b[key]
        else:
            if mode == 'override':
                res[key] = b[key]
            elif mode == 'sum':
                if isinstance(res[key],(int, float)) and isinstance(b[key],(int, float)):
                    res[key] += b[key]
                else:
                    res[key] = b[key]
            elif mode == 'append':
                if not isinstance(res[key],list):
                    res[key] = [res[key]]
                res[key].append(b[key])
            else:
                res[key] = b[key]
    return res

print(merge_dicts({'x': 2}, {'x': 3}, mode='override'))
print(merge_dicts({'x': 2}, {'x': 3}, mode='sum'))
print(merge_dicts({'x': 2}, {'x': 3}, mode='append'))