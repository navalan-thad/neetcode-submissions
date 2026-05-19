class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()
        ways = 0
        temp = 0
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                temp += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                ways = max(ways, temp)
                temp = 0
        ways = max(ways, temp)
        return ways + 1

        [0,1,1,2,3,4,5,6]
