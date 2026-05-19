class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == '0' or num2 == '0':
            return '0'

        n = len(num1)
        m = len(num2)
        res = [0] * (n+m)

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                product = int(num1[i]) * int(num2[j])

                # add current product to existing value
                total = product + res[i + j + 1]

                # store digit and carry
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        # convert array to string
        result_str = ''.join([str(x) for x in res])

        # remove leading zeros
        return result_str.lstrip('0')

        