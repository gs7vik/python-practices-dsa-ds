from collections import deque
class Solution:
    def isBipartite(self, V, edges):
        # code here
        adj_list = [[] for _ in range(V)]
        for e in edges:
            source = e[0]
            dest = e[1]
            adj_list[source].append(dest)
            adj_list[dest].append(source)
        
        col = [-1]*V
        
        q = deque()
        
        col[0] = 0
        q.append(0)
        
        while q:
            ele = q.popleft()
            for nei in adj_list[ele]:
                #if the neighbor has not been colored yet
                #we color it with the opposite color of the current node
                if col[nei] == -1:
                    col[nei] = 1 - col[ele]
                    q.append(nei)
                
                elif col[nei] == col[ele]:#when its not bipartite you will get a scenario when the neighbor has the same color as the current node
                    return False
        return True