class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s1) and j == len(s2):
                return True

            if i > len(s1) or j > len(s2):
                return False

            branch1 = False
            branch2 = False

            if i < len(s1) and s1[i] == s3[i+j]:
                branch1 = dp(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                branch2 = dp(i, j+1)

            memo[(i, j)] = branch1 or branch2

            return memo[(i, j)]

        return dp(0, 0)

            

        
        