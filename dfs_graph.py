def dfs(node, adj_list, dfs_list,  vis):
    
    for x in adj_list[node]:
        if vis[x] == 0:
            vis[x] = 1
            dfs_list.append(x)
            dfs(x, adj_list, dfs_list, vis)
        

    

adj_list = [
    [1, 2],    # Neighbors of node 0
    [0, 3, 4], # Neighbors of node 1
    [0],       # Neighbors of node 2
    [1],       # Neighbors of node 3
    [1]        # Neighbors of node 4
]

dfs_list = []
vis = [0] * len(adj_list)
vis[0] = 1  # Mark the starting node as visited
node = 0
dfs_list.append(node)  # Start DFS from node 0
dfs(node, adj_list, dfs_list,vis)
print("BFS Traversal:", dfs_list)  # Output: BFS Traversal: [0, 1, 3, 4, 2]