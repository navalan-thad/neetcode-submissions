class Solution:
    def countSubstrings(self, s: str) -> int:

        def palinCount(start, end):
            count = 0
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    start -= 1
                    end += 1
                    count += 1
                else:
                    return count

            return count

        total = 0
        for i in range(len(s)):
            total += palinCount(i, i)
            total += palinCount(i, i+1)

        return total


        

        