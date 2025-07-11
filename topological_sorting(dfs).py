#TOpological sorting DFS way
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            # print(u)
            adj[u].append(v)
            
        def dfs(i,vis,st):
            vis.add(i)
            for ele in adj[i]:
                if ele not in vis:
                    dfs(ele,vis,st)
            st.append(i)
            
            
        vis = set()
        st = []
        for i in range(V):
            if i not in vis:
                dfs(i,vis,st)
        
        ans = []
        while st:
            x = st.pop()
            ans.append(x)
        
        return ans
# Example usage:
if __name__ == "__main__":
    V = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    #we have to create an adjacency list from the edges
    # and then perform a topological sort on the graph represented by the adjacency list.
    solution = Solution()
    result = solution.topoSort(V, edges)
    print("Topological Sort:", result)  # Output: Topological Sort: [5, 4, 2, 3, 1, 0]
    