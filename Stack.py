# Stack
from collections import deque
q = deque()
print("This is Stack and it work on Last in First Out: ")
q = ["hello","how"]
print(q)
print("Appending first element: ")
q.append('are')
print(q)
print("Appending second element: ")
q.append('you?')
print(q)
print("Removing elements from last: ")
q.pop()
print(q)
print("Removing elements from last: ")
q.pop()
print(q)