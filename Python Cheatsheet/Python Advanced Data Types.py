# Heaps
"""
import heapq

myList = [9, 5, 4, 1, 3, 2]
heapq.heapify(myList) 
print(myList)    
print(myList[0]) 

heapq.heappush(myList, 10) 
x = heapq.heappop(myList)  
print(x)  
"""     

# Negate all values to use Min Heap as Max Heap

"""
myList = [9, 5, 4, 1, 3, 2]
myList = [-val for val in myList] 
heapq.heapify(myList)

x = heapq.heappop(myList)
print(-x)
"""

# Stacks and Queues

"""
from collections import deque

q = deque()
q = deque([1, 2, 3])

q.append(4)
q.appendleft(0)
print(q)

x = q.pop()
y = q.popleft()

print(x)
print(y)
print(q)

q.rotate(1)
print(q)
"""