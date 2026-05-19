class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]

            if n == 0 or n == 1:
                return 1

            result = dp(n-1) + dp(n-2)
            memo[n] = result
            return result

        return dp(n)


        