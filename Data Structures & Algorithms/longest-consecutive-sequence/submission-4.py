class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        numSet = set(nums)

        ways = 0
        for i in nums:
            if i-1 not in numSet:
                temp = 1
                nextNum = i+1
                while nextNum in numSet:
                    temp += 1
                    nextNum += 1
                ways = max(temp, ways)
                temp = 1
                
        return ways
