class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = []
        curr = []

        def dfs(curr, rem):
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return
            
            for i in range(len(rem)):
                curr.append(rem[i])
                dfs(curr, rem[:i]+rem[i+1:])
                curr.pop()

        dfs(curr, nums)
        return perms

        