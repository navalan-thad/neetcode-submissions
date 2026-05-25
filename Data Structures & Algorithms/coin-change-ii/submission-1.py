class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def dp(rem, ind):
            if (rem, ind) in memo:
                return memo[(rem, ind)]
            if rem == 0:
                return 1

            soln = 0
            
            for j in range(ind, len(coins)): 
                if rem - coins[j] >= 0:
                    soln += dp(rem - coins[j], j)
                    memo[(rem, ind)] = soln

            return soln

        return dp(amount, 0)
        