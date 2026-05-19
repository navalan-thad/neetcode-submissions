class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def recur(n):
            if n in cache:
                return cache[n]
            if n == 0 or n == 1:
                return 1

            result = recur(n-1) + recur(n-2)
            cache[n] = result
            return result

        return recur(n)
        



        