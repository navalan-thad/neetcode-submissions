class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF

        while b != 0: # while a carry remains
            noCarry = (a ^ b) & mask
            b = ((a&b) << 1) & mask
            a = noCarry

        return a if a <= maxInt else -( (a ^ mask) + 1 ) # 2's complement if negative

        