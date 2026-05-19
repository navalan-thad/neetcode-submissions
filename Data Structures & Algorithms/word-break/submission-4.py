class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def assemble(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return True

            for i in wordDict:
                end = len(i) + start
                if end <= len(s) and s[start:end] == i:
                    res = assemble(end)
                    memo[start] = res
                    if res:
                        return True
            memo[start] = False
            return False

        return assemble(0)

        