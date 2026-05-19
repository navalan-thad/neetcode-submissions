class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        k = len(nums)
        while count < k:
            if nums[count] == val:
                if k == 1:
                    return 0
                nums[-1], nums[count] = nums[count], nums[-1]
                nums.pop()
                k -= 1
            else:
                count += 1
            

        return k
        