class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        suffix_sum = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]
        
        memo = {}
        def dp(ind, M):
            if ind >= n:
                return 0

            if (ind, M) in memo:
                return memo[(ind, M)]

            total = 0
            for X in range(1, 2*M+1):
                total = max(total, suffix_sum[ind]-dp(ind+X, max(X, M)))
            memo[(ind, M)] = total

            return total

        return dp(0, 1)


        

        