#bisect is a library that provides simple and fast(binary search based) functions to search an element in a sorted list.
#provides efficient methods to insert elements into a sorted list while maintaining order.
#avoids the need to manually sort the list after each insertion.

import bisect

li = [1, 3, 4, 4, 4, 6, 7] 

print(bisect.bisect(li, 4)) #returns the rightmost index where 4 would be inserted to maintain order here its 6
print(bisect.bisect_left(li, 4)) #returns the leftmost index where 4 would be inserted to maintain order here its 2
# bisect.insort() inserts an element into the list while maintaining sorted order