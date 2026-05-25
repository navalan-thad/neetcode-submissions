class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def dp(rem, ind):
            if (rem, ind) in memo:
                return memo[(rem, ind)]
            if rem == 0:
                return 1
            if ind == len(coins):
                return 0

            soln = 0
            
            if rem - coins[ind] >= 0:
                soln += dp(rem - coins[ind], ind)
            soln += dp(rem, ind+1)
            memo[(rem, ind)] = soln

            return soln

        return dp(amount, 0)
        