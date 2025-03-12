# https://leetcode.com/problems/surrounded-regions/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(row:int,col:int)->None:
            if row<0 or col<0 or row>num_rows-1 or col>num_cols-1 or board[row][col]!='O':
                return
            board[row][col] = '#' # indicates a cell that is connected to the edge of the board
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        # call dfs on cells connected to edges of board

        for col in range(num_cols):
            if board[0][col] == 'O': # top row
                dfs(0,col)
            if board[num_rows-1][col] == 'O': # bottom row
                dfs(num_rows-1,col)

        for row in range(num_rows):
            if board[row][0] == 'O': # left col
                dfs(row, 0)
            if board[row][num_cols-1] == 'O': # right col
                dfs(row, num_cols-1)

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == 'O': # any O that are still O indicates that it was not connected to edge
                    board[row][col] = 'X' # flip them to X
                elif board[row][col] == '#': # indicates it was connected to edge of board
                    board[row][col] = 'O' # flip back to O
