class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        
        start = 0
        end = 1

        while start < len(nums)-1:
            if nums[start] == nums[end]:
                if abs(start - end) <= k:
                    return True
            end += 1
            if end == len(nums):
                start += 1
                end = start + 1

        return False
        
        