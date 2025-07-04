#there are three types of queues in python
# 1. queue.Queue (thread-safe, blocking) as its blocking in nature, its slower than deque, use this when you need thread-safety (consumer-producer model)
# 2. collections.deque (non-blocking, faster for single-threaded use)(use for  data processing, BFS, sliding window problems, etc.)
# 3. using list as a queue (not recommended for large data sets due to performance issues)(use for small data sets or simple use cases)

#queue.Queue usage example
import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(5)
q.put(4)

print("Queue size:", q.qsize())
print("Queue empty:", q.empty())
print("Queue full:", q.full())
print("Queue elements:")

     
print(q) #<queue.Queue object at 0x00000229C3213B50>
print(q.queue) #deque([1, 2, 5, 4])
print(list(q.queue)) # [1, 2, 5, 4]
print(q.queue[0]) #1

while not q.empty():
    print(q.get())  #get method removes and returns an item from the queue
# print(q.queue[0]) #this will give you error as queue is empty now


#collections.deque usage example
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(5)
d.append(4)
print("\nDeque size:", len(d))
print("Deque elements:", d)
while d:
    print(d.popleft())  #popleft method removes and returns an item from the left end of the deque
    
#lets say you got a situation where you need to store the queue item in following order: ((1,2),3)
#to handle this you can use the following code

dq = deque([((1, 2), 3)])
(r, c), t = dq.popleft()

print(r)  # 1
print(c)  # 2
print(t)  # 3

    
    
# Using list as a queue (not recommended for large data sets)
l = []
l.append(1) # append adds an item to the end of the list
l.append(2)
l.append(5)
l.append(4)
print("\nList size:", len(l))
print("List elements:", l)
while l:
    print(l.pop(0))  # pop(0) removes and returns the first item from the list, strictly give 0 # as index, as it will remove the first item from the list
# Note: Using pop(0) on a list is inefficient for large lists as it requires shifting all other elements
    
