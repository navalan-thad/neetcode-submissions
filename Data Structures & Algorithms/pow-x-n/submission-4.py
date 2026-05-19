class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                half = pow(x, n//2)
                return half*half
            else:
                half = pow(x, (n-1)//2)
                return half*half*x

        if n < 0:
            n = -n
            x = 1/x

        return pow(x, n)
        