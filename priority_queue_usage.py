#by default python implements min heap
#to implement max heap we can multiply the values by -1
import heapq

ans = [20,10,4,30,15,8,30]

heapq.heapify(ans)

print(ans)
while ans:
    print(heapq.heappop(ans))