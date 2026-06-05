from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        inf = 2**31 - 1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        frontier = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    frontier.append((i, j, 0))

        while frontier:
            i, j, dist = frontier.popleft()

            for x, y in dirs:
                if 0 <= x+i < m and 0 <= y+j < n:
                    if grid[i+x][y+j] == inf:
                       grid[i+x][y+j] = dist+1
                       frontier.append((i+x, j+y, dist+1))

        

        