class Solution:
    def longestPalindrome(self, s: str) -> str:

        memo = {}

        def isPalin(i, j):
            if i == j:
                return True
            if i > j:
                return True

            if (i, j) in memo:
                return memo[(i, j)]
            else:
                res = s[i] == s[j] and isPalin(i+1, j-1)
                memo[(i, j)] = res
                return res

        longest = s[0]

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if isPalin(i, j) and (j-i+1 > len(longest)):
                    longest = s[i:j+1]

        return longest


    




        