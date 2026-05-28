class Solution:
    def partition(self, s: str) -> List[List[str]]:

        subs = []
        curr = []

        def dfs(i):
            if i == len(s):
                subs.append(curr.copy())
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()

        dfs(0)

        return subs

            
        