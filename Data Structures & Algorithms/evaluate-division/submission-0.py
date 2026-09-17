class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = {}

        for (u, v), val in zip(equations, values):
            if u not in adj_list:
                adj_list[u] = {}
            if v not in adj_list:
                adj_list[v] = {}

            adj_list[u][v] = val
            adj_list[v][u] = 1.0 / val

        def dfs(i, j, visited):
            if i in visited:
                return -1.0
            else:
                visited.add(i)
            if i == j:
                return 1.0

            for neighbor, weight in adj_list[i].items():
                if neighbor not in visited:
                    sub = dfs(neighbor, j, visited)
                    if sub != -1.0:
                        return weight * sub
            return -1.0

        res = []

        for c, d in queries:
            visited = set()
            if c not in adj_list or d not in adj_list:
                res.append(-1)
            elif c == d:
                res.append(1)
            else:
                res.append(dfs(c, d, visited))

        return res

