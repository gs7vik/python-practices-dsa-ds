def adj_matrix_to_list(matrix):
    n = len(matrix)
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):  # Avoids double adding
            if matrix[i][j] == 1:
                adj_list[i].append(j)
                adj_list[j].append(i)
    return adj_list