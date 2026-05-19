class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            # include index i
            curr.append(nums[i])
            dfs(i+1)

            # skip i
            curr.pop()
            dfs(i+1)

        # generate all subsets
        dfs(0)
        return res
        