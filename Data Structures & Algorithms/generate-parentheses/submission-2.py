class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        pairs = []
        curr = []

        def dfs(curr, open_used, close):
            if open_used == close == n:
                pairs.append("".join(curr))
                return

            if open_used < n:
                curr.append('(')
                dfs(curr, open_used+1, close)
                curr.pop()

            if close < open_used:
                curr.append(')')
                dfs(curr, open_used, close+1)
                curr.pop()

        dfs(curr, 0, 0)
        return pairs

       
        