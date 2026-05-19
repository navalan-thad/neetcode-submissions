class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parent = {i:i for i in range(n)}

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        edges_used = 0 
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
                
            if root_u != root_v:
                parent[root_u] = root_v  # Merge
                edges_used += 1
            else:
                return False
                
        if edges_used == n-1:
            return True
        return False

        
        