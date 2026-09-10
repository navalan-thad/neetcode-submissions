class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combs = []
        curr = []
        
        def dfs(i):
            if len(curr) == k:
                combs.append(curr.copy())
                return
                
            if len(curr) + (n-i + 1) < k:
                return

            curr.append(i)
            dfs(i+1)
            curr.pop()
            dfs(i+1)


        dfs(1)
        return combs

            

        
        