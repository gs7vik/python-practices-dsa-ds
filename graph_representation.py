#unweighted, undirected graph representation using adjacency matrix
n = 5  # Number of nodes
adj_matrix = [[0] * n for _ in range(n)]

edges = [(0, 1), (1, 2), (3, 4)]
for u, v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # If undirected

print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
# Output:
# Adjacency Matrix:
# [0, 1, 0, 0, 0]
# [1, 0, 1, 0, 0]
# [0, 1, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 0, 0, 1, 0]

#unweighted, undirected graph representation using adjacency list
adj_list = [[] for _ in range(n)]

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)  # If undirected
    
print("\nAdjacency List:")
for i, neighbors in enumerate(adj_list):
    print(f"{i}: {neighbors}")

# Output:
# Adjacency List:
# 0: [1]
# 1: [0, 2]
# 2: [1]
# 3: [4]
# 4: [3]

# Weighted, undirected graph representation using adjacency matrix
n = 5
weight_adj_matrix = [[0] * n for _ in range(n)]

edges = [(0, 1, 2), (1, 2, 4), (3, 4, 1)]  # (u, v, weight)
for u, v, w in edges:
    weight_adj_matrix[u][v] = w
    weight_adj_matrix[v][u] = w  # If undirected
    
print("\nWeighted Adjacency Matrix:")
for row in weight_adj_matrix:
    print(row)
# Output:
# Weighted Adjacency Matrix:

# [0, 2, 0, 0, 0]
# [2, 0, 4, 0, 0]
# [0, 4, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 0, 0, 1, 0]
