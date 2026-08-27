class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        not_holding = 0
        holding = -prices[0]

        for price in prices:
            new_not_holding = max(not_holding, holding+price)
            new_holding = max(holding, not_holding-price)

            not_holding = new_not_holding
            holding = new_holding

        return not_holding
            
            

        

        