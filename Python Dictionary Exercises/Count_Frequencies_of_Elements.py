"""
Count Frequencies of Elements

Problem
Write a function freq_map(lst) that returns frequency of elements in a list using a dictionary.

Example
freq_map(['a', 'b', 'a'])
# Output: {'a': 2, 'b': 1}
"""
def freq_map(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(freq_map(['a', 'b', 'a']))
