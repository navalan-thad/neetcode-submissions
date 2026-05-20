class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n == 1:
            return matrix

        # vertical translation
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                

        