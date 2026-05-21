class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i == len(nums)-1:
                return nums[i]

            res = max(nums[i] + dp(i+1), nums[i])
            memo[i] = res
            return res

        maxSum = dp(0)
        for i in range(1, len(nums)):
            ith_dp = dp(i)
            if ith_dp > maxSum:
                maxSum = ith_dp
        return maxSum



        