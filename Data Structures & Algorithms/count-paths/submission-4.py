class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dirs = [(0, 1), (1, 0)]
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i > m-1 or j > n-1:
                return 0
            elif i == m-1 and j == n-1:
                return 1

            ways = 0

            for x, y in dirs:
                ways += dp(i+x, j+y)

            memo[(i, j)] = ways
            return ways

        return dp(0, 0)
        