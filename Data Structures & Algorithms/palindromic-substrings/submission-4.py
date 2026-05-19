class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    count += 1
                else:
                    return count
            return count

        total = 0
        for i in range(len(s)):
            total += expand(i, i) + expand(i, i+1)
        return total



        

        