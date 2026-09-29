class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        import heapq

        m, n = len(heights), len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_heap = [(0, 0, 0)] # effort, row, col
        efforts = [[float('inf')]*n for _ in range(m)]
        efforts[0][0] = 0

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if (r, c) == (m-1, n-1):
                return effort

            for x, y in dirs:
                if 0 <= x+r < m and 0 <= y+c < n:
                    next_effort = max(effort, abs(heights[r+x][c+y] - heights[r][c]))

                    if next_effort < efforts[r+x][c+y]:
                        efforts[r+x][c+y] = next_effort
                        heapq.heappush(min_heap, (next_effort, x+r, c+y))
