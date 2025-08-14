"""
Top N Frequent Elements

Problem
Write top_n_frequent(lst, n) to return top n most frequent items.

Example
top_n_frequent(['x', 'y', 'x', 'z'], 2)
# Output: [('x', 2), ('y', 1)]
"""

def top_n_frequent(lst, n):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    def count(pair):
        return pair[1]
    sorted_items = sorted(freq.items(), key=count, reverse=True)
    return sorted_items[:n]

print(top_n_frequent(['x', 'y', 'x', 'z'], 2))


