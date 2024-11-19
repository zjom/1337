# https://leetcode.com/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        startRow,startCol = 0,0
        endRow,endCol = len(matrix)-1, len(matrix[0])-1
        res: list[int] = []

        while startRow <=endRow and startCol<=endCol:
            for i in range(startCol,endCol+1):
                res.append(matrix[startRow][i])
            startRow += 1

            for i in range(startRow, endRow+1):
                res.append(matrix[i][endCol])
            endCol -= 1

            if startRow <= endRow:
                for i in range(endCol, startCol-1, -1):
                    res.append(matrix[endRow][i])
                endRow -= 1

            if startCol <= endCol:
                for i in range(endRow,startRow-1,-1):
                    res.append(matrix[i][startCol])
                startCol += 1

        return res
