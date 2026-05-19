class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF # 32-bit mask (hexadecimal)
        max_int = 0x7FFFFFFF # max 32-bit int

        while b != 0:
            temp = (a ^ b) & mask # XOR gives sum without carry
            b = ((a & b) << 1) & mask # AND + shift gives the carry
            a = temp

        # Handle negative numbers
        return a if a <= max_int else ~(a ^ mask)
        