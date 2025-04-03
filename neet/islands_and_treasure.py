# https://neetcode.io/problems/islands-and-treasure

# Islands and Treasure
#
# You are given a m×n 2D grid initialized with these three possible values:
# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
#
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.
#
# Assume the grid can only be traversed up, down, left, or right.
#
# Modify the grid in-place.
#
# Example 1:
#
# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
#
# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# Example 2:
#
# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]
#
# Output: [
#   [0,-1],
#   [1,2]
# ]
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is one of {-1, 0, 2147483647}


from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        q:deque[tuple[int,int]] = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            i,j = q.popleft()
            for x,y in dirs:
                r,c = x+i,y+j
                if r<0 or c<0 or r >=len(grid) or c >= len(grid[0]) or grid[r][c]!=2**31-1:
                    continue
                grid[r][c] = grid[i][j]+1
                q.append((r,c))
