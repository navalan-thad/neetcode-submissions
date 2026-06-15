class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        len_s = len(s)
        memo = {}

        def dfs(i):
            if i >= len_s:
                return 0

            if i in memo:
                return memo[i]

            min_extra = 1 + dfs(i+1)

            for word in dictionary:
                if s[i:i+len(word)] == word:
                    cand = dfs(i+len(word))
                    min_extra = min(cand, min_extra)

            memo[i] = min_extra
            return min_extra

        return dfs(0)




        