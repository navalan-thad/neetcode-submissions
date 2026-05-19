class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return False

        nums = sorted(nums)
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                return True

        return False
        