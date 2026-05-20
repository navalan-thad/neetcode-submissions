class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        zeroRows = set()
        zeroCols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)

        # zero rows:
        for i in zeroRows:
            matrix[i] = [0] * n

        # zero the cols:
        for i in zeroCols:
            for j in range(m):
                matrix[j][i] = 0

        
        