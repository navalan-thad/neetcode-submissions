class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        memo = {}
        
        def dfs(ind):
            if ind == len(s):
                return 0
            if ind in memo:
                return memo[ind]

            extra_chars = 1 + dfs(ind+1) # skip char at current index

            for word in dictionary:
                if word == s[ind:ind+len(word)]:
                    candidate = dfs(ind+len(word))
                    extra_chars = min(extra_chars, candidate)
            
            memo[ind] = extra_chars
            return memo[ind]

        return dfs(0)

            



            

        