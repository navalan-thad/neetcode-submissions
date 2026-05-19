class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        all_nums = [i for i in range(len(nums)+1)]
        visited = []

        for i in all_nums:
            if i not in nums:
                return i

        