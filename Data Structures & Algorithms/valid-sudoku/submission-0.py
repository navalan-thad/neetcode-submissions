class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(len(board)):
            rowCounts = {}
            colCounts = {}
            for col in range(len(board[0])):

                # row condition
                if board[row][col] != '.':
                    if board[row][col] in rowCounts:
                        return False
                    else:
                        rowCounts[board[row][col]] = (row, col)

                # col condition
                if board[col][row] != '.':
                    if board[col][row] in colCounts:
                        return False
                    else:
                        colCounts[board[col][row]] = (col, row)

        # sub-square condition
        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                visited = {}
                for i in range(3):
                    for j in range(3):
                        r = row + i
                        c = col + j
                        if board[r][c] != '.':
                            if board[r][c] in visited:
                                return False
                            else:
                                visited[board[r][c]] = (r, c)
        return True



        

        
        