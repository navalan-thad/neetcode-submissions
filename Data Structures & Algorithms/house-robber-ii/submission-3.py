class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0

            rob = dp(i+2) + nums[i]
            skip = dp(i+1)

            memo[i] = max(rob, skip)
            return max(rob, skip)

        if len(nums) == 1:
            return nums[0]

        last = nums.pop()
        rob_first = dp(0)

        memo.clear()

        nums.append(last)
        nums = nums[1:]
        rob_last = dp(0)

        return max(rob_first, rob_last)

            
        