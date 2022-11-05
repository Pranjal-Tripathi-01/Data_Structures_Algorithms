# Queue
from queue import Queue
Q= Queue(maxsize=4)
queue = []
print("This is Queue and it work on First in First Out: ")
Q.put('hi')
Q.put('how')
Q.put('are')
Q.put('you?')
print("Is Queue is full?: ", Q.full())
print("Get first inserted element from Queue: ",Q.get())
print("Get second inserted element from Queue: ",Q.get())


