class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = {i:i for i in range(1, len(edges)+1)}

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
                
            if root_u != root_v:
                parent[root_u] = root_v
            else:
                return [u, v]
