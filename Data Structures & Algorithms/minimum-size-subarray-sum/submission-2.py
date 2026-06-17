class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLen = float('inf')
        start, end = 0, 0
        
        while end < len(nums) and start <= end:
            if sum(nums[start:end+1]) >= target:
                minLen = min(minLen, end-start+1)
                start += 1
                if start > end:
                    end += 1
            else:
                end += 1

        return 0 if minLen == float('inf') else minLen





        