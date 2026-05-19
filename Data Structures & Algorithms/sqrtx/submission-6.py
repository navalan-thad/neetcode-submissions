class Solution:
    def mySqrt(self, x: int) -> int:

        L = 0
        R = x

        while L <= R:
            mid = (L + R) // 2
            if x < mid*mid:
                R = mid - 1
            elif x > mid*mid:
                L = mid + 1
            else:
                return mid

        return R