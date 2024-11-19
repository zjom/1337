from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict[int,set[str]](set)
        cols = defaultdict[int,set[str]](set)
        squares = defaultdict[tuple[int,int],set[str]](set)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in rows[i] or cell in cols[j] or cell in squares[i//3,j//3]:
                    return False

                rows[i].add(cell)
                cols[j].add(cell)
                squares[i//3,j//3].add(cell)
        return True

if __name__ == "__main__":
   print([[f"{i}" for i in range(9)] for _ in range (9)])
