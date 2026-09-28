class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # first row
        above = [1] * n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                above[i:] = [0] * (n-i)
                break

        row = above # init row val to above val for first cell
        for i in range(1, m): # remaining rows
            if obstacleGrid[i][0] == 1: # first cell in each row
                row[0] = 0
            for k in range(1, n): # remaining cells in the row
                if obstacleGrid[i][k] == 1:
                    row[k] = 0
                else:
                    row[k] = above[k] + row[k-1]
            above = row

        return above[-1]

        
        