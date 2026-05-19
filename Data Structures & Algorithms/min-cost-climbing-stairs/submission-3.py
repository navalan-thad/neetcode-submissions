class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]

            if n == 0 or n == 1:
                return 0

            result = min(
                dp(n-1) + cost[n-1],
                dp(n-2) + cost[n-2]
            )
            memo[n] = result
            return result

        return dp(len(cost))



        