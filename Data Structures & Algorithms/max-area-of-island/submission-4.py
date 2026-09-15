class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        
        def dfs(i, j):
            if i == len(grid) or j == len(grid[0]):
                return 0

            area = 1

            if grid[i][j] == 1:
                grid[i][j] = 0
                for x, y in dirs:
                    if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]):
                        if grid[i+x][j+y] == 1:
                            area += dfs(i+x, j+y)
            else:
                return 0
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, dfs(i, j))

        return max_area

        