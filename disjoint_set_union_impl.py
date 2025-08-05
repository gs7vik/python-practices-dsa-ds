"""
Disjoint Set Union is a data structure that is commonly used to reduce the time complexity of 
graph problems to constant time.
two ways of union:
union_by_rank
union_by_size
you will be having a list of graph edges

The algo goes like this:
1. initialise a rank list with initial rank 0s and parent list where the nodes will be parent of itself. consider
a 1 based index list [1,2,3,4,5] where the values at the index represent the parents, for 
example 1 is the parent of index 1.
now iterate through each edge which is in the form of u->v:
    1. find ultimate parent of u and v, pu and pv (if pu==pv then return as they belong to the same comp(component))
    2. Find rank of pu and pv (rank actually means the height of the tree)
    3. Always Connect smaller rank to larger rank (in case of equality you can connect anyone to anyone)
    
"""
class DSU:
    
    def __init__(self,n):
        
        self.parent = [i for i in range(n+1)]
        
        self.rank = [0]*(n+1)
        
    def find_ultimate_parent(self, node):
        
        if node == self.parent[node]:
            return node
        else:
            # self.parent[node] = self.find_ultimate_parent(node) 
            self.parent[node] = self.find_ultimate_parent(self.parent[node])
            return self.parent[node]        
    
    def find_union_rank(self,u,v):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)
        
        if ulp_u == ulp_v:
            return #this means that u and v belong to the same component.
        
        elif self.rank[ulp_u] > self.rank[ulp_v]:
                self.parent[ulp_v] = ulp_u
        elif self.rank[ulp_v] > self.rank[ulp_u]:
                self.parent[ulp_u] = ulp_v
        else: #if the ranks are equal then rank of any one up will increase
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u]+=1
            
dsu = DSU(7)

dsu.find_union_rank(1,2)
dsu.find_union_rank(2,3)
dsu.find_union_rank(4,5)
dsu.find_union_rank(6,7)
dsu.find_union_rank(5,6)

if dsu.find_ultimate_parent(3) == dsu.find_ultimate_parent(7):
    print("same")
else:
    print("not same") 

#will print not same 

dsu.find_union_rank(3,7)

if dsu.find_ultimate_parent(3) == dsu.find_ultimate_parent(7):
    print("same")
else:
    print("not same") 

#will print same
