from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = dict()
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for val in range(1, amount+1):
            for coin in coins:
                if val - coin >= 0:
                    cand = 1 + dp[val - coin]
                    dp[val] = min(dp[val], cand)

        return -1 if dp[amount] == inf else dp[amount]




        