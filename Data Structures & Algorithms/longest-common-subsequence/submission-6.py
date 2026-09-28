class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        def dp(j, k):
            if (j, k) in memo:
                return memo[(j, k)]
            if j == len(text1) or k == len(text2):
                return 0
            
            match = 0
            no_match = 0

            if text1[j] == text2[k]:
                match = dp(j+1, k+1) + 1
            else:
                no_match = max(dp(j, k+1), dp(j+1, k))

            memo[(j, k)] = max(match, no_match)
            return memo[(j, k)]

        return dp(0, 0)


        
        