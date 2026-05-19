class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ways = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                ways.append(curr.copy())
                return

            # positive
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            # negative
            curr.append(nums[i] * -1)
            dfs(i+1)
            curr.pop()

        dfs(0)

        ans = 0
        for cand in ways:
            if sum(cand) == target:
                ans += 1

        return ans


        
        