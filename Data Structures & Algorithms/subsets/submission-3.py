class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        curr = []

        def dp(i):
            if i == len(nums):
                subsets.append(curr.copy())
                return

            curr.append(nums[i])
            dp(i+1)
            curr.pop()
            dp(i+1)
        
        dp(0)

        return subsets
        