class Solution:
    def validPalindrome(self, s: str) -> bool:

        if len(s) <=2:
            return True

        def isPalin(string):
            for i in range(len(string)//2):
                if string[i] != string[len(string)-i-1]:
                    return False
            return True

        res1 = isPalin(s)
        print(res1)

        for i in range(len(s)):
            cand = s[:i] + s[i+1:] 
            if isPalin(cand):
                return True

        return res1
        