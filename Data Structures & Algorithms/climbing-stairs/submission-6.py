class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0 or n == 1:
            return 1

        start = 0
        end = 1

        for _ in range(1, n+1):
            start, end = end, start+end

        return end
        



        