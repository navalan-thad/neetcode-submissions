class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            left, right, up, down = False, False, False, False

            if k == len(word):
                return True

            if i - 1 >= 0:
                if board[i-1][j] == word[k]:
                    temp = board[i-1][j]
                    board[i-1][j] = "#"
                    left = dfs(i-1, j, k+1)
                    board[i-1][j] = temp

            if i + 1 < len(board):
                if board[i+1][j] == word[k]:
                    temp = board[i+1][j]
                    board[i+1][j] = "#"
                    right = dfs(i+1, j, k+1)
                    board[i+1][j] = temp

            if j - 1 >= 0:
                if board[i][j-1] == word[k]:
                    temp = board[i][j-1]
                    board[i][j-1] = "#"
                    down = dfs(i, j-1, k+1)
                    board[i][j-1] = temp

            if j + 1 < len(board[0]):
                if board[i][j+1] == word[k]:
                    temp = board[i][j+1]
                    board[i][j+1] = "#"
                    up = dfs(i, j+1, k+1)
                    board[i][j+1] = temp

            return any([left, right, up, down])

        inBoard = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "#"
                    inBoard = dfs(i, j, 1)
                    board[i][j] = temp
                    if inBoard:
                        return True
        return inBoard

