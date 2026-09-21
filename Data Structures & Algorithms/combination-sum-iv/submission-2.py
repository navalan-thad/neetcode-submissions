class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        nums.sort()
        def dfs(total):
            if total == target:
                return 1

            if total > target:
                return 0

            if total in memo:
                return memo[total]

            res = 0
            for num in nums:
                res += dfs(total + num)

            memo[total] = res
            return res

        return dfs(0)
        