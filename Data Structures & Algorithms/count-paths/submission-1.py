class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}

        def travel(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m or j == n:
                return 0

            if i == m-1 and j == n-1:
                return 1

            down = travel(i+1, j)
            right = travel(i, j+1)

            memo[(i, j)] = down + right

            return down + right

        paths = travel(0, 0)
        return paths
        