class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        best = ""

        def isDivisor(s, full_str):
            while len(full_str) >= len(s):
                if full_str[:len(s)] == s:
                    full_str = full_str[len(s):]
                else:
                    return False
            return len(full_str) == 0

        GCD = ""
        i = 0
        while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
            GCD += str1[i]
            if isDivisor(GCD, str1) and isDivisor(GCD, str2):
                best = GCD
            i += 1

        return best

        