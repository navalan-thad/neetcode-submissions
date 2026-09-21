class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        from collections import deque
        q = deque()

        if n <= 2:
            return list(range(n))
        
        adj_list = {i: set() for i in range(n)}
        for i, j in edges:
            adj_list[i].add(j)
            adj_list[j].add(i)

        q = deque([i for i in adj_list if len(adj_list[i]) == 1])

        rem = n
        while rem > 2:
            count = len(q)
            rem -= count
            for _ in range(count):
                leaf = q.popleft()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)

                if len(adj_list[neighbor]) == 1:
                    q.append(neighbor)

        return list(q)



        