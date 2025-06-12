
def bfs(adj):
    
    vis = [0]*len(adj)
    vis[0] =1 
    q = []
    q.append(0)
    
    bfs = []
    while len(q)!=0:
        node = q.pop(0)
        bfs.append(node)

        for i in adj[node]:
            if vis[i] ==0: #if not vis[i]
                vis[i] = 1
                q.append(i)
            
    return bfs

adj_list = [
    [1, 2],    # Neighbors of node 0
    [0, 3, 4], # Neighbors of node 1
    [0],       # Neighbors of node 2
    [1],       # Neighbors of node 3
    [1]        # Neighbors of node 4
]

bfs_result = bfs(adj_list)
print("BFS Traversal:", bfs_result)  # Output: BFS Traversal: [0, 1, 2, 3, 4]