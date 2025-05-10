# import queue

# q = queue.Queue()

# q.put(1)
# q.put(2)
# q.put(5)
# q.put(4)

# print("Queue size:", q.qsize())
# print("Queue empty:", q.empty())
# print("Queue full:", q.full())
# print("Queue elements:")

     
# print(q) #<queue.Queue object at 0x00000229C3213B50>
# print(q.queue) #deque([1, 2, 5, 4])
# print(list(q.queue)) # [1, 2, 5, 4]
# print(q.queue[0]) #1

# while not q.empty():
#     print(q.get())  #get method removes and returns an item from the queue
    
    
# print(q.queue[0]) #this will give you error as queue is empty now
    
import sys
print(sys.platform)