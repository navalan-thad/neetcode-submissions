class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_total = sum(nums)
        true_total = sum([i for i in range(len(nums)+1)])

        return true_total - nums_total

        