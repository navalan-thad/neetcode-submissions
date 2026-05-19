class Solution:
    def myPow(self, x: float, n: int) -> float:

        ans = x

        if n == 0:
            return 1
        else:
            for _ in range(1, abs(n)):
                ans = ans * x
        
            print(ans)
            if n < 0:
                ans = 1 / ans

        return ans

        