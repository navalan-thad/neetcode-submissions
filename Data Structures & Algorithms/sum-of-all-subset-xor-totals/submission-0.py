class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        all_subsets = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                all_subsets.append(curr.copy())
                return
            # include index i
            curr.append(nums[i])
            dfs(i+1)
            # don't include index i
            curr.pop()
            dfs(i+1)
        
        # generate all subsets
        dfs(0)

        print(all_subsets)

        result = 0
        for i in all_subsets:
            subset_total = 0
            for j in i:
                subset_total ^= j
            result += subset_total
        
        return result



        
        