class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = []
        curr = []
        visited = set()

        def dfs(i, visited):
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return

            for i in range(len(nums)):
                if i not in visited:
                    curr.append(nums[i])
                    visited.add(i)
                    dfs(i+1, visited)
                    curr.pop()
                    visited.remove(i)
                    
        dfs(0, visited)
        return perms
        