class Solution:
    def validPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1

        def isPalin(left, right, string):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        while start < end:
            if s[start] != s[end]:
                return isPalin(start, end-1, s) or isPalin(start+1, end, s)
            start += 1
            end -= 1

        return True

        