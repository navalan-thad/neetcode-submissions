class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if i != j:
                    total *= nums[j]
            output.append(total)

        return output
        