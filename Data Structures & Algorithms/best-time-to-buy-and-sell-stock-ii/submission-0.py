class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        buy = 0
        skip = 0
        sell = 0

        memo = {}

        def dp(i, holding):
            if (i, holding) in memo:
                return memo[(i, holding)]

            if i == len(prices):
                return 0

            if holding:
                sell = prices[i] + dp(i+1, False)
                skip = dp(i+1, True)
                res = max(sell, skip)
                memo[(i, holding)] = res
            else:
                buy = -prices[i] + dp(i+1, True)
                skip = dp(i+1, False)
                res = max(buy, skip)
                memo[(i, holding)] = res

            
            return res

        return dp(0, False)


        