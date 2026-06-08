class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0

            visited.add((i, j))
            maxArea = 1          

            for x, y in dirs:
                if 0 <= i+x < n and 0 <= j+y < m:
                    if grid[i+x][y+j] == 1:
                        maxArea += dfs(i+x, j+y)

            return maxArea

        area = 0
        for i in range(n):
            for j in range(m):
                area = max(area, dfs(i, j))

        return area

        



        