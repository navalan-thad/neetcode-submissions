class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0] * rows for _ in range(cols)]
        
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = matrix[j][i]

        return result

