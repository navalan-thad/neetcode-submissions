class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1)]
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m-1 and j == n-1:
                return grid[m-1][n-1]
            elif i == m or j == n:
                return float('inf')

            cost = float('inf')
            for x, y in dirs:
                cost = min(cost, dp(i+x, j+y) + grid[i][j])
            
            memo[(i, j)] = cost
            return cost

        return dp(0, 0)


            
        