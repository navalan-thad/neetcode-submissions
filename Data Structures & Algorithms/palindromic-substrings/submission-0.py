class Solution:
    def countSubstrings(self, s: str) -> int:

        table = [[False for _ in range(len(s))] for _ in range(len(s))]

        def dp(start, end):
            if table[start][end]:
                return True
            if start == end:
                table[start][end] = True
                return True
            if start+1 == end and s[start] == s[end]:
                table[start][end] = True
                return True
            if s[start] == s[end] and dp(start+1, end-1):
                table[start][end] = True
                return True
            return False

        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp(i, j):
                    count += 1
        return count



        

        