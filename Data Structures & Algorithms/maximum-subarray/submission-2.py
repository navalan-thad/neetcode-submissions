class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        memo = {}

        def maxUntil(i):
            if i in memo:
                return memo[i]

            if i == len(nums)-1:
                return nums[-1]

            res = max(nums[i] + maxUntil(i+1), nums[i])
            memo[i] = res
            return res

        val = maxUntil(0)

        for i in range(1, len(nums)):
            res = maxUntil(i) 
            if res > val:
                val = res
        return val

        


        