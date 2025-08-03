#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist = [100000000]*V
        
        dist[src] = 0
        for i in range(V-1):
            for e in edges:
                source = e[0]
                dest = e[1]
                wei = e[2]
                
                if dist[source] != 100000000  and dist[source] + wei < dist[dest]:
                    dist[dest] = dist[source] + wei
        
        #for negative cycle detection
        for i in range(1):
            for e in edges:
                source = e[0]
                dest = e[1]
                wei = e[2]
                
                if dist[source] != 100000000 and dist[source] + wei < dist[dest]:
                    return [-1]
        
        return dist
            
        