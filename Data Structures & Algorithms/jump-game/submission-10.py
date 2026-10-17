class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = {}
        def dfs(i):
            if i >= len(nums)-1:
                return True

            if nums[i] == 0:
                return False

            if i in memo:
                return memo[i]

            jump = False
            for j in range(1, nums[i]+1):
                jump = dfs(i+j)
                if jump:
                    jump = True
                    break
                
            memo[i] = jump
            return memo[i]

        return dfs(0)
        