class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0

            branch1 = 0
            branch2 = 0

            if text1[i] == text2[j]:
                branch1 = dp(i+1, j+1) + 1
            else:
                branch2 = max(dp(i, j+1), dp(i+1, j))

            memo[(i, j)] = max(branch1, branch2)
            return memo[(i, j)]

        return dp(0, 0)
        