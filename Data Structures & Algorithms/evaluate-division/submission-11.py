class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = {}
        for (a, b), val in zip(equations, values):
            if a not in adj_list:
                adj_list[a] = {}
            if b not in adj_list:
                adj_list[b] = {}

            adj_list[a][b] = val
            adj_list[b][a] = 1.0 / val


        def dfs(src, dst, visited):
            if src in visited:
                return -1.0
            visited.add(src)
            if src == dst:
                return 1.0

            for neighbor, val in adj_list[src].items():
                if neighbor not in visited:
                    res = dfs(neighbor, dst, visited)
                    if res != -1.0:
                        return res*val
            return -1.0

        res = []
        for c, d in queries:
            if c not in adj_list or d not in adj_list:
                res.append(-1.0)
            elif c == d:
                res.append(1.0)
            else:
                visited = set()
                res.append(dfs(c, d, visited))

        return res

