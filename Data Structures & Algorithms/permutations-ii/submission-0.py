class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        perms = []
        curr = []
        visited = set()
        nums.sort()

        def dfs(i, visited):
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                    continue
                    
                curr.append(nums[i])
                visited.add(i)
                dfs(i+1, visited)
                curr.pop()
                visited.remove(i)

        dfs(0, visited)
        return perms

            
        