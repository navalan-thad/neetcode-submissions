class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dirs = [(0, 1), (1, 0)]

        memo = {}
        def dfs(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m-1 and j == n-1:
                return 1
            
            paths = 0
            for x, y in dirs:
                if x+i < m and y+j < n:
                    if obstacleGrid[x+i][y+j] == 0:
                        paths += dfs(x+i, j+y)
            
            memo[(i, j)] = paths
            return paths

        return dfs(0, 0)
            

        