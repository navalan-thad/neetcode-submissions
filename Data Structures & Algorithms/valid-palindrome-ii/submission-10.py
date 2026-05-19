class Solution:
    def validPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1

        def isPalin(string):
            for i in range(len(string)//2):
                if string[i] != string[len(string)-i-1]:
                    return False
            return True

        while start < end:
            if s[start] != s[end]:
                return isPalin(s[start+1:end+1]) or isPalin(s[start:end])
            start += 1
            end -= 1

        return True

        