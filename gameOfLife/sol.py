# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    # Any live cell with fewer than two live neighbors dies as if caused by under-population.
    # Any live cell with two or three live neighbors lives on to the next generation.
    # Any live cell with more than three live neighbors dies, as if by over-population.
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[0,1],
                [0,-1],
                [1,0],
                [1,1],
                [1,-1],
                [-1,0],
                [-1,1],
                [-1,-1]]
        def count_neighbours(i:int,j:int)->int:
            count = 0
            for y,x in dirs:
                curr_y,curr_x = y+i,x+j
                if curr_y < 0 or curr_x < 0 or \
                    curr_y > len(board)-1 or \
                    curr_x > len(board[0])-1 or \
                    board[curr_y][curr_x] == 0 or \
                    board[curr_y][curr_x] == 2:
                    continue
                count += 1
            return count


        # update board to tmp truth table values
        for i in range(len(board)):
            for j in range(len(board[0])):
                nei = count_neighbours(i,j)
                if board[i][j] == 1:
                    if nei == 2 or nei == 3:
                        board[i][j] = 3
                    # if nei < 2 or nei > 3:
                    #     board[i][j] = 1
                elif board[i][j] == 0 and nei == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] <= 1:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
