class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        all_subsets = []
        curr = []
    
        def dfs(i, curr_sum):
            if i == len(nums) or curr_sum > target:
                return

            if curr_sum == target:
                all_subsets.append(curr.copy())
                return

            # include i
            curr.append(nums[i])
            curr_sum += nums[i]
            dfs(i, curr_sum)

            # exclude i
            curr.pop()
            curr_sum -= nums[i]
            dfs(i+1, curr_sum)

        dfs(0, 0)

        return all_subsets



        