#topological sorting using BFS (Kahn's algorithm)
#you will need queue and indegree list which will store the indegree of each node
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = [[] for _ in range(numCourses)]
        for ele in prerequisites:
            first,sec = ele
            adj_list[sec].append(first)
        
        print(adj_list)
        indeg = [0]*numCourses
        for ele in adj_list:
            for a in ele:
                indeg[a] +=1 
       
        q = deque()
        ans  = []
        for i, ele in enumerate(indeg):
            if ele == 0:
                q.append(i)

        while q:
            ele = q.popleft()
            ans.append(ele)
            for neigh in adj_list[ele]:
                indeg[neigh] -=1
                if indeg[neigh] == 0:
                    q.append(neigh)
        if len(ans) == numCourses:
            return ans
        else:
            return []

            


        