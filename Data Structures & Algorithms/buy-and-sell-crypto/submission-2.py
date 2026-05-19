class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        profit = 0

        while buy < sell and sell < len(prices):
            profit = max(profit, prices[sell] - prices[buy])

            if sell == len(prices) - 1:
                buy += 1 
                sell = buy + 1
            else:
                sell += 1

        return profit