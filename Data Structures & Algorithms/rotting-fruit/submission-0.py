from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = 0
        rotten = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        while rotten:
            rot = False
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                if i+1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    rotten.append((i+1, j))
                    rot = True
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rotten.append((i-1, j))
                    rot = True
                if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    rotten.append((i, j+1))
                    rot = True
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    rotten.append((i, j-1))
                    rot = True

            if rot:
                time += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time

                
        