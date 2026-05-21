from math import inf

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dp(i, last_val):
            if (i, last_val) in memo:
                return memo[(i, last_val)]
            if i == len(nums):
                return 0

            res1 = 0

            if nums[i] > last_val:
                res1 = dp(i+1, nums[i]) + 1
            res2 = dp(i+1, last_val)

            maxLength = max(res1, res2)
            memo[(i, last_val)] = maxLength
            return maxLength

        return dp(0, -inf)




        