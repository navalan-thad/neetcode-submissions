class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        prod = 1
        for i in range(len(nums)):
            output[i] = prod
            prod *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output   
        