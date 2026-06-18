class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        r, c = len(matrix), len(matrix[0])
        self.pref = [[0]*(c+1) for _ in range(r+1)]

        for row in range(r):
            for col in range(c):
                self.pref[row+1][col+1] = (matrix[row][col] + self.pref[row][col+1]
                + self.pref[row + 1][col] - self.pref[row][col]
            )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        
        return ( 
            self.pref[r2][c2] - self.pref[r1-1][c2]
            - self.pref[r2][c1-1] + self.pref[r1-1][c1-1]
        )

        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)