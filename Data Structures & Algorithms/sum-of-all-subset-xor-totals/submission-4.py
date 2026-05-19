class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        result = 0
        def dfs(i, currXOR):

            if i >= len(nums):
                return currXOR

            include_i = dfs(i+1, currXOR ^ nums[i])
            exclude_i = dfs(i+1, currXOR)
            return include_i + exclude_i
        
        return dfs(0, 0)



        
        