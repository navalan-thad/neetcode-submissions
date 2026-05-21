class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        groups = {i:i for i in range(n)}

        def find(n):
            while n != groups[n]:
                groups[n] = groups[groups[n]]
                n = groups[n]
            return n

        count = n
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                groups[root_u] = root_v
                count -= 1

        return count



        