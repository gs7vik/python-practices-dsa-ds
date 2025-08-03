"""
In an undirected graph, if during DFS you reach a neighbor that is already visited and is not the parent, 
then you’ve found a cycle.
https://claude.ai/public/artifacts/d01110b3-6f7a-4c83-aadf-cf25f412e92f
check above image for better understanding(created by claude..prompted by me).
tldr:
If you’re at a node C and you see a neighbor D that:

1. Is already visited, and

2. Is not the parent of C

…it means there is a cycle.
"""
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj = [[] for _ in range(V)]
		for s,d in edges:
		    adj[s].append(d)
		    adj[d].append(s)
        
        vis = set()
        
        
        def hasCycle(adj,node,parent,vis):
            
            vis.add(node)
            
            for nei in adj[node]:
                if nei not in vis:
                    if hasCycle(adj,nei,node,vis):
                        return True
                elif nei != parent:
                    return True
            return False
        for i in range(V):
            if i not in vis:
                if hasCycle(adj, i, -1, vis):
                    return True
        return False

            

