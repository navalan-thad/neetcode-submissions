class Solution:
    def multiply(self, num1: str, num2: str) -> str:


        int1 = 0
        int2 = 0

        for i in range(-1, -len(num1)-1, -1):
            int1 += int(num1[i]) * (10 ** (-i - 1))

        for i in range(-1, -len(num2)-1, -1):
            int2 += int(num2[i]) * (10 ** (-i - 1))

        return str(int1*int2)

        