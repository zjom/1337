# https://neetcode.io/problems/max-area-of-island

# Max Area of Island
#
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
#
# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
#
# The area of an island is defined as the number of cells within the island.
#
# Return the maximum area of an island in grid. If no island exists, return 0.
#
# Example 1:
#
#
#
# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]
#
# Output: 6
# Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.
#
# Constraints:
#
# 1 <= grid.length, grid[i].length <= 50

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        def aux(i:int,j:int)->int:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            for x,y in dirs:
                r,c = i+x,y+j
                res += aux(r,c)
            return res


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                    continue
                res = max(res, aux(i,j))
        return res

s = Solution()
assert s.maxAreaOfIsland(
    [[0,1,1,0,1],
     [1,0,1,0,1],
     [0,1,1,0,1],
     [0,1,0,0,1]]
) == 6



assert s.maxAreaOfIsland(
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
) == 6
