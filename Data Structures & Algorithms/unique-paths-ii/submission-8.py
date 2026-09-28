class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        above = [1] * n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                above[i:] = [0] * (n-i)
                break

        row = above
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                row[0] = 0 
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    row[j] = above[j] + row[j-1]
                else:
                    row[j] = 0
            above = row

        return row[-1]
        
        