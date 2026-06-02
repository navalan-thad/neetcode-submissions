class Solution:
    def solve(self, board: List[List[str]]) -> None:

        n, m = len(board), len(board[0])

        safe = {}
        neighbors = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j):
            if i == n or j == m or i < 0 or j < 0:
                return

            if (i, j) in safe:
                return safe[(i, j)]

            if board[i][j] == 'O':
                safe[(i, j)] = True

                for x, y in neighbors:
                    dfs(i+x, j+y)
            else:
                return

        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[n-1][i] == 'O':
                dfs(n-1, i)

        for j in range(n):
            if board[j][0] == 'O':
                dfs(j, 0)
            if board[j][m-1] == 'O':
                dfs(j, m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i, j) not in safe:
                    board[i][j] = 'X'




    

        

        