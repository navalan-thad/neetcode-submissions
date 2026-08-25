class Solution:
    def validPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1
        while L < R:
            if s[L] != s[R]:
                skip_left = s[L+1:R+1]
                skip_right = s[L:R]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            L += 1
            R -= 1

        return True
