

class Heap:
    def __init__(self):
        self.heap_list = [-1]
    def insert(self, ele):
        self.heap_list.append(ele)
        
        idx = len(self.heap_list) - 1
        parent = idx //2
        print("parent is",parent)
        print("idx is",idx)
        print(self.heap_list[idx])
        while (idx>1 and self.heap_list[parent]> self.heap_list[idx] ):
            self.heap_list[parent],self.heap_list[idx] = self.heap_list[idx], self.heap_list[parent]
            
            idx=parent
            parent = idx//2
            
            
my_heap = Heap()

# Insert values into the heap
my_heap.insert(5)
my_heap.insert(3)
my_heap.insert(7)
my_heap.insert(1)
my_heap.insert(9)

# Print the heap to see the result
print(my_heap.heap_list)