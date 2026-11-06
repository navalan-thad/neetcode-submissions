class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combs = []
        curr = []

        def dfs(i):
            total = sum(curr)
            if total > target:
                return

            if total == target:
                combs.append(curr.copy())
                return

            if i == len(nums):
                return


            curr.append(nums[i])
            dfs(i)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return combs
        