class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        result = 0
        def dfs(i, curr):
            nonlocal result
            if i >= len(nums):
                result += curr
                return
            # include index i
            dfs(i+1, curr ^ nums[i])
            # don't include index i
            dfs(i+1, curr)
        
        dfs(0, 0)
        
        return result



        
        