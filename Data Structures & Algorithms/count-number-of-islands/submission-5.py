class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n, m = len(grid), len(grid[0])
        parent = {}
        self.islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.islands += 1
                    parent[(i, j)] = (i, j)

        def find(n):
            while n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1, n2):
            root_n1 = find(n1)
            root_n2 = find(n2)

            if root_n1 != root_n2:
                parent[root_n1] = parent[root_n2]
                self.islands -= 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    if j+1 < m and grid[i][j+1] == '1':
                        union((i, j), (i, j+1))
                    if i+1 < n and grid[i+1][j] == '1':
                        union((i, j), (i+1, j))

        return self.islands



            

        



