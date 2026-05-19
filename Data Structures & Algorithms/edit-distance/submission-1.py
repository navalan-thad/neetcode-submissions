class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def minOps(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(word1):
                memo[(i, j)] = len(word2) - j
                return len(word2) - j

            if j == len(word2):
                memo[(i, j)] = len(word1) - i
                return len(word1) - i

            if word1[i] == word2[j]:
                memo[(i, j)] = minOps(i+1, j+1)
                return minOps(i+1, j+1)
            else:
                insert = 1 + minOps(i, j+1)
                delete = 1 + minOps(i+1, j)
                replace = 1 + minOps(i+1, j+1)

                memo[(i, j)] = min(insert, delete, replace)
                return min(insert, delete, replace)

        ops = minOps(0, 0)

        return ops



        