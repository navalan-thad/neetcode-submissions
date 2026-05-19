class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        visited = set()

        i = 0
        while i < len(nums):
            if nums[i] in visited:
                nums.remove(nums[i])
            else:
                visited.add(nums[i])
                i += 1

        return len(visited)
        