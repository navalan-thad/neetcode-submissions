class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        longest = 0
        start = 0

        for i in range(len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]]+1)
            seen[s[i]] = i
            longest = max(longest, i-start+1)

        return longest
