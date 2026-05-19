class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        all_subsets = []
        curr = []

        def dfs(i):
            if i == len(nums):
                currSorted = sorted(curr.copy())
                if currSorted not in all_subsets:
                    all_subsets.append(currSorted)
                return

            curr.append(nums[i]) # include i
            dfs(i+1)

            curr.pop() # exclude i
            dfs(i+1)

        dfs(0)

        return all_subsets




        