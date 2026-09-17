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

        def dfs(src, dst, visited):
            if src in visited:
                return -1.0
            else:
                visited.add(src)
            if src == dst:
                return 1.0

            for neighbor, val in adj_list[src].items():
                if neighbor not in visited:                
                    branch = dfs(neighbor, dst, visited)
                    if branch != -1.0:
                        return val*branch

            return -1.0

        res = []
        for c, d in queries:
            if c not in adj_list or d not in adj_list:
                res.append(-1.0)
            elif c == d:
                res.append(1.0)
            else:
                visited=set()
                res.append(dfs(c, d, visited))

        return res

