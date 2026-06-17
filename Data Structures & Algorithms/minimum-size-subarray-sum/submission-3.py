class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLen = float('inf')
        start, end = 0, 0
        total = nums[0]
        size = len(nums)
        
        while end < size and start <= end:
            if total >= target:
                minLen = min(minLen, end-start+1)
                total -= nums[start]
                start += 1
                if start > end:
                    end += 1
                    if end < size:
                        total += nums[end]
            else:
                end += 1
                if end < size:
                    total += nums[end]

        return 0 if minLen == float('inf') else minLen





        