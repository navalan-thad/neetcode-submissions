class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])
        soln = []
        visited = set()

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # spiral direction
        curr = 0

        i, j = 0, 0

        while len(soln) < m*n:

            if (i, j) not in visited:
                visited.add((i, j))
                soln.append((matrix[i][j]))
                
            next_i = i + dirs[curr][0]
            next_j = j + dirs[curr][1]

            if (next_i, next_j) not in visited and 0 <= next_i < m and 0 <= next_j < n:
                i, j = next_i, next_j
            else:
                curr = (curr + 1) % 4

        return soln
        