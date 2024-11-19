# https://leetcode.com/problems/rotting-oranges/description/
from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    q = deque()
    fresh_oranges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh_oranges += 1
            if grid[i][j] == 2:
                q.append([i, j])

    count = 0
    dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    while len(q) != 0 and fresh_oranges > 0:
        lenq = len(q)
        for i in range(lenq):
            x, y = q.popleft()
            for x_offset, y_offset in dirs:
                next_x, next_y = x+x_offset, y+y_offset
                if next_x < 0 or next_y < 0 or \
                        next_x > len(grid)-1 or \
                        next_y > len(grid[0])-1 or \
                        grid[next_x][next_y] == 2 or \
                        grid[next_x][next_y] == 0:
                    continue
                grid[next_x][next_y] = 2
                fresh_oranges -= 1
                q.append([next_x, next_y])
            count += 1

    return count if fresh_oranges == 0 else -1
