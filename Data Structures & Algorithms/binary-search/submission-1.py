class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1
        mid = (L + R) // 2

        while L <= R:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1 
            mid = (L + R) // 2


        return -1
        