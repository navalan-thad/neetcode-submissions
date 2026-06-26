class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combs = []
        curr = []

        def dfs(i):
            if len(curr) == k:
                combs.append(curr.copy())
                return

            for num in range(i, n+1):
                curr.append(num)
                dfs(num+1)
                curr.pop()

        dfs(1)
        return combs

        