class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        rotten = []
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        q = deque(rotten)

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)): # level processing
                i, j = q.popleft()
                for x, y in dirs:
                    if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]):
                        if grid[i+x][j+y] == 1:
                            grid[i+x][j+y] = 2
                            q.append((i+x, j+y))
                            fresh -= 1
            time += 1

        if fresh == 0:
            return time

        return -1

        