class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ans = 0

        def dfs(i, total):
            nonlocal ans
            if i >= len(nums):
                if total == target:
                    ans += 1
                return

            # positive
            dfs(i+1, total + nums[i])

            # negative
            dfs(i+1, total - nums[i])

        dfs(0, 0)

        return ans


        
        