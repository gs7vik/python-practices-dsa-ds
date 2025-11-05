#step 1 Our dataset: (features, label)
dataset = [
    ([1.0, 2.0], 'A'),
    ([2.0, 3.0], 'A'),
    ([3.0, 3.0], 'B'),
    ([5.0, 1.0], 'B'),
    ([6.0, 2.0], 'B')
]

def euclidean_distance(x1, x2):
    total = 0
    for i in range(len(x1)):
        total += (x1[i] - x2[i]) ** 2
    return total ** 0.5

def knn_predict(dataset, query_point, k=3):
    # 1. Compute distances
    distances = []
    for features, label in dataset:
        dist = euclidean_distance(features, query_point)
        distances.append((dist, label))
    
    # 2. Sort by distance
    distances.sort(key=lambda x: x[0])
    
    # 3. Pick k nearest neighbors
    neighbors = distances[:k]
    
    # 4. Count labels
    label_counts = {}
    for _, label in neighbors:
        label_counts[label] = label_counts.get(label, 0) + 1
    
    # 5. Return the label with max votes
    return max(label_counts, key=label_counts.get)

query = [4.0, 2.0]
predicted_label = knn_predict(dataset, query, k=3)
print(f"Predicted label for {query}: {predicted_label}")
