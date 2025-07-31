#dijkstra's algo can be applied only to graphs with non-negative weights
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        import heapq
        # code here
        pq = []
        adj_list = [[] for _ in range(V)]
        
        for e in edges:
            source = e[0]
            des =  e[1]
            wei = e[2]
            
            adj_list[source].append([des,wei])
            adj_list[des].append([source,wei])
            
        dist = [float('inf')]*V
        dist[src] = 0
        pq = [(0,src)]
        
        while pq:
            d,node = heapq.heappop(pq)
            for x in adj_list[node]:
                n = x[0]
                wei = x[1]
                if d+wei < dist[n]:
                    dist[n] = d+wei
                    heapq.heappush(pq,(d+wei,n))
            
                
            
        return dist