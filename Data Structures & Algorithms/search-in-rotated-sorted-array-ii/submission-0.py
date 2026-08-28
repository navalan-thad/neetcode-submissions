class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        pivot = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i

        def bs(left, right):

            while left <= right:
                mid = (left+right) // 2
                if target < nums[mid]:
                    right = mid-1
                elif target > nums[mid]:
                    left = mid+1
                else:
                    return True

            return False

        return bs(0, pivot) or bs(pivot, len(nums)-1)
        