#User function Template for python3

from typing import List


class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        #create an adjacency list first
        def dfs(node, vis,st):
            vis.add(node)
            for x in adj_list[node]:
                y = x[0]
                if y not in vis:
                    dfs(y,vis,st)
            st.append(node)
        
        vis = set()
        st = []
        adj_list = [[] for _ in range(V)]
        for ele in edges:
            pos = ele[0]
            nei = ele[1]
            weight = ele[2]
            adj_list[pos].append([nei,weight])
        # print(adj_list)
        for i in range(V):
            if i not in vis:
                dfs(i,vis,st)
        # print(st)
        dis_list = [10**5+1]*V
        dis_list[0] = 0
        
        while st:
            x = st.pop()
            for ele in adj_list[x]:
                v = ele[0]
                wt = ele[1]
                if dis_list[x]+wt < dis_list[v]:
                    dis_list[v] = dis_list[x]+wt
        
        
        for i,ele in enumerate(dis_list):
            if ele == 10**5+1:
                dis_list[i] = -1
        
        # print(dis_list)
        return dis_list
            
        