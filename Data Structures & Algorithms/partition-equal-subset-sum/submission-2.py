class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}

        def dp(i, amount):
            if (i, amount) in memo:
                return memo[(i, amount)]

            if i == len(nums):
                return False
            if amount == target:
                return True
            if amount > target:
                return False

            res1 = dp(i+1, amount+nums[i])
            res2 = dp(i+1, amount)
            memo[(i, amount)] = res1 or res2
            return res1 or res2

        for i in range(len(nums)):
            if dp(i, 0):
                return True
        return False






        