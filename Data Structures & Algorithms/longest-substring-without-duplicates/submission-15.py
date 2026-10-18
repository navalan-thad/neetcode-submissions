class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        longest = 1
        L = 0
        visited = {}

        for R in range(len(s)):
            if s[R] in visited:
                L = max(L, visited[s[R]]+1)

            visited[s[R]] = R
            longest = max(longest, R-L+1)

        return longest
