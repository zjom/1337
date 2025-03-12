# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def aux(row:int,col:int,i:int):
            if i == len(word):
                return True

            if (row < 0 or row >= len(board) or 
                col < 0 or col >=len(board[0])or
                board[row][col] != word[i]):
                return False
            
            temp = board[row][col]
            board[row][col] = ''
            if (aux(row+1,col,i+1) or aux(row-1,col,i+1) or
                aux(row, col+1, i+1) or aux(row, col-1, i+1)):
                return True

            board[row][col] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if aux(row, col,0):
                    return True

        return False
