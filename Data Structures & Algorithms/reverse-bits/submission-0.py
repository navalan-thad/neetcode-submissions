class Solution:
    def reverseBits(self, n: int) -> int:

        if n == 0:
            return 0

        strInt = ""
        while n > 0:
            remainder = n % 2
            strInt = str(remainder) + strInt
            n //= 2

        size = len(strInt)
        if size < 32:
            strInt = (32-size) * ("0") + strInt

        total = 0
        for i in range(32):
            total += int(strInt[i])*(2 ** i)
        return total
