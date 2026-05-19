class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        pairs = []
        def dfs(curr, open_used, closed):
            if open_used == closed == n:
                pairs.append("".join(curr))
                return

            if open_used < n:
                curr.append('(')
                dfs(curr, open_used+1, closed)
                curr.pop()

            if closed < open_used:
                curr.append(')')
                dfs(curr, open_used, closed+1)
                curr.pop()

            
        curr = []
        dfs(curr, 0, 0)
        return pairs
        