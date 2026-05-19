class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        result = 0
        def dfs(i, currXOR):
            nonlocal result
            if i >= len(nums):
                result += currXOR
                return
            # include index i
            dfs(i+1, currXOR ^ nums[i])
            # don't include index i
            dfs(i+1, currXOR)
        
        dfs(0, 0)
        
        return result



        
        