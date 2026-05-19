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
            total += nums[i]
            dfs(i+1, total)

            # negative
            total -= (nums[i] * 2)
            dfs(i+1, total)
            
        dfs(0, 0)

        return ans


        
        