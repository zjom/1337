# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        q: list[list[int]] = [] # stored positions of zeroes
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # find all zeroes
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    q.append([i,j])

        lenQ = len(q)
        for _ in range(lenQ):
            row,col = q.pop()
            matrix[row] = [0 for _ in matrix[row]]
            for i in range(num_rows):
                matrix[i][col] = 0
