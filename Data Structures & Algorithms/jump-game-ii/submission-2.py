from math import inf

class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums)-1:
                return 0
            if nums[i] == 0:
                return inf

            res = dp(i+1) + 1
            for j in range(1, nums[i]+1):
                res = min(dp(i+j)+1, res)
                
            memo[i] = res
            return res

        return dp(0)
        