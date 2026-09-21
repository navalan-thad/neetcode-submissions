class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 2:
            return list(range(n))
        
        from collections import deque

        adj = {i: set() for i in range(n)}
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = deque([node for node in range(n) if len(adj[node]) == 1])

        remaining = n
        while remaining > 2:
            level_count = len(leaves)
            remaining -= level_count

            for _ in range(level_count):
                leaf = leaves.popleft()

                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)


        return list(leaves)
        