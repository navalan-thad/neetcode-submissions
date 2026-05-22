class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0

            res1 = dp(i+1)
            res2 = dp(i+2) + nums[i]

            memo[i] = max(res1, res2)
            return memo[i]

        return dp(0)


            
        