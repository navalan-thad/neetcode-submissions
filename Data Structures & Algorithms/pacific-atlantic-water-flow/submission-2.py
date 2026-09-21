class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        R, C = len(heights), len(heights[0])

        p_cells = set()
        a_cells = set()

        def dfs(i, j, visited):
            visited.add((i, j))

            for x, y in dirs:
                if 0 <= i+x < R and 0 <= j+y < C:
                    if heights[i][j] <= heights[i+x][j+y] and (i+x, j+y) not in visited:
                        dfs(i+x, j+y, visited)

        for i in range(R):
            dfs(i, 0, p_cells)
            dfs(i, C-1, a_cells)

        for j in range(C):
            dfs(0, j, p_cells)
            dfs(R-1, j, a_cells)
                
        return [[r, c] for r, c in p_cells.intersection(a_cells)]


        