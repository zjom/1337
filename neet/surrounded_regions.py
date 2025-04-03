# https://neetcode.io/problems/surrounded-regions
# Surrounded Regions

from collections import deque

from icecream import ic

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        q:deque[tuple[int,int]] = deque()
        num_rows = len(board)
        num_cols = len(board[0])
        for r in range(num_rows):
            if board[r][0] == 'O':
                q.append((r,0))
            if board[r][num_cols-1] == 'O':
                q.append((r,num_cols-1))
        for c in range(num_cols):
            if board[0][c] == 'O':
                q.append((0,c))
            if board[num_rows-1][c] == 'O':
                q.append((num_rows-1,c))

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r,c = q.popleft()
            board[r][c] = '.'
            for dr,dc in dirs:
                _r, _c = r+dr,c+dc
                if _r < 0 or _r >= num_rows or _c < 0 or _c >= num_cols or board[_r][_c]!='O':
                    continue
                q.append((_r,_c))

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == '.':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'


s = Solution()
board=[["O","X","X","O","X"],
       ["X","O","O","X","O"],
       ["X","O","X","O","X"],
       ["O","X","O","O","O"],
       ["X","X","O","X","O"]]
s.solve(board)
ic(board)

