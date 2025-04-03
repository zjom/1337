# https://neetcode.io/problems/count-number-of-islands

# Number of Islands
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
#
# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.
# You may assume water is surrounding the grid (i.e., all the edges are water).
# Example 1:
#
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1
# Example 2:
#
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 100
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(i:int,j:int):
            # bounds check
            if i<0 or i>=len(grid) or j < 0 or j >= len(grid[0]):
                return

            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for x,y in dirs:
                dfs(x+i,y+j)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count += 1

        return count
