class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(i, last):
            if (i, last) in memo:
                return memo[(i, last)]

            if i >= len(nums):
                return 0

            rob = 0
            if last != i-1:
                rob = dp(i+1, i) + nums[i]

            skip = dp(i+1, last)

            memo[(i, last)] = max(rob, skip)
            return max(rob, skip)

        if len(nums) == 1:
            return nums[0]

        last = nums.pop()
        rob_first = dp(0, -2)

        memo.clear()

        nums.append(last)
        nums = nums[1:]
        rob_last = dp(0, -2)

        return max(rob_first, rob_last)

            
        