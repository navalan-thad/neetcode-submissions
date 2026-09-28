class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        above = [grid[0][0]] * n
        for i in range(1, n):
            above[i] = grid[0][i] + above[i-1]

        for i in range(1, m): # remaining rows
            rows = above
            rows[0] += grid[i][0]
            for j in range(1, n):
                rows[j] = min(above[j], rows[j-1]) + grid[i][j]
            above = rows

        return above[-1]



            
        