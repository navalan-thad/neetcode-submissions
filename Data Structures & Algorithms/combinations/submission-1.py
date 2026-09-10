class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combs = []
        nums = [i for i in range(1, n+1)]
        curr = []
        
        def dfs(i):
            if len(curr) == k:
                combs.append(curr.copy())
                return
            if i == len(nums):
                return

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return combs

            

        
        