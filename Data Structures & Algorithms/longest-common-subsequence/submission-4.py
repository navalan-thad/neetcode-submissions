class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0

            inc, inc1, inc2 = 0, 0, 0

            if text1[i] == text2[j]:
                inc += dp(i+1, j+1) + 1
            else:
                inc1 = dp(i+1, j)
                inc2 = dp(i, j+1)

            memo[(i, j)] = max(inc, inc1, inc2)

            return memo[(i, j)]

        return dp(0, 0)


        