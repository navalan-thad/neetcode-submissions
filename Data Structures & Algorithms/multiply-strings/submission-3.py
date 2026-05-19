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

                # positions in result array
                p1 = i + j
                p2 = i + j + 1

                # add current product to existing value
                total = product + res[p2]

                # store digit and carry
                res[p2] = total % 10
                res[p1] += total // 10

        # convert array to string
        result_str = ''.join(map(str, res))

        # remove leading zeros
        return result_str.lstrip('0')

        