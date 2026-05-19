class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    p += 4

                    # check up
                    if i > 0 and grid[i-1][j] == 1:
                        p -= 1
                    # check down
                    if i < rows - 1 and grid[i+1][j] == 1:
                        p -= 1
                    # check left
                    if j > 0 and grid[i][j-1] == 1:
                        p -= 1
                    # check right
                    if j < cols - 1 and grid[i][j+1] == 1:
                        p -= 1

        return p


        


        