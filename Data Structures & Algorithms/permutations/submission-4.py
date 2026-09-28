class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = []
        curr = []
        seen = set()

        def dfs(ind, seen):
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return

            for j in range(len(nums)):
                if j not in seen:
                    curr.append(nums[j])
                    seen.add(j)
                    dfs(j+1, seen)
                    curr.pop()
                    seen.remove(j)

        dfs(0, seen)
        return perms
        