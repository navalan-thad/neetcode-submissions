from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [inf] * (amount + 1)
        dp[0] = 0

        for curr_amount in range(1, amount+1):
            for coin in coins:
                if curr_amount - coin >= 0:
                    cand = 1 + dp[curr_amount - coin]
                    dp[curr_amount] = min(dp[curr_amount], cand)
        return -1 if dp[amount] == inf else dp[amount]

        # top down
        # memo = {}

        # def solve(rem):
        #     if rem == 0:
        #         return 0
        #     if rem < 0:
        #         return inf
        #     if rem in memo:
        #         return memo[rem]
        
        #     best = inf
        #     for coin in coins:
        #         cand = 1 + solve(rem - coin)
        #         best = min(best, cand)
        #     memo[rem] = best

        #     return best

        # result = solve(amount)
        # return -1 if result == inf else result






        