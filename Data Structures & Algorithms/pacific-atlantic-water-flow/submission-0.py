class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n, m = len(heights), len(heights[0])
        atlantic = {}
        pacific = {}

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, tracker):
            if i < 0 or i == n or j < 0 or j == m:
                return

            if (i, j) in tracker:
                return
                
            tracker[(i, j)] = True

            for x, y in dirs:
                if 0 <= i+x < n and 0 <= j+y < m: 
                    if heights[i+x][j+y] >= heights[i][j]:
                        tracker[(i, j)] = True
                        dfs(i+x, y+j, tracker) 

        for i in range(m):
            dfs(0, i, pacific)
            dfs(n-1, i, atlantic)

        for j in range(n):
            dfs(j, 0, pacific)
            dfs(j, m-1, atlantic)

        return list(set(atlantic.keys()).intersection(set(pacific.keys())))

            



        