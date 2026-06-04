class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        explored = set() 

        def dfs(i, j):
            if (i, j) in explored:
                return
            if grid[i][j] == '1':
                explored.add((i, j))
                grid[i][j] = '0'

                for x, y in dirs:
                    if 0 <= x+i < n and 0 <= y+j < m:
                        dfs(x+i, y+j)

        islands = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        return islands


            

        



