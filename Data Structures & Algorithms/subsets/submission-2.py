class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        all_subsets = []
        current = []

        def dfs(index):
            if index >= len(nums):
                all_subsets.append(current.copy())
                return

            # include nums[index]
            current.append(nums[index])
            dfs(index+1)

            # don't include nums[index]
            current.pop()
            dfs(index+1)

        dfs(0)
        return all_subsets