class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        result = 0
        i = 0
        j = 1
        k = 1

        for _ in range(2, n):
            result = i + j + k
            i, j, k = j, k, result

        return result



        