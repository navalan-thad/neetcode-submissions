class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == -1:
                return 1

            double = 0
            single = 0

            if i == 0:
                if s[i] == '0':
                    return 0
            else:
                if 0 < int(s[i-1:i+1]) <= 26 and int(s[i-1]) != 0:
                    double = dfs(i-2)
            
            if s[i] != '0':
                single = dfs(i-1)

            memo[i] = single + double
            return memo[i]
            

        return dfs(len(s)-1)