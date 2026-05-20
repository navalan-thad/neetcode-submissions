class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        rowZero = True if 0 in matrix[0] != 0 else False
        colZero = False
        for k in range(m):
            if matrix[k][0] == 0:
                colZero = True
                break

        # store zero rows/cols
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowZero:
            matrix[0] = [0]*n

        if colZero:
            for k in range(m):
                matrix[k][0] = 0




        
        