class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max, curr_min, glob_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], curr_max*nums[i], curr_min*nums[i])
            curr_min = min(nums[i], curr_max*nums[i], curr_min*nums[i])
            curr_max = new_max

            if curr_max > glob_max:
                glob_max = curr_max

        return glob_max



