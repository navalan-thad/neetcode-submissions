from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = 0
        rotten = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while rotten:
            rot = False
            for _ in range(len(rotten)):

                i, j = rotten.popleft()
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy

                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            rotten.append((ni, nj))
                            rot = True
            if rot:
                time += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return time