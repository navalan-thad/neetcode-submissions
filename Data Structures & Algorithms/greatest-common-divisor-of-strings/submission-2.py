class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        gcd = ""
        best = ""

        def isDivisor(s, full):
            while len(full) >= len(s):
                if full[:len(s)] == s:
                    full = full[len(s):]
                else:
                    return False

            return len(full) == 0

        i = 0

        while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
            gcd += str1[i]
            if isDivisor(gcd, str1) and isDivisor(gcd, str2):
                best = gcd
            i += 1
        
        return best
            

        