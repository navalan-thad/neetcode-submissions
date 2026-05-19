class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dp(i, can_buy):
            if (i, can_buy) in memo:
                return memo[(i, can_buy)]
            if i >= len(prices):
                memo[(i, can_buy)] = 0
                return 0

            if not can_buy:
                hold = dp(i+1, False)
                sell = dp(i+2, True) + prices[i]
                memo[(i, can_buy)] = max(hold, sell)
                return memo[(i, can_buy)]
            else:
                skip = dp(i+1, True)
                buy = dp(i+1, False) - prices[i]
                memo[(i, can_buy)] = max(skip, buy)
                return memo[(i, can_buy)]
            
        return dp(0, True)