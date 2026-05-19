class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1
        memo = {}

        def dp(posn):
            if posn in memo:
                return memo[posn]

            if posn + nums[posn] >= target:
                return True

            maxJump = min(posn + nums[posn], target)

            for dist in range(maxJump, posn, -1):
                if dp(dist):
                    memo[dist] = True
                    return True

            memo[posn] = False
            return False

        return dp(0)

            


        