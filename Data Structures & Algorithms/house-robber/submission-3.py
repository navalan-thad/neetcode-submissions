class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(i, last_robbed):
            if (i, last_robbed) in memo:
                return memo[(i, last_robbed)]

            if i >= len(nums):
                return 0

            res2 = 0
            res1 = dp(i+1, last_robbed)
            if last_robbed != i-1:
                res2 = dp(i+1, i) + nums[i]

            memo[(i, last_robbed)] = max(res1, res2)
            return memo[(i, last_robbed)]

        return dp(0, -2)


            
        