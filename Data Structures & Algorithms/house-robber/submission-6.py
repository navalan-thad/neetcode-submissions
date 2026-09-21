class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        def dp(i, canRob):
            if i == len(nums):
                return 0

            if (i, canRob) in memo:
                return memo[(i, canRob)]

            if canRob:
                rob = dp(i+1, False) + nums[i]
                not_robbed = dp(i+1, canRob)
                res = max(rob, not_robbed)
            else:
                res = dp(i+1, True)

            memo[(i, canRob)] = res
            return memo[(i, canRob)]

        return dp(0, True)
        