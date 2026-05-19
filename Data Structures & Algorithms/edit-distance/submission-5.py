class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                res = dp(i+1, j+1)
                memo[(i, j)] = res
                return res
            else:
                insert = 1 + dp(i, j+1)
                delete = 1 + dp(i+1, j)
                replace = 1 + dp(i+1, j+1)

                res = min(insert, delete, replace)
                memo[(i, j)] = res
                return res

        soln = dp(0, 0)
        return soln



        