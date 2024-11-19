# https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix)-1

        while left <= right:
            for i in range(right - left):
                top, bottom = left, right

                # save top left variable
                top_left = matrix[top][left+i]

                # move bottom left to top left
                matrix[top][left+i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]

                # move top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                # move saved top left to top right
                matrix[top+i][right] = top_left
            right -= 1
            left += 1

