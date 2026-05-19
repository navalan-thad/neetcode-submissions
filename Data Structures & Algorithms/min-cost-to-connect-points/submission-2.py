class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        all_pairs = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                all_pairs.append((manhattan(points[i], points[j]), i, j))

        all_pairs.sort(key=lambda x: x[0])
        
        cost = 0
        parent = {i: i for i in range(len(points))}
        cost = 0

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]  # Path compression
                n = parent[n]                  # Move up to the parent
            return n

        edges_used = 0 
        for weight, u, v in all_pairs:
            root_u = find(u)
            root_v = find(v)
            
            if root_u != root_v:
                parent[root_u] = root_v  # Merge
                cost += weight
                edges_used += 1
                
                if edges_used == len(points) - 1:
                    return cost

        return cost
        