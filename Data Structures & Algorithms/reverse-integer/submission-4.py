class Solution:
    def reverse(self, x: int) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1

        x = abs(x)
        rev = 0

        while x:
            if rev * 10 > INT_MAX:
                return 0

            rev = rev*10 + (x % 10)
            x //= 10

        return rev * sign




        