class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        zeroes = set()
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.add(i)
            else:
                prod *= nums[i]

        for j in range(len(nums)):
            if zeroes:
                if j in zeroes and len(zeroes) == 1:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                output.append(prod // nums[j])

        return output
        