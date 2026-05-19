class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        start = 0
        longest = 0

        for i in range(len(s)):

            # duplicate inside current window
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)

            seen[s[i]] = i

            longest = max(longest, i - start + 1)

        return longest