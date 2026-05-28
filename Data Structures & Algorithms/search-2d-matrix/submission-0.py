class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        L = 0
        R = m*n -1

        while L <= R:
            mid = (L + R) // 2
            row = mid // n
            col = mid % n

            if target > matrix[row][col]:
                L = mid + 1
            elif target < matrix[row][col]:
                R = mid - 1
            else:
                return True

        return False



        