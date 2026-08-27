class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dp(i, bought):
            if i == len(prices):
                return 0

            if (i, bought) in memo:
                return memo[(i, bought)]

            if bought:
                sell = prices[i] + dp(i+1, False)
                hold = dp(i+1, True)
                maxProfit = max(sell, hold)
                memo[(i, bought)] = maxProfit
            else:
                buy = -prices[i] + dp(i+1, True)
                skip = dp(i+1, False)
                maxProfit = max(buy, skip)
                memo[(i, bought)] = maxProfit

            return maxProfit

        return dp(0, False)
            
            

        

        